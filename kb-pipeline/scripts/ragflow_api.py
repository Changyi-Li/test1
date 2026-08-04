"""RAGFlow HTTP API 薄客户端（导入工具，接缝 6）。

使用 stdlib urllib.request（与仓库 pipeline.py 一致，零第三方依赖）。所有
端点统一：code==0 返回 data，否则抛 RagflowError。multipart 上传手工构造，
文件名=clean 文件名（即 RAGFlow 文档名）。
"""
from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any
from urllib import error, request

urlopen = request.urlopen  # 测试可 monkeypatch

DEFAULT_TIMEOUT = 30


class RagflowError(RuntimeError):
    pass


def _items(data: Any) -> list:
    """把分页响应（list / {items:[...]} / {docs:[...]}）统一成可迭代条目。

    v0.26.4 的文档列表用 `docs` 键，数据集列表直接是 list——都要兼容。
    """
    if isinstance(data, dict):
        items = data.get("items")
        if items is None:
            items = data.get("docs")
        return items or []
    return data or []


def _multipart_body(file_path: Path, boundary: str) -> bytes:
    name = file_path.name
    head = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{name}"\r\n'
        "Content-Type: text/markdown\r\n"
        "\r\n"
    ).encode("utf-8")
    tail = f"\r\n--{boundary}--\r\n".encode("utf-8")
    return head + file_path.read_bytes() + tail


class RagflowClient:
    def __init__(self, base_url: str, api_key: str, timeout: int = DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def _headers(self, content_type: str | None = None) -> dict[str, str]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if content_type is not None:
            headers["Content-Type"] = content_type
        return headers

    def _request(self, method: str, path: str,
                 body: object | None = None,
                 headers: dict[str, str] | None = None) -> Any:
        url = f"{self.base_url}{path}"
        payload = None
        final_headers = self._headers()
        if headers:
            final_headers.update(headers)
        if isinstance(body, bytes):
            payload = body
        elif body is not None:
            final_headers["Content-Type"] = "application/json"
            payload = json.dumps(body).encode("utf-8")
        req = request.Request(url, data=payload, headers=final_headers,
                              method=method)
        try:
            with urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8")
        except error.HTTPError as exc:
            raise RagflowError(f"HTTP {exc.code} {method} {path}: {exc.reason}")
        except error.URLError as exc:
            raise RagflowError(f"网络错误 {method} {path}: {exc.reason}")
        try:
            payload_json = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RagflowError(f"RAGFlow 响应不是 JSON（{method} {path}）: {exc}")
        if payload_json.get("code") != 0:
            raise RagflowError(
                f"RAGFlow 返回 code={payload_json.get('code')}: "
                f"{payload_json.get('message')}（{method} {path}）")
        return payload_json.get("data")

    # -- 数据集 --
    def create_dataset(self, name: str, chunk_method: str,
                       parser_config: dict, embedding_model: str = "",
                       permission: str = "me") -> dict:
        body: dict = {
            "name": name, "chunk_method": chunk_method,
            "parser_config": parser_config, "permission": permission,
        }
        if embedding_model:
            body["embedding_model"] = embedding_model
        data = self._request("POST", "/api/v1/datasets", body=body)
        return data if isinstance(data, dict) else {}

    def list_datasets(self) -> list[dict]:
        data = self._request("GET", "/api/v1/datasets?page=1&page_size=100")
        return [d for d in _items(data) if isinstance(d, dict)]

    # -- 文档 --
    PAGE_SIZE = 100  # RAGFlow 上限

    def list_documents(self, dataset_id: str) -> list[dict]:
        docs: list[dict] = []
        page = 1
        while True:
            data = self._request(
                "GET",
                f"/api/v1/datasets/{dataset_id}/documents"
                f"?page={page}&page_size={self.PAGE_SIZE}")
            items = [d for d in _items(data) if isinstance(d, dict)]
            docs.extend(items)
            if len(items) < self.PAGE_SIZE:
                break
            page += 1
        return docs

    def upload_document(self, dataset_id: str, file_path: Path) -> dict:
        boundary = "----MonitorErp" + uuid.uuid4().hex
        body = _multipart_body(Path(file_path), boundary)
        headers = self._headers(f"multipart/form-data; boundary={boundary}")
        data = self._request("POST", f"/api/v1/datasets/{dataset_id}/documents",
                             body=body, headers=headers)
        docs = _items(data)
        if not docs:
            raise RagflowError(f"上传后未返回文档记录: {file_path.name}")
        first = docs[0]
        if not isinstance(first, dict) or "id" not in first:
            raise RagflowError(f"上传响应缺少文档 id: {file_path.name}")
        return first

    def delete_documents(self, dataset_id: str, doc_ids: list[str]) -> None:
        if not doc_ids:
            return
        self._request("DELETE", f"/api/v1/datasets/{dataset_id}/documents",
                      body={"ids": doc_ids, "delete_all": False})

    def update_document_metadata(self, dataset_id: str, doc_id: str,
                                 meta_fields: dict[str, str]) -> None:
        self._request(
            "PUT", f"/api/v1/datasets/{dataset_id}/documents/{doc_id}",
            body={"meta_fields": meta_fields})

    def trigger_parse(self, dataset_id: str, doc_ids: list[str]) -> None:
        if not doc_ids:
            return
        self._request("POST", f"/api/v1/datasets/{dataset_id}/chunks",
                      body={"document_ids": doc_ids})

    # 注: v0.26.4 的 GET /documents/{id} 返回文档正文（非 JSON 元数据），
    # 轮询解析状态统一走 list_documents 的 run 字段，不提供 get_document。

    # -- 检索 --
    def retrieve(self, dataset_ids: list[str], question: str,
                 top_k: int = 5, **kwargs) -> dict:
        body: dict = {"question": question, "dataset_ids": dataset_ids,
                      "top_k": top_k, **kwargs}
        data = self._request("POST", "/api/v1/retrieval", body=body)
        return data if isinstance(data, dict) else {}
