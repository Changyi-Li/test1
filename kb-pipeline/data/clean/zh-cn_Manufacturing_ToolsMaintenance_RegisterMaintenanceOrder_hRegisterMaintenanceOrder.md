### 页眉行

#### 订单号
你可以在此处载入现有的维护订单的订单号。对于新建的维护订单，当你保存订单时会已分配订单号。这是从工单编号序列中的下一个可用编号加载的。维护订单是一种工单，它基于基本类型“维护”的单独订单类型。
> 请注意！在查找功能中你还可以看到常规的工单。如果你在此程序中载入常规的工单，则不对该订单进行任何变更。

#### 序列号 / 批次号
你为此处你第一个的序列号创建新建的维护订单。在报告维护订单时，已建议使用此序列号，然后已报告。

#### 维护
在这里，你可以执行由选择维护模板来选择要执行的维护。你可以选择的维护模板是那些已链接至维护计划中具有序列号的组件的模板。在字段的列表中，你还可以看到维护模板已链接到哪个维护计划。

#### 组件
在这里你选择包含维护中应该使用的BOM 与工艺路线的生产件。一次你已保存了订单，它就会显示在工序框和物料框中。这里的默认组件是维护模板中已配置使用BOM 与工艺路线的组件。如果维护模板中否输入 此组件, 则默认使用序列号的组件.

#### 配置
如果已选择的组件链接至配置组，则会可用一个用于订单配置的按钮。如果按钮显示此符号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Button_Configuration_Available.png) 表示配置错误的或者不完整。通过单击此按钮，你访问配置窗口，你可以在其中配置该组件。你按钮确认配置时 确认 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) 在那个窗口中，按钮上的符号将会更改 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Button_Configuration_Done.png)，说明该组件已已配置。
组件可以具有在组件登记中确定的默认配置，并且在这种案件下，该配置将自动加载到维护事项中。

#### 评论
你可以在这里输入维护订单的评论。
单击此按钮，你访问文本编辑器，你可以在其中编写和格式文本、插入图像和签名以及超链接等。当有评论/文本时，按钮上的符号将从空的气泡更改 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_no_comment.png) 到已填满的对话泡泡 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。

#### 变量代码
你可以在此处输入变量代码，订单将变量代码用于已选择生产件中的加工工序行和物料行。

#### 仓库
字段​ 仓库 选项已安装。你可以在这里为维护订单选择一个仓库。默认已选择当前仓库。如果你选择的仓库其它已选择生产件所属的仓库，然后你保存，列名为 仓库 将显示在全部工序行和物料行上。在此列你查询一个符号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_warehouses_alt.png) 带有工具提示。加工工序行，它可以让你知道该行属于不同的仓库，对于物料行，它可以让你知道物料将从不同的仓库中领用/已扣减。
