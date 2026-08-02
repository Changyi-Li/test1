## Question

每个 Help 主题页有哪些可靠元数据，可用于增量同步与版本记录？

需要调查：
- HTTP 响应头（Last-Modified / ETag / Cache-Control）对 .htm 页面的行为；If-Modified-Since / If-None-Match 条件请求是否生效（.cn 英文页、中文页分别验证）。
- 页面内嵌元数据：<title>、面包屑、页脚版本/日期、页面内“最后更新”标记等，哪些稳定可用。
- .cn 与 .com 英文页时间戳不一致的成因（已知 .com 更新），中文页时间戳行为如何。
- 用哪个信号做增量比较最可靠、成本最低（响应头 vs 页面内容 hash vs 页面内时间戳）。

输出：facts + 增量信号建议（写进 findings.md）。
