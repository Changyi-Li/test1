### 导出 / 导入
在此程序中，你可以导出和导入会计数据。
In Sweden this takes place using SIE files (types 4E and 4I).Where SIE-type 4E – Transactions contains complete information on the chart of accounts, balances and voucher records.This file format can be used to export the journal postings for the year to a program for transaction analysis.SIE-type 4I – Transactions only contain voucher records.The file format is used when a preliminary system, for example, a payroll or invoicing program, is to generate an accounting order to be loaded into the accounting program.
程序工序可用的字段已选择在 类型 字段。
会计数据是例如凭证、余额、期初余额、会计科目表、预算和预测。
对于 SIE导出，默认程序已配置在 导出 / 导入设置 程序。
SAF-T（标准审计文件-税）的导出是用于以 XML格式导出不同类型簿记事务的标准格式，并且可作为一种选项。
程序中的工作流程
第一个，你应该确保你在正确的会计年度内工作。然后你要执行的工序： 导出 或者 导入。然后，你可以为导出或导入配置不同的设置。你可以使用按钮执行导出或导入 导出 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_export.png) 或者 导入 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_import.png) 在程序的工具栏上。输入正确的文件路径/文件名称激活时间。当你进行导入时， 导入规则 打开窗口，你可以在其中决定如何将不同的项目已导入系统。你步骤已完成点击之后 导入，会显示一个对话框，显示导入的结果。
导入规则窗口
When you make an import, the Import rules window opens for you to have the chance to decide how different items should be imported to the system.The system tries to match voucher series and dimensions.If the system does not succeed, you can do this manually.
凭证号序列
The upper box is only used if you have chosen to import vouchers.In the box you see/enter links between voucher number series in the file and voucher number series in the system.You can also see/enter how many vouchers exist in the file per voucher number series.If the same series exist in the file as in the system, this will be suggested.In case voucher number series are completely missing in the import file then you must always do the linking manually.
对于文件中的每个序列，以下选项都存在于 导入 列：
- Yes, voucher no. from file (default) – if voucher number for the series in question exists in the file, that voucher number will be created at the import.This option might mean that the import at a later stage will cause messages saying the import failed because the voucher number already exists in the system.
- Yes, voucher no. from file, skip voucher when a clash occurs – if voucher number for the series in question exists in the file, that voucher number will be created at the import.This option might mean that the import will skip vouchers which are already recorded in the system.This option can be useful if you continuously import SIE files where each import also contains vouchers already imported.In those cases only new vouchers added since the previous import will become imported.
- Yes, next available voucher no. – This option (and the No option) are the only options you can select if the file does not contain any voucher numbers.Even though the file contains voucher numbers you can still choose to take the voucher number from the next available voucher number in the system instead.The latter might be useful if you for example obtain an SIE file with closing record vouchers from the accountant where he/she has used the same series and voucher number which have already been used.Then this option can be used to import the vouchers, as an alternatives to entering them in a separate voucher number series.
- 否 – 此选项意味着你完全跳过导入相关编号序列的凭证。
It is allowed to enter the same voucher number series on several rows.But during the import you risk receiving an error message about the voucher number clashing.To the far right in the box there is a column containing a button which you can use to display errors/warnings per voucher number series.There might be more than one error/warning within the same series if:
- 期间已关闭（警告）
- 该期间已已锁定（错误）
- 凭证序列已已锁定（错误）
- 有属于另一个会计年度的凭证（错误）
- 同一凭证号出现多个（时间）
Warnings/errors recognize what you have entered in the Import column.If you choose the No option all warnings/errors, if any, will disappear.If you change from Yes, voucher no. from file to any of the other options, the warnings/errors will take this into consideration.
维度
The system recognizes which dimensions exist in the file.These are displayed and are automatically matched against the dimensions existing in the system.If the dimensions do not become matched, you must do this manually.In the Import column you can determine if the dimension should be imported.This will then also apply to transactions/balances/budgets for the dimension in question.In the Create missing code column you can choose if the system automatically should create dimensions that are missing in the system.The dimensions will in that case be registered in the Dimensions procedure.If you choose not to create the dimension, imported transactions with this dimension code in the import file will be created without having a dimension code in Monitor.
> 通过使用 暂估凭证 列表类型 凭证列表 程序，你可以轻松查看全部暂估凭证。
