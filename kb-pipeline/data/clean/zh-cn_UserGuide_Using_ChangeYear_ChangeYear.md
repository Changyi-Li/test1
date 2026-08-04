## 更改年度
看着 关于更改年 Monitor ERP 视频：
| 瑞典语 | 英语 |
|---|---|
|   |   |
“更改年度”（变更为新建的会计年度）是公司在你新建的财务年时需要做的事情，在公司使用 会计 模块 Monitor ERP。会计年度的更改应该在应付账款、应收账款以及新建年的会计中你登记之前进行。
你使用以下程序 更改期间 / 会计年度 更改年度和程序 期初余额 将期初余额(期初余额 )载入到新建年。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ChangeYearProcedures.png)
> 请注意！在开始你更改年度之前，请确保你拥有当前可用的MONITOR数据库备份！
变更为新建的会计年度
按照此指导更改会计年度：
1. 打开调用的程序 更改期间 / 会计年度。确保所讨论的期间是会计年度的最后期间。图片中， 十二月是当期会计期间（期间12）。黑色箭头表示 当前的 当期会计期间所在行下一个的列。
2. 点击按钮 更改年度 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_calendar_next.png) 然后点击 OK （当当前期间是会计年度的最后一个期间激活时间）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ChangeAccountingYear.png)](../../../../Resources/Images/TrainingMaterial/ChangeAccountingYear.png)
3.    
然后你输入新当前会计年度。默认下已建议下一个日历年。点击 OK 使系统生成新建的会计年度。
> 请注意！生成新建的会计年度可能需要分钟，并且可能看起来好像程序不响应。你必须等待程序已完成新建会计年度的生成。底部不关闭该程序！
变更为新建会计年度之后
当你已变更年时，你应该检查：
- 新建的期间分配是正确的。重新打开 更改期间 / 会计年度 程序并确保 1-3 个期间可以打开会计。
- 损益表已重置，新建年的资产负债表仅包含预估期初余额。你检查在 打印财务报告 程序。
- 检查年度财务对账单中的损益表和资产资产负债表是否正确。
与会计集成
如果公司使用应付账款/应收账款和会计在中间的集成，请重要记住，在你你新建的会计年度之前，不能已打印和重置属于新建会计年度会计年度的日记帐。当你使用会计集成而不打印中日记账时这也适用。
> 请注意！凭证号序列链接至日记账，集成设置为 直接每发票，将保持下去，不重启编号序列。对于这些凭证号序列，字段 后续凭证号 未激活。当你已变更至新建的会计年度之后，其它凭证号序列将开始从 1 开始。
在国库署和新建会计年度并行上班
你新建的会计年度已创建，你可以后退AFS（前道一个会计年度）来添加事务并完成财务对账单。在里面 会计年度 在桌面后台的章节，你可以更改上班的会计年度。然后更改适用于全部程序。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ChangeAccountingYearBackstage.png)](../../../../Resources/Images/TrainingMaterial/ChangeAccountingYearBackstage.png)
如果你在会计年度在中间班次，这将仅应用于相关的登录用户。因此，不同的用户可以并行在不同的会计年度上班。
你还可以在某些程序中临时班次会计年度，只需点击按钮 更改会计年度 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_calendar.png) 在程序的 工具栏 上 。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ChangeAccountingYearProcedure.png)](../../../../Resources/Images/TrainingMaterial/ChangeAccountingYearProcedure.png)
如果你在某个程序中在会计年度在中间班次，则它将仅应用于该特定程序和时间的情况。如果你关闭该程序并再次打开，你将自动进入当期会计年（新建会计年度）。
年末结账已完成时载入期初余额
当 AFT 中的年末结账工作已完成（通常是当年度财务对账单凭证已加载到 AFS 中时），将明确将期初余额（期初余额 ）负荷到新建的会计年度。请遵循以下指导：
1. 确保你在当期会计年（新建会计年度）工作。
2. 打开 期初余额。
3. 要载入全部期初余额，你单击按钮 自上一年的期末余额载入期初余额![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_databaseImport.png)。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ChangeYearLoadOB.png)](../../../../Resources/Images/TrainingMaterial/ChangeYearLoadOB.png)
请注意！你可以根据你时间载入期初余额 。
> 请注意！完成全部对账后，请记住关闭AFS 中的最后一个期间（前道会计年度）！
在新建的会计年度开始时记录年的结果
请注意！AFS（前道会计年度）中已记录的结果必须人工的已记录在当期会计年（新建会计年度）。
会计程序与​ Monitor ERP
差异会计程序在中间 Monitor ERP，并且你认为年度财务报表是完成的，最共同的原因是不全部的年度财务对账单凭证都已加载到 Monitor ERP。
