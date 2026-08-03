### 组成 (构造图)
这种列表显示已经进行盘点的组件。在这些组件下方，你可以看到它们的结构。
顶部组件节点默认默认为 。对于已选择的组件，你将看到它被用于在哪些其它结构组件中。这显示在 [被用于在](bIncludedIn.htm) 列表。
如果你已选择组件不包含任何物料或工序，则它们将以无结构显示。这样做是订单能够执行“被用于”采购件的分析。如果你还已选择了要显示的工序，它们将与有关工序号和工序名称的信息一起被用于在结构中。
功能按钮
有功能按钮可以在打印之前预览列表并打印它。在预览窗口中，你可以选择或不在打印中包括选择视图。你可以使用按钮在记录中搜索（Ctrl + B）并将其待复制到 剪贴板。你可以使用一个按钮来展开和最小化（班次 + F8）结构中的全部节点。还有一个按钮可以在相关程序中打开标记的记录。

#### 组件类型 / 工序
在第一个列中，你可以看到用符号表示的组件类型 / 工序。

#### 基本类型
这里你可以看到该组件的基本类型。它是从与该组件链接至的组件模板加载的。基本类型主要用于工具，可用 工具与维护 选项已安装。

#### 组件 / 工序
此列显示组件号或工序号。

#### 名称
你可以在此处看到组件名称或工序名称。

#### 数量
此列以默认单位（标准单位）显示主组件的物料数量。

#### 组件状态
一个组件有七种不同的状态。这些反映了部件的生命周期（以及未激活组件的附加状态），低于表格的状态阶段所示：
| 象征 | 代码 | 名称 |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeFictitious.png) | 1 | 报价 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypePrototype.png) | 2 | 样品 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/green_dot.png) | 3 | 新组件 |
|   | 4 | 正常的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeUpgrade.png) | 5 | 新版本 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDowngrade.png) | 6 | 逐步淘汰 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDeleted.png) | 9 | 过时的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/RedPadlock.png) | 99 | 未激活 |
不同组件状态是固定的。不添加或删除组件状态。例如，在订单行上显示组件的状态。你可以根据不同列表中的组件状态选择。
新的组件将获得默认组件状态，该状态由系统设置决定 新组件的默认状态。
更多信息按钮
点击 更多信息 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 在列表的最左边，你查询附加列，其中包含来自BOM 与工艺路线和组件登记的信息。
