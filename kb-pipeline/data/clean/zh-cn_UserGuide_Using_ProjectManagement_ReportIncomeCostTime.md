### 报告并跟进收入、成本和时间

#### 收入
这 计划的 / 订单的 项目收入是 在客户订单行中过账 的, 标明 相关项目号, 并且 将科目标记 到 与收入相关 的成本类型/收入类型.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ProjectCustomerOrderRow.png)](../../../../Resources/Images/TrainingMaterial/ProjectCustomerOrderRow.png)
结果 指已入账会计的销售收入（项目内）。关于收入的实际的结果从过账总账中加载，用于与上面成本类型/收入类型链接至的科目。
预期结果 收入来自与已链接的客户订单相关的左边交付/发票的剩余值加上实际的结果。

#### 自工单成本
工单的成本分为三种固定成本类型 物料 - 工单， 外协 - 工单， 和 工作 - 工单。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ProjectCostsManufacturingOrder.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsManufacturingOrder.png)
全部项目将默认从此处读取成本，但可以在程序中为此创建例外 基本数据表 - 项目。例外是每项目类型已创建的。例如，如果你希望查看会计中的外协科目而不是工单的外协成本结果，就可以这样做。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ProjectCostsSubcontract.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsSubcontract.png)
然后，重要的是为外协登记一个单独的成本类型，你其链接到会计科目表中的外协科目。复选框 载入外协费用 然后必须取消选中上面，否则成本将翻倍。
项目的生产成本通过与相关项目号链接至的工单吸收。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ProjectManufacturingOrderRow.png)](../../../../Resources/Images/TrainingMaterial/ProjectManufacturingOrderRow.png)
物料、分包和工作订单的计划成本已记录为 计划的 / 订单的 在项目中 。已报告的成本已记录为 结果 与你报告订单时连接。已已报告的金额 +工单上剩余的金额合计将已记录为 预期结果 在项目中 。
对于成本类型 物料 - 工单 你可以在组件层级创建例外，确定或不应该从工单中进行读取。如果项目直接采购件了物料，并且你希望通过供应商发票/会计来吸收这些成本，你在组件登记中激活设置 项目采购。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/PurchaseToProjectPart.png)](../../../../Resources/Images/TrainingMaterial/PurchaseToProjectPart.png)

#### 从客户订单成本
当你需要吸收项目中既不在工单上也未在项目中采购件的物料成本时，自客户订单中载入物料成本可能会很有用。订单进行这种类型的读取，需要该组件 不 在项目上采购件，即已未激活上面设置 项目采购并且项目类型具有设置 载入物料成本 从客户订单已激活。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ProjectCostsMaterialCustomerOrder.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsMaterialCustomerOrder.png)
> 如果你正在过账项目的销货成本（销货成本 ），你应该 不 使用上面提到的设置从客户订单载入物料成本，因为该物料成本然后翻倍。

#### 其它成本类型
项目的其它成本类型包括外部的工作、差旅、直接物料采购、员工时间报告等。这些是在标签页下定义的 成本 / 收入 在程序中 基本数据表 - 项目 并且属于以下类型 成本。
结果 其它成本类型通过以下方式吸收：
- 成本已记录在会计科目表中与任何其它“免费”成本类型相链接的科目中。
- 成本已报告于 直接项目报告 程序。
- 你报告活动的报告时间，其中活动已链接至成本类型，并且已在程序中为成本类型输入了每小时成本 基本数据表 - 项目。
计划的 / 订单的 对于其它成本类型，则取决于列中成本类型的设置方式 计划加载自 在程序中 基本数据表 - 项目。例如，你可以吸收以下记录：
- 项目的采购订单，其中订单行上的科目与其它成本类型相链接。
- 活动的计划成本。要求在项目活动中输入已计划小时，并且活动本身与成本类型相链接。
预期结果 对于其它成本类型，则取决于列中的设置方式 预期结果载入从 在程序中 基本数据表 - 项目。

#### 已使用时间
已报告时间可以从以下位置已添加到项目中：
- 工单上的已报告时间。
- 已报告时间 直接项目报告 程序。
- 通过项目活动报告来已报告时间。
