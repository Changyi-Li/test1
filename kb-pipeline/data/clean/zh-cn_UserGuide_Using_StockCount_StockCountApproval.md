### 库存盘点批准
你可以配置在库存盘点值在一定范围内和/或一定范围内案件使用库存盘点批准 余额百分比。这应用至值高于和值低于。库存盘点值是基于零件的标准成本乘以库存盘点差异得出的。
> 请注意，目前，库存库存盘点批准仅应用下班在 库存盘点列表 程序。下班在 库存盘点 目前否支持需审批。

#### 通用审核设置
订单批准库存盘点，设置在 盘点 - 批准 标签页卡中的 通用审核设置 程序。你可以在此处添加能够批准库存盘点的审核人 / 批准者。你添加的每个审核人 / 批准者都链接至一个用户。你还必须为审核人 / 批准者设置一个值范围 - 也就是说，从/到将触发器审批的库存盘点值。你还可以输入 余额百分比 这触发器需要获得批准。审核人 / 批准者可以结合使用金额间隔和百分比。在这种案件下，库存盘点批准将由第一个满足的条件触发由。通过此设置，你可以决定通知审核人 / 批准者是否消息在 任务 当有库存盘点需要批准时。
> 如果你两者输入了值间隔和余额百分比，则当库存盘点差异超出这两个限制时，就需要获得批准。
你还可以为审核人 / 批准者配置组件条件。你可以为组件号、组件代码、产品组或ABC 代码（或这些的组合）设置间隔。当库存盘点值属于这些条件一所指定的范围案件，已选择的审核人 / 批准者必须批准该库存盘点。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/StockCountApproval1.png)

#### 报告仓库盘点
当用户报告库存盘点时 库存盘点列表 程序，并保存， 状态 列表示库存盘点是否已已报告或必须首先获得已批准。
对于不批准的已报告库存盘点，将已创建库存事务并照常是已更新余额。在绿色案件下， ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) 我 状态 列。对于必须一次已批准的已报告库存盘点，否已创建库存事务，也否是已更新余额。在这种案件下，以下符号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusOpStarted.png) 出现在 状态 列。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/StockCountApproval2.png)

#### 库存盘点差异
待已批准的库存数量已报告由审批人/审核人使用列表类型加载 库存盘点批准， 在里面 库存盘点差异 程序。
在里面 库存盘点批准 你可以选择的列表类型 批准 或者 拒收 用于报告。列表还 显示 了库存盘点底单,库存已盘点数量,库存盘点差异,报告余额,标准成本和价值变更的细节.
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/StockCountApproval3.png)
如果审核人 / 批准者选择 批准，并保存，将进行库存事务以进行库存盘点，并且余额将被已更新。如果审核人 / 批准者选择 拒收并保存，将为该组件已创建库存盘点请求并显示在 库存盘点 在里面 库存 标签页卡中的 组件登记。
> 请注意，具有角色的用户 ERP 经理 或者 系统管理员 总是可以选择批准，而不是审核人 / 批准者 库存盘点差异 程序，例如，如果该员工时间不可用。用户可以在设置下选择自己作为审核人 / 批准者 选择 标签页。 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/StockCountApproval5.png)

#### 组件登记
未批准的库存库存盘点报告的库存盘点请求显示在 组件登记，其中包含已创建请求的时间和日期。评论表明库存盘点不获得已批准，必须对该组件一次盘点。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/StockCountApproval4.png)
