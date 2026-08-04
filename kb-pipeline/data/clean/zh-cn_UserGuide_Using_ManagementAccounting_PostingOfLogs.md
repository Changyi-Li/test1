### 过账日志
在里面 过账日志 程序，你过账应通过库存科目和管理会计已记录的事务。还可以自动过账和记录会计中的事务（使用日程计划）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc48.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc48.png)
手工过账
当你开始使用库存科目或管理会计时，周三建议你人工的运行过账。这是在程序顶部的框中进行的。第一个你时间，你自日期在 过账起始时间 每个日志的列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc49.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc49.png)
点击 运行 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 按钮订单执行过账。
过账后会出现一条消息。过账结果在​ 打印日志日记帐 程序。你还过账检查 搜索管理会计 程序。这是通过选择替代方案来实现的 未审批日记账 位于选择标签页的底部。
当你已批准并将第一个日记账已传输到会计， 过账起始时间 字段将被未激活。系统会自动识别过账的时间。这样做是为了查询全部不已记录的事务，仓储费用可以已编码它们。
当你运行某个日期的日志时，你必须检查上个月的日记帐中是否已添加了你。请注意！这些必须得到已批准，无需集成。
无效过账
在过账中，有些事务可能不过账。当无法已编码事务时，会出现一条消息。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc50.png)
这些事务的列表可以已打印在 打印日志日记帐 程序，在“警告”标签页下。你可能需要调整/新建的过账方法来修复错误。例如，当为组件基础数据包含错误的产品组、组件代码等时，就会出现这种案件。然后，你必须调整错误并运行新建的过账日志以查看结果是否OK。阅读更多内容 [警告](PrintLogJournal.htm#Fliken_Varningar) 在打印日志日记帐章节。
日程计划
可以进行以下日程计划：
- 过账日志
- 审批日志日记账（传输至会计）
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc51.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc51.png)
过账日志
你可以配置库存科目和管理会计中全部日志的自动过账。这是在 日程计划 盒子。检查复选框 激活的 在行 过账日志。在右边的框里 过账日志，你输入是否应在给定时间过账 日程表 或在某些 时间间隔。
> 请注意！ 为了避免服务器超载，周三建议你未运行多于必要的过账日志。如果公司有很多事务的话，这一点就尤其重要。
审批日志日记账
当日志已编码时 ,日记帐必须 得到已批准,订单事务能够已记录在会计中 .你可以按照与过账日志相同的方式日程表日志日记帐的审批。这意味着你不使用 打印日志日记帐 程序。事务将被已记录在会计中，而无需打印中日记账。检查复选框 激活的 在行 审批日志日记账。在里面 审批日志日记账 框到右边，你日记账是否应在给定时间通过输入方式已批准 日程表 或在某些 时间间隔。
> 提示！ 请注意！将连接每个已排程的批准已创建每日志一凭证。不你每个有太多的凭证 ，日程计划就不设得太频繁。
日志情况不自动批准日记帐：
- 无效过账（事务不存在过账方法）
- 属于已关闭或已锁定的会计期间或凭证号序列的事务。
- 包含错误的/已冻结科目、维度的过账
通知和日志
你可以激活日程计划的日志。这样，你时间就可以视图历史日程计划并查看统计。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc52.png)
你还可以激活日程计划通知。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc53.png)
然后，如果例如无法已编码的事务，系统可以向已选用户/角色/组发送消息。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc50.png)
这些通知也可以在 Monitor ERP。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ManagementAcc54.png)
