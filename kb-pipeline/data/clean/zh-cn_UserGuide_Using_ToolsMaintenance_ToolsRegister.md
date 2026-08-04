### 工具登记
在 Monitor ERP，你处理工具在 组件登记 通过程序 基本类型 为工具。这意味着实际上全部处理组件的程序也处理工具。

#### 组件模板
在里面 组件模板 程序，你查询为工具的基本类型。为了能够处理工具，你必须第一个为你使用的工具和设备类型创建组件模板。你必须每基本类型创建至少一模板。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/PartTemplate.png)](../../../../Resources/Images/TrainingMaterial/PartTemplate.png)
为工具的基本类型
为工具有三种不同的基本类型。确保为工具你正确的基本类型，因为它决定了可用的功能：
-   
消耗 – 这种类型的实际工作方式与常规的组件相同。这是用于已报告时消耗的工具。这通常用于消耗工具、耗材和备件。
-   
可重复使用的 – 这可能是最常用的基本类型。类型工具通过从库存中领用并退回至仓库处理。如果你想要进行维护和校准，则总是使用可重复使用使用。然后，你还必须使用在组件模板中已增加的序列号的可追溯性。你可以为不同类型的工具（例如测量工具、夹具和设备）创建多个组件模板。
-   
工具列表 – 此类型主要用于创建可在多个BOM 和工艺路线中重复使用的虚拟件工具清单。将会针对此基本类型开发更多功能。
> 提示！为工具和常规的组件创建单独的查找格式可能是一个好主意。

#### 组件登记
你登记在 组件登记 程序。大多数可为常规的组件已配置的设置也可为工具已配置。许多设置可以通过组件模板默认设置，例如序列号的可追溯性和计划设置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsInPartRegister.png)](../../../../Resources/Images/TrainingMaterial/ToolsInPartRegister.png)
> 提示！对于消耗工具，使用计划方式可能是一个好主意 库存再补充。输入再订购点、订单数量、供应商和交期，可以轻松进行采购管理 库存补充 - 采购 程序。
