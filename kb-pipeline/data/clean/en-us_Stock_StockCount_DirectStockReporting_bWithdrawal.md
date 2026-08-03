### Withdrawal
In this box you report direct withdrawals.

#### Part number
You can add rows and select for which part withdrawals will be made

#### Current total balance
Here you can see the current balance of the part. It is a total of the balances on all locations.

#### Unit
Here you can select the unit in which the reporting should be made. The current stock balance will also be displayed in this unit. The unit shown as default is the unit selected in the Part register to apply for stock count/stock reporting for the part in question.

#### Comment
Here you can enter a comment regarding the withdrawal. Mandatory comments can be configured to apply when entering certain cause codes. For such codes a comment must always be entered.

#### Location
In this column you see the name of the location. You can only use already existing locations when making withdrawals. The name cannot be edited. If the part has multiple stock locations, these are shown on separate rows from which you can make withdrawals.

#### Balance
In this column you see the current balance of the location.

#### Quantity
Here you enter the quantity to be withdrawn. It is possible to enter a negative quantity. This can be useful if you want to adjust previously incorrect withdrawal.

#### Actual date
Here you enter/see the date when the withdrawal is made or physically took place. Today's date is shown by default. If you have entered a negative quantity, you must select a date.

#### Disposable balance
In this column you see the disposable balance of the location.

#### Revision
Here you see/enter the default revision for the part on the location.

#### Cause
Here you enter a cause code for the withdrawal. These cause codes are handled in the Cause codes procedure. It is mandatory to enter a cause code if the setting called Use cause/posting in the Direct stock reporting procedure is set to Cause or Cause and posting. The column is only displayed when the system setting is activated. It is only possible to enter one cause for all rows.

#### Posting
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see the distribution of the posting in different posting dimensions. It is mandatory to enter accounts for the posting. You can enter a specification text for each posting row. The system setting Use cause/posting in the procedure Direct stock reporting determines if this column should be shown.
In the Posting matrix procedure you find the tab Direct stock reporting where you can configure the coding.

#### Project
Here you can enter a project number for the withdrawal. If a part is linked to a project in the part register, the project number will be set automatically on the transaction.
If you activate the setting Project will be copied from the row above, then new rows will by default get the same project as the row above. This does not apply if the new row is already linked to a project.

#### Batch
Here you see the batch number of the part in this location. If the part has more than one batch number on the location, then one row per batch number will be shown.

#### Best-before date
If best-before date is applied for the part in the batch, this date will be shown here.

#### Charge number
If a charge number exists for the batch number, it is displayed here.

#### Serial number
Here you see the serial numbers of the parts. The parts are shown with one row per serial number.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by selecting by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.
