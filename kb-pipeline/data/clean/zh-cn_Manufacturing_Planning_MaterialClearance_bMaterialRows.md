### 物料行
在此框中，你可以看到一个表格，其中包含属于已选择订单的物料 预留状态 盒子。
功能菜单
随着 查询 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_search.png) （Ctrl + B）你可以在表格的全部列中搜索你输入的短语。
使用按钮 复制记录到剪贴板 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy.png) 你可以复制记录到剪贴板，包括组件节点，组件，物料或工单。
使用按钮 转到程序 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_link.png) 你可以为余额 - 组件创建监控任务。
使用按钮 展开所有 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_expand_collapse.png) （班次 +F8）你可以展开所有物料行，查看每个物料的批次号 / 序列号，以及查看物料在哪些库位，并你输入要预留的输入数量。你还可以使用箭头按钮展开个体物料行 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_expand_row.png) 位于表格最左边。
使用按钮 显示所有组件 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_part_structure.png) 你可以决定是否显示全部组件。
使用按钮 显示所有工具 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_tools.png) 你可以决定是否显示全部工具。

#### 显示
在框的最顶部，你可以用这个设置来决定是否 全部物料 或者如果 仅短缺物料 应显示在框中。

#### 已预留物料（当前日程表图表）
如果物料被已预留，你会看到 当前日程表图表 在此列中。

#### 类型
对于可追溯物料，你将在这里看到一个符号，表示物料的可追溯性类型；批次 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/batch_image.png) 或序列号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/serialnumber_image.png)。对于库位，你可以在此处看到一个符号，代表所关注的库位类型：线边库、工作中心的线边库或到货库位。

#### 订单号
在此列中，你可以看到物料所属的工单编号。如果物料短缺，订单号会显示在 红色的。

#### 项目
如果批次号与项目相链接，你将在此列中看到项目号。

#### 组件节点
在这里你可以看到物料所属的订单结构中的组件节点。

#### 加工工序
在这里你可以看到将要使用该物料的工序。

#### B (基本类型)
这里你可以看到该组件的基本类型。工具以符号和工具提示显示。

#### 物料组件号
此字段显示物料组件号。

#### 名称
这里你可以看到物料的名称。

#### 已预留
在此列，你可以看到已建议预留的物料数量。如果你该行，你每库位更改已建议数量以预留。系统根据可用库位的账龄分析建议预留。然后进行校验，确保输入的数量不大于库位余额。总数量必须与物料需求相同。也就是说，你不能预留组件物料需求，或预留更多可丢弃物料的物料。

#### 已预留数量
顶部行显示的是已经已预留的数量。在接下来的行中，数量会根据每个行所规定的需求而增加，订单将即将已预留关的内容考虑在内。这用于查看组件的余额可以使用多长时间。
物料的已过期数量也显示在这里。

#### 当前余额
在这里你可以看到 当前余额 当前余额是当前库位上的组件余额。 已选择仓库中的物料。你从程序的工具栏中选择仓库。

#### 可用余额
在此列中，你可以看到 可用余额 可用余额是库位上的当前组件余额减去已预留数量。 的物料。

#### 物料需求
在这里你可以看到该订单的物料需求。是订单剩余的物料数量。

#### 可支配余额
在此列中，你可以看到 可支配余额 可支配余额是组件的当前库位余额在给定时间减去预定数量加上订购数量。 的物料。如果物料短缺，短缺值将显示为值低于 红色的。

#### 需求日期
在这里你可以看到物料需求发生的日期。

#### 此前最佳
如果 此前最佳 应用组件登记中的物料，此日期将显示在这里。如果日期是今天或过去的时间，则将显示日期 红色的。物料是根据此前最佳进行分类的。

#### 费用号
在这里你可以看到自供应商的费用号（如果有），该编号是在到货报告物料到货时输入的。
