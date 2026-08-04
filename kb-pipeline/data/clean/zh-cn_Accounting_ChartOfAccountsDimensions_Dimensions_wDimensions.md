## 维度
在此程序中，你可以定义你过账的不同维度。你登记和名称的维度可以在系统的许多程序中找到。例如，你会在全部过账窗口、凭证、清单和报告中查询它们。
Monitor ERP 可处理最多八个过账维度。
当你登记新建的维度时，它们将自动被用于在例如过账窗口、选择行（包含维度）更多中。但是，新建的维度不自动被用于在系统的列表或报告中。为了显示这些内容，你需要在相关列表的配置中添加新建的维度。
例如，如果你添加了新建的第四个过账维度并希望它显示在总账中，然后你需要配置总账以使新建列出现。对于日记账打印，这些文档中会自动已添加新建的维度。
> 提示！订单使维度适合文档，你可以更改 布局 将文档的设置从“竖着”改为“横向”。这是在会计标签页下完成的，该程序名为 文档设置。这然后应用至全部日记账文档和会计订单文档。更多高级选项的解决方案是调整文档的模板，以允许适合维度的空间。在这种案件下，应在 文档模板 程序，但这需要你了解 DevExpress报告设计器。
你还可以创建 维度组 维度。这样做的目的是能够将一个维度中的多个维度代码组为上级术语，以用于报告目的。你可以为不同的业务领域或不同的项目类型（例如客户项目、固定资产项目或开发项目）创建维度组。
在此程序中，你还可以登记具有可用于在每个维度中登记的维度代码的基本表。这是在名为 维度代码。如果维度链接至登记，那么你将看到维度中可用于记录的代码，例如项目表格。

#### 你是否希望更多深入地跟进会计？
你可以通过以下登记链接至的维度自动过账过账来更多深入地跟进会计：
- 组件
- 组件代码
- 产品组
- 客户
- 供应商
- 工作中心
- 部门
- 员工
- 客户组 (客户)
- 客户区域
- 客户类型
目的是能够在过账上面条款的基于，更多深入层级分析、跟进和衡量盈利能力。若要过账到上面一登记中，你其登记为单独的维度。然后，你激活在​ 会计科目表 程序。在会计中也可以按照这些维度来做预算。
系统中可用以下维度的自动过账：
|   | 项目 | 产品组 | 组件 | 部门 | 工作中心 | 客户 | 供应商 | 员工 | 客户组 (客户) | 客户区域 | 客户类型 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 客户订单 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png)（销售员） | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
| 应收账款（付款） |   |   |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png)（销售员） |   |   |   |
| 采购订单 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |
| 应付账款（收款） |   |   |   |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |
| 直接库存报告 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |   |   |   |   |
| 计提会计 |   |   |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |
| 固定资产登记 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png)（使用由） |   |   |   |
| 库存事务 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 工单（工作） | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 价格变更 |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |   |
| 计算差异 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |   |   |
| 发票日志 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
