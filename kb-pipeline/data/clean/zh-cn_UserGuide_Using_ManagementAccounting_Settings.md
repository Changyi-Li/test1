### 启动设置
在开始你库存科目和/或管理会计之前，你必须在系统中配置一些设置。
> 请注意！全部启动设置和过账方法都应与顾问一起已配置。

#### 凭证号序列 / 日记账
在此程序中，你登记凭证与库存科目相关的日记帐的凭证凭证号序列编号序列，即 库存事务日记账 和 价格变更日记账。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc14.png)
如果使用“管理会计”选项，你还必须登记凭证编号序列 工单日记账， 计算差异日记账，也可能用于 开票日记账 （如果使用过账方式记录销货成本 ，与非在常规的客户开票日记账中已记录）。
> 请注意！在下方的框中你链接凭证号序列每个输入 是的 如同集成下的设置。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc15.png)
在上面的例如中，使用了管理会计，但销货成本已记录在销售模块中的常规的客户开票日记账中。
> 请注意！直接库存报告日记账应 不 如果你使用库存科目过账库存事务，则可以使用。应设置为 否 在“集成”列中。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc16.png)

#### 系统设置
还有编号针对库存科目和管理会计的系统设置。你可以在标题下查询这些设置 管理会计， 在下面 会计 标签页卡中的 系统设置 程序。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc17.png)
阅读更多主题中有关每个系统设置的更多信息 [管理会计](../../../GeneralRegisters/BasicSettings/SystemSettings/bManagementAccounting.htm) 在线帮助功能 系统设置。
在下面 采购 在标签页，你查询一些有关在最终记录与采购订单链接至的供应商发票时过账价格差异的系统设置：
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc18.png)
激活价差过过账并输入备选价格。推荐的选项是 到货标准成本。
阅读更多主题中有关每个系统设置的更多信息 [管理会计](../../../GeneralRegisters/BasicSettings/SystemSettings/bAccountsPayable.htm) 在线帮助功能 系统程序设置。
在下面 库存 标签页你需要复核以下系统设置：
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc19.png)
上面系统设置适用于使用“管理会计”选项的情况。通常情况下，应将其设置为 已开始。
在主题中了解有关上面系统设置的阅读更多 [组件](../../../GeneralRegisters/BasicSettings/SystemSettings/bPart.htm) 在线帮助功能中有关系统设置程序的信息。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc20.png)
上面系统设置应设置为 原因与过账 是否能够输入与直接库存报告报告连接的过账。
做 不 如果你已已配置系统设置配置为，请使用直接库存报告日记账 原因与过账。
在主题中了解有关上面系统设置的阅读更多 [直接库存报告](../../../GeneralRegisters/BasicSettings/SystemSettings/bDirectStockReporting.htm) 在线帮助功能中有关系统设置程序的信息。
在下面 销售 标签页你需要复核以下系统设置：
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc21.png)
顶部系统设置通常应设置为 是的。但是，如果你使用“管理会计”选项并通过此选项记录销货成本 ，然后此系统设置应设置为否，否则销货成本将被已记录两次。你可以选择用于计算P 部件和 M 部件的销货成本的备选价格。建议的备选价格是 交货时标准成本。
在主题中了解有关上面系统设置的阅读更多 [开票](../../../GeneralRegisters/BasicSettings/SystemSettings/bInvoicing.htm) 在线帮助功能中有关系统设置程序的信息。

#### 过账矩阵
在里面 过账矩阵 在程序中，你输入与开票时过过账销货成本相关的科目。这是在销售科目标签页下输入的。系统设置 在开票时记录已售货物物料成本 必须被已激活。作为科目 物料，通常使用销货成本成本科目。作为科目 库存，通常输入交货预留科目（此科目在交货记入借方，在开票时记入贷项）。应为涉及库存已更新并已交货给客户的商品的产品组输入这些科目。如果使用管理会计选项，并且销货成本已记录在那里，然后低于的科目不在这里输入，但可以在程序中输入 登记过账方式 反而。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc22.png)
在此程序中，你还可输入与链接供应商发票时价格差异过过账有关的科目。这是在“采购科目”标签页下输入的。系统设置 在登记发票时记录价差 必须被已激活。作为科目 采购，通常会输入到货预留科目（此科目在到货时记入贷项，在发票登记时记入借方）。作为科目 价差，通常会输入价格差异的成本科目。应该为与库存已更新和从供应商采购件的物料相关的产品组输入这些科目。
应为涉及外协的产品组已配置价差科目，案件你记录 已计划 WIP 中的外协成本。在过账的已报告外协成本时，仅应已记录与采购货物相关的产品组的价差。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc23.png)
你还可以在此处输入有关直接库存报告过账的科目。系统设置 在直接库存报告程序中使用原因/过账 必须设置为 原因与过账。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc24.png)

#### 会计科目表
在图表科目程序，你应该标记 订单号 对于系统也应该在总账中过账订单号的科目，例如应该已对账的结算科目。对于你希望系统在总账凭证行中过账附加细节（例如组件号）的科目，应该已激活规格。
