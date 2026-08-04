### 开票

#### 直接登记发票
当你想要直接向客户发票而又没有基础客户订单时，你使用此程序。你可以为借项发票创建发票底单。在此程序中可以已批准和已打印发票底单。另一种方法是批准并打印 复审 / 批准发票 程序。当你需要向客户贷项案件，此程序还可用来贷项发票。还可以修改现有的发票底单并删除发票基础。
发票上的行类型与客户订单上的行类型相同。你可以在主题中查询行类型的描述 [行标签页](../../../Sales/Orders/RegisterCustomerOrder/tRows.htm) 在线帮助功能 登记客户订单 程序。
创建借项发票：
1. 选择要向哪个客户开具发票并选择/输入其它信息。
2. 添加组件行并输入行信息。
3. 当你在程序中保存时，就会已创建发票底单。
4. 之后，你可以点击按钮直接批准发票 批准发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_approve_document.png) 在工具栏上。然后系统会询问你是否你打印发票或时间打印。你也可以跳过此程序中批准发票的步骤，而是选择批准发票底单并在 复审 / 批准发票 程序。
创建贷项发票：
1.    
For a new invoice you mark the Credit checkbox and in the field Crediting of invoice number (which will then become available) you select the debit invoice to credit.When you have selected an invoice number a dialog box appears.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingAccountsReceivable2.png)](../../../../Resources/Images/TrainingMaterial/InvoicingAccountsReceivable2.png)
> 如果你通过系统设置已选择了贷项发票的默认付款期限，则该付款期限将自动已变更。
2.     
In the dialog box you can choose or select the order number* the credit invoice will have.With Include you select which rows to credit.If no other settings are configured, the credit will be created for the full invoice row.If you want to create a price credit, select Price crediting on the row and enter New price.If the invoice row has a setup price, you can also choose for this to be credited in conjunction with the price crediting.During price crediting a minus row with the initial price will automatically be created, and also a new row with the new price.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/Credit_invoice_window.png)](../../../../Resources/Images/TrainingMaterial/Credit_invoice_window.png)
> * It is convenient to use the same order number on the credit invoice as on the debit invoice and just add the prefix "C".In the invoicing log and accounts receivable you can then search for the order number to find all debit and credit invoices that are invoiced with this order number.
3. 当你点击 OK 在对话框中，已保存贷项发票，并在程序中输入贷项发票的其它信息。
> Please note!When a credit invoice is loaded in the procedure you see the procedure name and invoice number in red text in the title bar.
修改现有的发票底单：
1. 选择订单号并载入发票底单。
2. 修改发票底单的信息。
3. 按程序保存。
> 还可以修改发票底单 复审 / 批准发票 程序。使用 编辑发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) 按钮打开所选发票底单的编辑窗口。
取消发票：
只要发票不获得已批准（状态为 8），你就可以删除/取消发票底单。如果已为发票底单已创建了形式发票，你必须开始使用按钮删除形式发票 删除形式发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_delete.png) 在其它框中，之前你删除/取消发票底单。
1. 选择订单号并载入发票底单。
2. 点击 删除 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_delete.png) （Ctrl + F6）在程序的工具栏中。
3.    
你按钮时，你会得到两个有关删除的选项：
1. 取消发票底单而不影响余额 – 如果它是以发票底单为基础的客户订单报告交货行，然后交货将不被撤销。如果发票底单来自客户订单的开票计划，则此选项不可用。
2. 取消和撤销发货报告 –交货报告也被取消。
如果发票底单已获已批准（已创建发票时），但发票未付款，则你按照以下程序取消发票 更新应收账款分类账。如果发票已经已登记了收款，则在已删除该付款之前不删除/取消。这是在 收款 程序。
> 已删除的发票底单不显示在系统中，但可以被用于在程序的列表中 发票底单 - 销售 通过在选择中包含状态0。
> 如果你在系统设置中调用 在订单报告期间检查开账期 已已选择 冻结 或者，如果日期属于已关闭的会计案件，则删除/取消发票底单时将不撤销交货。

#### 发票底单 - 销售
在此程序中，你可以看到已已交货但未未开票的货物。你还可以在库存估值中按标准成本值。该程序还可以显示已删除/已取消的发票底单。

#### 复审 / 批准发票
在客户订单已报告在 报告交货 程序, 有就绪好 待已批准未开票的 发票底单.开票按此程序处理。你在这里复核并批准发票底单并打印发票。在发票底单获得已批准之前，可以编辑该基础上的某些信息。你变更通过点击 编辑发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) 功能菜单中的按钮。在批准发票底单的连接，已创建发票并获得发票号。在应收账款中生成记录，并在客户开票日记账中生成过过账。
在此程序中，你复核并批准利息发票、内部的发票和现金收据。利息发票的发票底单已创建通过 利息费用底单 程序。
1. 标记 包括 在里面 结果 填写需要已批准的发票底单。
2. 点击按钮 批准发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_approve_document.png) 在工具栏上。
3. 批准之后，会出现一个问题询问你是否要打印发票。然后你将自动链接至程序 打印发票 已加载已批准发票。你还可以选择仅批准发票，以便在该程序的稍后时间打印它们。

#### 打印发票
在此程序中，你打印已批准的发票 复审 / 批准发票 程序。你可以选择自动打开 打印发票 发票被已批准之后。
你还可以在此处打印已已打印的旧的发票，方法是设置名为 重印。

#### 打印客户开票日记账
在此程序中，你打印并批准客户开票日记账。它包含已批准发票的过账。也可以不打印中而批准日记账。当你批准日记账时，会计便会已更新。你还可以在此处创建客户开票日记账的重印。
当使用客户发票直接集成到会计中时，此步骤不包含在工作流程中。
> MONITOR提示！ 使用 Monitor - to - Monitor 通过Email以PDF文件和 XML文件形式发送发票。XML文件的接收者的然后可以使用它来登记他们的 Monitor ERP 系统。该文件可以已导入到 Monitor ERP 直接从Email中消息。 使用 发票日志 视图每客户、组件、期间等的销售统计。 使用 复审 / 批准形式发票 在实际的开票之前打印形式发票。在国际的交货中，必须随货物附上形式发票，以方便海关申报。 使用 更新应收账款分类账 直接 将未付款记录输入应收账款, 无需开票或订单更改到期日/付款条款.你还可以在此处取消发票，只要该发票否已登记收款。如果有发票的收款，你第一个收款在 收款 程序。
