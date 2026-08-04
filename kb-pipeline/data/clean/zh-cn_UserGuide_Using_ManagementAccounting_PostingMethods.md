### 过账方式
在这里你查询有关如何登记不同日志的过账方法的示例和提示。
库存事务日志的过账方式
为了能够过账/记录所有库存事务，你必须登记库存事务日志的过账方法。这些过账方法处理流程的以下阶段（低于的第 1-8 项）：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc32.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc32.png)
该日志中已记录的值是： 余额变更×已选价格替代方案。
低于表格中，你查询如何根据上面的编号箭头创建库存事务过过账方法的例如。在此例如中，应用了标准价格的过账以及采购件的仓储费用加成。采购件的零件和生产件用于单独的库存科目。使用哪个库存科目取决于 组件类型。然而，可以使用其它字段来确定这组件。如果你有一个共享库存科目，已登记过账方法的编号实际上可以减少50%。然而，如果你由于仓库而拥有许多库存科目，你需要增加过账方法的编号。每仓库/库存科目应该有一流程。这可以通过使用仓库作为 其它条款 关于过账方法。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc35.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc35.png)
直接库存报告的过账方式
这种事务类型（上面的事项1项和第6项）与库存事务日志中的其它交易类型不同。对于此报告类型，你可以确定是否应从过账方式或报告时间输入的过账中加载过过账。工具的提取和退回报告也使用此过账方式进行处理（“工具和维护”是一种选项）。这是由会计标签页下的低于系统设置决定的：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc36.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc36.png)
如果你选择 过账矩阵，将会加载报告时间输入的过账。这是最共同的的方式。低于的设置（位于“库存”标签页下）也必须设置为 原因与过账 订单使其正常上班。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc20.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc20.png)
当上面设置已已配置过账，你默认在 过账矩阵 程序，在直接库存报告标签页下。请参阅以下章节阅读更多相关信息 [启动设置](Settings.htm)。
采购件标准成本计算组件的过账方式
在该字段 采购件备选价格，你可以选择如何过已编码采购件的费用。对于不同的过账方式，你可以选择是否将备选价格设置为 标准成本不含费用 要不就 费用。请注意！如果该组件否存在计算，系统将过账0值。因此，当使用这些备选价格时，采购件具有标准成本计算尤为重要。
生产件标准成本计算组件的过账方式
如果标准成本的计算组件已编码为在字段 生产件备选价格 （例如物料成本、加工成本），正在已编码的值是从组件的计算登记中加载的。请注意！如果该组件否存在计算，系统将过账0值。因此，当使用这些备选价格时，生产件的标准成本计算尤为重要。
在低于的系统设置中，在会计标签页下，你可以选择是否从中加载值 当前计算 或者 报告时的当前计算。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc37.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc37.png)
替代方案 当前的 如果在过账库存事务日志时出现性能问题，建议 过账日志 程序。
产品配置过账方式
如果你使用产品配置选项，则在过账事务类型时会已记录以下值 转移至成品库存 （4）以及 交货 - 客户订单 （7）： 余额变更×标准成本或已配置计算的计算组件。
当已配置一个订单（客户订单 / 工单）时，会已保存一个该订单特有的标准成本和计算。当使用产品配置时，将已记录此计算，而不是组件登记中的标准成本计算。
远程配置过账方式（销售公司）
如果你使用产品配置选项，则在过账事务类型时会已记录以下值 到货 - 采购订单 和 交货 - 客户订单 在销售公司： 余额变更x订单行已保存的标准成本。
仅备选价格“标准成本”才会从订单行发布标准成本，这就是为什么在这些事务中使用此备选价格很重要。在远程配置期间，订单行的计算未保存在销售公司中。仅已保存标准成本，计算本身仅已保存在生产公司中。
价格变更日志的过账方式
如果库存组件获得新建的标准价格，则该零件的全部余额将基于新建的标准成本。库存的更改必须在会计中作出已调整。因此，你必须为此目的登记编码方法（低于的事项9 项和第 10 项）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc38.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc38.png)
库存变更的已记录值通常是： （新建标准成本-前道标准成本）×库存余额
由于标准成本变更也可能影响WIP 价值，因此在会计中对WIP 价值进行了调整的（上面的第 11事项）。
在WIP 价值调整的已记录值一般为： （在WIP 余额- “至仓库”余额）×（新建标准成本-前道的标准成本）
低于表格中，你查询如何根据上面的编号箭头更新价格变更日志的过账方法的例如。在此例如中，应用了标准价格的过账以及采购件的仓储费用加成。采购件的零件和生产件用于单独的库存科目。在里面 组件类型 如果组件是采购件 的,生产件 的, 还是虚拟件 的,你在 字段选择.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc39.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc39.png)
标准成本变更WIP 的过账方式
除了“管理会计”选项附加，还必须已激活“库存”标签页下的低于设置，订单过已编码第 11事项。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc19.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc19.png)
工单日志的过账方式（管理会计）
此日志已记录了工单的加工成本和外协成本。这也应用至已报告的外协成本 报告外协成本 程序。这些过账方法处理流程的以下阶段（低于的第 12-13 项）：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc40.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc40.png)
上面事务类型加工成本（12）的已记录值报告的：
时间（准备时间+单位时间）×工作中心每小时成本
关于上面时间，你可以在 数量 字段选择以下备选：
- 已报告时间 – 当你选择此选项时，将根据操作的实际的已报告时间来已记录工作。当订单已报告为已完成时，五月出现有关工作的计算差异。然后将其已编码在单独的日志中以计算差异。
- 已报告数量的计划时间 – 当你选择此选项时，将根据已已报告数量的操作计划时间来已记录工作。在这种案件下，当订单已报告为已完成时，否发生有关工作的计算差异。
> 提示！ 你上面查询在 WIP 价值 程序。确保在对账期间两者地方使用相同的备选。
在里面 成本要素 字段，输入你使用的每小时成本。也就是说，哪些成本要素应该包含在应过已编码的值被用于。在 Monitor你查询最多三种可使用的不同成本要素。例如，这些可以分为直接工资费用、设备成本和制造费用。如果你想要分离这些成本（在制品科目的冲销科目），你必须为同一报告登记更多过账方法。这是通过在这些过账方法上使用相同的条款来实现的。然而， 允许副本 必须标记。你还应该为这些过账方法输入不同的成本要素和成本科目。
对于事务类型 加工，你还可以选择 价格类型。可用的选项包括 已报告 和 当前的。已报告 指报告时间应用的每小时成本。当前的 指工作中心当前的每小时成本。在这里你还应该确保在 WIP 价值 程序。
上面事务类型外协（13）的已记录值是以下备选一（在 数量 字段）：
- 报告成本 –实际外协成本将根据与外协采购已链接的发票上的发票价格已记录。对于未链接与发票相 关联 的供应商/工作中心,价格将从采购订单中连接到货报告已记录.
- 已报告数量的计划成本 –计划外协费用将根据采购订单上的价格与到货报告一起已记录。请注意以下事项 已计划准备成本：对于外协，整个已计划准备成本将在报告第一个数量连接已创建。
> 提示！ 你上面查询在 WIP 价值 程序。确保在对账期间两者地方使用相同的备选。
如果你还想评估包括外协成本加成外协成本，然后你还需要创建上述备选价格的复制，选择你一备选之一：
- 报告外协成本加成
- 已计划外协成本加成

#### 在发票被链接前的计划成本
此设置仅可用于 工单日志 和事务类型 外协。数量还必须设置为 报告成本 或者 报告外协成本加成。如果已激活此设置，系统将在到货时登记计划成本。当已链接供应商发票时，即当知道实际成本时，就可以已调整成本。
低于表格中，你查询如何根据上面的编号箭头创建工单日志过账方法的例如。在此例如中，工作成本和成本要素应用单独过账。外协成本根据报告成本（包括外协成本加成）已编码。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc41.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc41.png)
计算差异的过账方式（管理会计）
当工单最终已报告（接收状态9）时，已记录计算差异 关闭工单 生产模块中 的程序.这些过账方法处理流程的以下阶段（低于的第 14事项）：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc42.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc42.png)
计算差异是指制造一组件的已计划成本（预先计算）与已报告成本（按实际计算的）在中间的差异。这些在中间的差异已记录在 WIP科目中，并用冲销科目计算差异。有两种不同的方法来记录这些计算差异：
- 合计计算差异 – 通过使用此替代方案，将仅已记录订单的合计计算差异。否每计算组件进行单独计算。此种计算差异的方法仅基于当前订单的 WIP科目上的过账。当订单最终已报告时，在 WIP科目上的全部过账都会被总计。将在 WIP科目和计算差异科目上已创建登记，这使得订单上的WIP 价值0。
- 单独计算差异 – 通过使用此替代方法，你将看到每计算组件（物料、工作、外协等）的单独计算差异。这里你必须创建多个编码方法，每计算组件一。你还必须检查复选框 允许副本。计算差异是通过计算订单每计算组件的已报告值，并将其与标准成本计算（预先计算的标准成本）中的相应值进行比较来确定的。
对于计算差异日志，如果为借项和贷项已选择了错误的科目类型，你会在过账框中看到警告。
低于表格中你查询两个如何更新计算差异的过账方法的示例。在第一个例如中，仅已记录每订单的合计计算差异。在第二个例如中，已记录了单独计算差异。加工成本以每成本要素的计算差异来显示。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc43.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc43.png)
阅读更多本章节以了解有关计算差异的更多信息 [订单的关闭工单和计算差异。](OtherThingsToConsider.htm#Slutrapportering_av_tillverkningsorder_och_kalkyldifferenser)
未开票日志过账方式（管理会计）
当客户发票被已批准时，发票日志会被已记录 复审 / 批准发票 程序。这些事务也可以在常规的开票日记账中已编码。但是，通过使用管理会计，可以使用多个条款来确定过过账。销货成本 （销货成本）也可以每计算组件分开已记录。这些过账方法处理流程的以下阶段（低于的第 15事项）：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc44.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc44.png)
在销货成本期间，已记录所售商品的预先计算的生产成本（标准成本）。如果你使用管理会计过账销货成本 ，则可以详细进行（每计算组件分开）。销货成本通常已编码入成本科目，并通过冲销科目预留科目交货。
对于事务类型销货成本，你还可以选择价格类型。你可以选择以下备选一 交货价格 和 开具发票时的价格。交货价格 建议确保在开票和交货时已记录相同的值。
低于表格中你查询两个如何更新销货成本过账方法的示例。在第一个例如中，仅已记录了合计销货成本。在第二个例如中，每计算组件都已记录了单独的销货成本 。加工成本也每成本要素与销货成本分开：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc45.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc45.png)
你还可以在此日志中记录收入。这是为了应对特别案件。例如，当你想以比过账矩阵更多高级选项的方式确定收入过账时。
产品配置
当你安装了选项产品配置时，应为销货成本已编码的值将从已配置部件的标准成本/计算中加载。当已配置一个客户订单时，该订单特有的标准成本和计算将被已保存。
远程配置（销售公司）
当使用产品配置选项时，事务类型销货成本的已编码账值将从销售公司中客户订单行的已配置标准成本中加载。当远程已配置订单时，会为该订单行已保存唯一的标准成本（虽然否已保存计算，因为这仅已保存在生产公司中）。
仅备选价格“标准成本”才会从订单行发布标准成本，这就是为什么在这些事务中使用此备选价格很重要。
