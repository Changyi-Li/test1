# 条款和定义
共同的你列表查询​​ Monitor ERP。
A
-    
ABC
ABC 代码用于按销售数量对组件范围进行分类。这些代码被用作衡量周转最多钱的组件的尺度。营业额是通过将组件的价格乘以年销量来计算的。周转最多钱的组件称为“A组件”，之后称为“B组件”等。
B
-    
Balance accuracy
Balance accuracy is a metric that indicates the extent to which the recorded stock balance matches the actual physical quantity in stock.
-    
Balance sheet total
The balance sheet total is the sum of assets, or the sum of liabilities and equity, in the balance sheet.
C
-    
CDT
CDT 是检查交付时间的缩写，它是订单行上的一个函数，它计算相关订单行何时可以交付，同时考虑交期和产出时间。CDT 还会检查现有订单和建议是否可以弥补物料短缺（若有），并影响订单行何时可以交付。
-    
Cost center (CC)
A cost center can be a department, a branch of operation, work centers, areas of responsibility or similar to which costs are assigned.
-    
Cost unit (CU)
A cost unit could be, for example, a product group to which you assign a cost.
D
-    
Dimensions
Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results.An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project.In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up.
E
-    
EDI
EDI 是电子数据交换的首字母缩写。EDI 是关于与您的业务合作伙伴交换电子商务文件，例如客户和供应商。EDI 的概念可能很宽泛且有点不清楚，并且可以多次用于以电子方式发送的所有类型的文档，即使它可能是通过 Email 发送的 PDF 文件或在网站上发布的业务文档。我们所说的 EDI——以及传统意义上的 EDI——是结构化的商业文件，遵循给定的标准，以电子方式发送或接收，自动编译和解释，并与客户/供应商的 ERP 系统集成。
-    
Efficiency factor (E-factor)
这是对计划时间和实际时间的结果的度量。计算方式如下：E = 计划时间 * 报告数量 /（报告时间 x 计划数量）
F
-    
FIFO
此价格是通过系统中存在的旧库存日志记录计算的。所有记录都有一个在到货报告期间保存的价格。但是，对于采购订单，价格将在供应商发票链接到报告到货项目时更新。这意味着即使在创建最近库存价值列表后没有发生任何库存事务，FIFO值也可能发生变化。库存盘点和直接库存报告将以标准成本作为价值。其他事务——例如通过工单对物料报告负数——获得标准价格并影响先进先出。要计算 FIFO 时，首先检查组件的余额。然后程序将找到能够评估这些组件所需的、尽可能多的（正的）事务。然后将首先使用最近的事务。Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit.
I
-    
Intrastat
Intrastat is the system which gathers statistics relating to trade in products within the European Union.Gathering of Intrastat statistics is handled in the same way by all EU member states.
M
-    
Management accounting
Management accounting is an option in Monitor ERP.It is used as a complement to the standard function called Stock accounting.The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5.The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor.Calculation differences are posted and these can be followed up per product, per order, etc.This function also contains extended management of cost of goods sold.
-    
Monitor-to-Monitor (M2M)
Monitor-to-Monitor is designed to facilitate the communication between customers and suppliers using Monitor ERP and/or Monitor G4.该功能便于登记，例如采购订单、订单确认和发票。
O
-    
Overlap
Overlap is abbreviated to OL, and is entered as a percentage.This allows two operations to overlap in time when a manufacturing order is created.Overlap is entered as a value that indicates how much of the current operation should remain when the next operation can begin.Any queue time on the subsequent operation means that overlap is ignored.
P
-    
Packing list
A packing list describes in which packages and using which types of packaging, the parts/products have been packed for delivery.The packaging list often contains information about package number and gross as well as net weight.
-    
Pick list
A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order.
-    
Posting methods
Posting method is used to register how different types of transactions are posted to the correct accounts in the Stock or Management accounting.
Q
-    
Queue time
Queue time refers to time which is added to create a gap between two operations when the manufacturing order is created.It is normally stated in days, where 1 means the rest of the commenced day will be the "gap".2 means the rest of the commenced day plus 1 full day will be the gap.For work centers with hourly planning, the queue time is instead entered in hours.The entered queue time will be added before the operation which has a value entered.
S
-    
SC (Subcontracting cost)
外协成本加成是外协成本的百分比加成，以涵盖外协的所有成本。外协成本 + 外协成本加成一起描述了采购、运费、海关、处理和库存的成本。
-    
SO (Storage overhead)
仓储费用加成是物料成本的百分比加成，以涵盖物料的所有成本。物料成本 + 仓储费用加成一起描述了采购、运费、海关、处理和库存的成本。
-    
SRU
会计科目表中的所有科目都链接到SRU代码。（SRU 是瑞典语标准会计报表的缩写）该代码用于将信息从会计转移到纳税申报表中的会计计划。有关SRU编码的信息将导出到SIE文件中的会计科目表信息中。
-    
Stock accounting
Stock accounting is a standard feature in Monitor ERP.It is used to continuously post all stock transactions in the system.This way the stock value in the Stock module matches the recorded value in the Accounting module.Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement.
W
-    
WIP (Work in progress)
WIP 是“进行中的工作”的缩写。WIP 表示与生产相关的所有组件的价值，包括增加的工作和物料。
包
-    
包装类型
包装类型描述了使用包装的类型，例如欧盟托盘的“托盘”，纸板箱的“盒子”等。
操
-    
操作时间
条款“操作时间”表示工序需要生产一定数量的产品的负荷时间。这是在负荷计划或日程表中显示为“负荷”的时间。如果工作中心是自动化的，生产产品需要这个时间，但不需要那么多工时。通过使用人员因子，你可以重新计算设备和人员之间的负荷差异。
查
-    
查找
查找功能是一个强大的搜索工具，它允许您从大型寄存器中搜索和加载信息。您可通过单击下拉按钮或使用键盘上的 F4 打开查找功能。
超
-    
超链接
超链接是您可以单击的 HTML 元素。使用超链接，您可以链接/转到网站、Email 地址或文件。
-    
超量
超量是额外数量，例如设置机器时的浪费，在为特定组件创建 BOM 与工艺路线时应该可以考虑。
成
-    
成本要素
工作中心的成本要素用于在按标准计算中计算加工成本。
当
-    
当前余额
当前余额是当前库位上的组件余额。
订
-    
订单建议
Order suggestions are suggestions made for manufacturing or purchase orders generated by the system in order to cover stock shortages of manufactured parts as well as purchased parts.
费
-    
费用号
费用号用于提供可追溯性。它是供应商的批次号或费用号，与我们库位的批次相关联。
工
-    
工资类型
工资类型用于为工作时间和缺勤创建工资底单。Different salary types are used, for example, for work during regular working hours, flex, overtime, shorter working hours, and sick leave.The salary bases are used to manage salaries in a payroll system.Salary types are linked to absence codes in addition to work schedules and overtime schedules.
-    
工作中心
工作中心是工厂的一部分。它可以是单台机器或一组机器、单个工站或一组工站。
货
-    
货物类型
货物类型描述了它是什么类型的组件，如机器组件、电子产品等。此信息印在货运文件上。
基
-    
基础数据
对于“基础数据”，我们指的是数据库中的静态记录，例如组件、客户、用户、工作中心等。
计
-    
计划设置
组件寄存器中有许多不同的设置，例如再订购点和安全时间。这些设置在需求计算期间作为组件信息被使用。
记
-    
记账
记账是您向供应商支付或从客户那里收到的部分付款（预付款）。
价
-    
价差
差价 (PD) 的计算方法是采购价格减去采购组件的标准价格。对于外协，价差计算为外协的实际成本（供应商发票上的价格）减去外协的计划成本。
交
-    
交货日程表
Silf（瑞典采购与物流协会）对“交货计划”一词解释如下：交货日程表是从供应商到客户的交货计划/时间表。交货日程表由客户创建，通常包含 0.5-1 年的计划范围。通常，交货日程表数量会根据需求类型分配不同的状态。例如，在不久的将来（最接近的时间）输入的数量实际上是固定订单，这是很常见的。在固定订单之前的几个月内，输入的数量可能被视为预估订单，客户有义务对供应商购买的任何物料承担财务责任。输入的后续数量仅被视为预测。（翻译自来源 https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]）。交付日程表是一种提高透明度的方法，从而可以在供应链的多个步骤中相互掌控财务状况。这是通过传输有关即时需求/要求以及未来预测需求的信息来完成的。
-    
交期计算
登记工单时将计算工单的交期，前提是您已选择加载模式为使用交期计算。订单交期——使用开始和结束日期——决定了准备和物料需求的发生时间。
阶
-    
阶梯价格
Staggered price means the part has one price for one sales volume/purchase volume (quantity) and another price for another sales volume/purchase volume, etc.阶梯价格也被称为“价格梯”。
节
-    
节点
节点是组件结构中某个级别上包含/合并的生产件。结构组件中的一个级别可以包含多个节点。The node on the highest level is called the main part (order).
结
-    
结构订单
结构订单是指在一个工单中有多个组件作为一个批次，应该以某种结构生产。
净
-    
净需求计算
您可使用净需求计算执行基于累积客户订单的需求计划，以及任何现有的销售预测。
聚
-    
聚合
聚合是汇总或组合的数据，创建新数据。
可
-    
可用余额
可用余额是库位上的当前组件余额减去已预留数量。
-    
可支配余额
可支配余额是组件的当前库位余额在给定时间减去预定数量加上订购数量。
-    
可追溯性
Traceability in Monitor ERP is all about being able to trace a specific serial number or a batch in each step it is being processed, as of when a part or a material arrives with you from a supplier.Traceability is also about stating what is withdrawn from and what is added to stock, so it is then possible to trace from customer order, via manufacturing order to purchase order.但这也是关于能够以相反的方式追踪；从采购订单到工单再到客户订单。
快
-    
快速报告
快速报告意味着整个工单在一个步骤中报告为已完成，包括删除剩余数量（若有）。
宽
-    
宽限期
宽限期用于需求计划，以计算并重新调度哪些能够满足需求但时间太晚的订单，而不是建议新建订单。
利
-    
利润加成
利润加成是成本价格的百分比加成，它将产生建议的报价。
零
-    
零散供应商
您很少采购的供应商。因此，这些供应商不必在供应商登记程序中登记。如果选中了“零散供应商”设置，您可以填写订单上的所有字段。
-    
零散客户
仅偶尔采购的客户。"“零散客户”是用于一次性（非经常性）销售的不同客户的客户号。因此，这些客户不必在客户登记程序中登记。
毛
-    
毛利
毛利（CM）是标准价格和销售价格之间的差额。
-    
毛利率
毛利率(CR) 是毛利所代表的发票金额（销售价格）的一部分。毛利率以百分比形式输入。
批
-    
批次
批次是同时生产并由相同原始材料制成的一组组件/产品。
-    
批次号
批号是用于跟踪一组或一批组件的编号。采购的材料可以有一个批号，该批号应该能够追溯到供应商的某个费用号。
-    
批量规则
批量规则确定组件出现库存短缺时的建议订购数量。批量规则用于执行需求计划的组件。
缺
-    
缺勤代码
使用缺勤代码是为了能够将缺勤的原因与记录联系起来。工资类型可以链接到缺勤代码，从而系统可将不同类型的缺勤链接到正确的工资类型。一些最常见的缺勤原因包括生病、育儿假、请假、迟到等。此外，缺勤代码可以链接到时间余额，以便缺勤记录自动减少弹性时间、补偿或补课时间的余额。
日
-    
日常工时
日常工时是根据时间表每 24 小时约定的工作时间。
-    
日计划
当您不应用小时计划时使用日计划。这意味着所有工序都计划到某个日期，而不是某个日期的特定时间。
-    
日消耗量
日消耗量是特定组件每天的消耗量。
时
-    
时间单位
时间单位是用于指示 BOM 与工艺路线的准备和单位时间的单位。通常使用分或小时。
-    
时间银行
时间银行被用于节省预定工作时间之外的记录时间。例如，不同的时间银行用于补偿时间、补充时间、弹性时间（正/负）和更短的工作时间。
实
-    
实体
实体是生产或采购的单个组件，每个实体都有唯一的序列号。
无
-    
无效时间
无效时间是工序中必需、但不是直接生产的时间。
销
-    
销售费用
销售费用是生产成本的百分比加成，它描述了生产本身之外的间接费用。这些是管理成本和销售费用。生产成本 + 销售费用 = 成本价格（公司开始赚钱的极限）。
小
-    
小时计划
小时计划是指按小时计划每个工作中心的工作。小时计划是通过系统设置激活的。期间是随后输入的日期和时间。您可以按小时查看负荷情况。
形
-    
形式发票
形式发票是在货物出口过程中使用的一种海关文件。它用于显示有关出口（清关）价值的信息。形式发票也用于其他情况，例如在联系银行安排银行担保时比交付时间早得多。
序
-    
序列号
序列号是用于在实体级别跟踪组件的编号。
延
-    
延误
术语“延误”是指在计划完成期间未完成计划准备时间和单位时间报告的总和。
运
-    
运输时间
运输时间是将货物从发件人运输到收件人所需的工作日数。
周
-    
周期
周期是工序中的生产时间，不包括非生产时间。周期越短，生产率越高。
主
-    
主库位
以前称为“当前库位”。主库位是指具有组件最近到货日期的库存库位。如果您为库位应用优先级，则主库位是具有最高优先级（即最低编号）的库位。
-    
主组件
“主组件”是用于组件结构中顶部节点（最高级别）的组件的术语。
装
-    
装载长度
单位“装载长度”用于难以装载或包装的组件（例如不能装在托盘上）。您输入包装组在存放时占用空间的最长尺寸（以米为单位）。
