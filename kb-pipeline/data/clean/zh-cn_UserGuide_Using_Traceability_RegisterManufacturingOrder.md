### 登记工单

#### 序列号层级的序列号的可追溯性
当为具有可追溯性级别的为组件已创建工单时 序列号，序列号将总是被已创建并与工单相链接。
如果人工的已创建制造订单或通过工单建议（未链接到客户订单）创建工单，则将从序列号的编号序列中加载该编号。这可以在 编号序列 程序。
如果工单是创建自客户订单或从与客户订单已链接工单建议创建的，其中已经生成了序列号，则这些序列号将从工单的客户订单行行继承。否则，它们是创建自编号序列创建的。
如果已创建了结构订单，其中包含的组件也具有序列号的可追溯性，则也会为这些部件已创建序列号。序列号总是与工单中的组件代码（包含的生产件）链接至。
在序列号标签页下 编号序列 程序，你可以选择如何生成序列号至。除了常规的编号序列附加，还可以为序列号激活其它前缀或后缀。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/SerialnumberManufacturingOrder.png)](../../../../Resources/Images/TrainingMaterial/SerialnumberManufacturingOrder.png)
你可以在工单文档上显示序列号。这是每文档的设置确定的 显示序列号 在程序中 文档模板 - 工单。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/SerialnumberManufacturingOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/SerialnumberManufacturingOrderDocument.png)
