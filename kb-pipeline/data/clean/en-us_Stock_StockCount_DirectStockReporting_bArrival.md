### Arrival
In this box you report direct arrivals.

#### Part number
You can add rows and select for which part arrivals will be made

#### Current total balance
Here you can see the current balance of the part. It is a total of the balances on all locations.

#### Unit
Here you see the unit in which the reporting is made and in which the current stock balance is displayed. This unit applies during reporting. The current stock balance is also shown in this unit. The default unit is the unit selected in the Part register to apply for stock count/stock reporting for the part in question.

#### Comment
Here you can enter a comment regarding the arrival. Mandatory comments can be configured to apply when entering certain cause codes. For such codes a comment must always be entered.

#### Location
In this column you see the name of the location. If you perform arrival reporting you can use the button Add location ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) to add a new location where you can stock a quantity of the part.

#### Balance
In this column you see the current balance of the location.

#### Quantity
Here you enter the quantity that should be arrival reported. It is possible to enter a negative quantity. This can be useful if you want to adjust previously incorrect arrivals.

#### Actual date
Here you enter/see the date when the arrival is made or physically took place. Today's date is shown by default. If you have entered a negative quantity, you must select a date.

#### Revision
In this field you see part's revision on the location. The part's active revision is used by default. It is possible to change to a different revision which is already registered on the part.

#### Cause
Here you enter a cause code for the arrival. These cause codes are handled in the Cause codes procedure. It is mandatory to enter a cause code if the setting called Use cause/posting in the Direct stock reporting procedure is set to Cause or Cause and posting. The column is only displayed when the system setting is activated.

#### Posting
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see the distribution of the posting in different posting dimensions. It is mandatory to enter accounts for the posting. You can enter a specification text for each posting row. The system setting Use cause/posting in the procedure Direct stock reporting determines if this column should be shown.
In the Posting matrix procedure you find the tab Direct stock reporting where you can configure the coding.

#### Project
Here you can enter a project number for the arrival. If a part is linked to a project in the part register, the project number will be set automatically on the transaction.
If you activate the setting Project will be copied from the row above, then new rows will by default get the same project as the row above. This does not apply if the new row is already linked to a project.

#### Batch
If you arrival report parts to a location and the part has traceability at batch level, then you must here enter a batch number.

#### Best-before date
If best-before date is applied on the part in the part in the batch, you must enter a best-before date on the part you are arrival reporting on the location.

#### Charge number
If a charge number is included in the parts that should be arrival reported, this is entered here.

#### Certificate
If a certificate is included in the parts that should be arrival reported, you can scan it as a PDF file and link it under the Files ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) button in this column.

#### Serial number
If you arrival report parts to a location using traceability at serial number level, then you can use the Serial numberA serial number is a number that is used for traceability for parts on entity level.![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to enter from which number the serial numbers for the arrival reported parts should start. If you enter a serial number which already exists that part will not be arrival reported. After you have entered a start number in the From column, you then enter in the Quantity column how many parts to arrival report. Then the end number will be calculated automatically in the To field. You can enter a prefix that applies to the entire interval.
You can import serial numbers from a text file using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) button, called Import serial numbers.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.
