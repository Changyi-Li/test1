![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Options/NestingSoftwareIntegration.png)

# 嵌套软件集成
嵌套软件集成是MONITOR G5 的一个选项，允许你在MONITOR和嵌套系统在中间传输信息。这使得生产计划更加完善，并且更容易保持材料消耗。

#### 技术
嵌套软件集成作为两项服务安装在您的MONITOR服务器上；一用于 Web客户端，一用于集成。Web客户端是内部的，用于配置集成的多样的设置。
MONITOR和嵌套程序在中间的通信通过 XML文件进行。

#### 导出
该集成可识别何时为已选择的生产组已创建工序，并将订单文件发送到接收嵌套系统。然后操作员将在嵌套系统的任务列表中看到此工序。你还可以使用 BAP – 业务Adaptation插件人工的导出工序。
如果在 Monitor的工序数量或日期发生已变更，则会已发送信息并更新嵌套系统中的工序。如果在 Monitor移除该工序，则在排料程序中该操作也会被移除。
可以从MONITOR中已导出以下字段：
- 行动报告号
- 生产订单的报告号
- 计划开始日期
- 计划完成日期
- 生产件零件的编号和名称
- 物料组件号和名称
- 当前组件版本
- 图号
- 物料批次号
- 在 Monitor的客户
- 在 Monitor的客户的订单号。

#### 导入
当一个套料被切割后，套料系统后退MONITOR报告，并报告套料中被用于的每个工序。你还可以使用嵌套信息来更新生产件的BOM 与工艺路线。
如果已报告的物料与实际使用的材料不同，则集成时导入将重置原始物料需求，使用新建一设置新建的物料需求，然后报告。当同一类型的物料有不同的组件编号（例如不同尺寸）时，就会发生这种情况。
可以已报告以下情况：
- 数量
- 单位时间
- 准备时间
- 每细节的物料用途
- 物料单位
- 批次(物料)
- 物料浪费

#### 组件导入
可以数据从嵌套程序导入组件数据，然后在 Monitor创建/更新组件，以及在BOM 与工艺路线 和组件工艺路线中创建/更新工序和物料行行。
这提供了更多准确的按标准计算，从而可以更好地概览生产和成本。
可已导入的组件数据如下：
- 组件号和名称
- 单位时间
- 准备时间
- 物料组件号
- 物料每
- 这里你可以看到物料的单位。
如果嵌套系统可以已导出数据，那么也可以导入数据。

#### 目前支持排料程序
| 供应商 | 地址 | 联系人 | 信息 |
|---|---|---|---|
| Bystronic BySoft CAM | [链接](https://www.bystronic.se/se/Produkter/programvara/BySoft-CAM.php) | Chris Waters |软件专家chris.waters@bystronic.com | 为了能够充分利用集成中的功能， 工厂经理 需要 BySoft CAM 中的模块。无需工厂经理即可使用组件导入。在这种案件下， Nester组件 需要模块。 |
| TRUMPF TruTops Boost | [链接](https://www.trumpf.com/sv_SE/produkter/mjukvara/programmeringssystem/trutops-boost/) |   |   |
| 六角 RADAN Radnest (MAZAK) | [链接](https://www.radan.com/combination/radanradnest) |   |   |
有兴趣下班更多？请联系人我们的销售部门 [表格](https://www.monitorerp.com/contact-us/)。
