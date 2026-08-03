### Operations
Reporting at part level
If a part node is selected in the structure map you will see an operation list containing the operations included for the part. In this mode you can report operations in a list. You enter quantity to report, location (for the final operation), time to report, cause code (if reported time exceeds/falls below the limit of time used in the system setting), change work center, remaining quantity, rejection list, employee, setup time to report, and actual report date for the operations.
By using the button Insert row (Shift + F5) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) you can insert operations in the operation list. By clicking the button Add new row at the end (F5) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) you can also add an operation at the bottom of the operation list. In both cases you get to select a work center and also enter quantity and time to report. It is not possible to add a new final operation when there is a quantity reported for the operation which is last.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can, for example, go to the Report maintenance procedure to report performed maintenance.
Read a description about each field on operations in the section Reporting at operation level you find below.
Reporting at operation level
If you select an operation in the structure map you will in this box see detailed information about the operation. In this mode you report one operation at a time and you can also enter additional information.
Quantity/Time

#### Quantity to report
(This field is not available for the final operation) Here you enter the number of finished/approved parts that have been processed in the operation and that should be reported.
There is a validation that will warn you if the reported quantity you enter here is larger than the remaining quantity. There is also a validation to see if it is traceable material which should be withdrawn for the reporting. Withdrawal of traceable material is done by clicking the Loc. Button in the Material box.
If you first have made a positive reporting, it is allowed to report a negative quantity provided that the remaining will not be greater than the planned quantity. However, this does not apply if the operation is the final operation and/or has serial numbers.
If the operation has a measuring plan, a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is shown if a control measurement must be performed for the entered quantity you are to report. You can then link the operation to the Report measuring data procedure via the button called Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to report the performed control measurement.
For the final operation this field is instead called Transfer to stock, see below.

#### Transfer to stock
(This field is available for the final operation) For the last operation you report the transfer to stock for a location (the number of parts that is reported and will be transferred to stock). If you enter a negative quantity, this will be shown with a minus symbol in the Reported quantity on Transport label, manufacturing, transfer to stock. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the locations registered for the part. You can select a location and add new locations. The selected location will be printed on the transport label for transfer to stock.
If the part has traceability at batch level you will in the field called Batch A batch is the set of components/products manufactured at the same time and made from the same original material. see a suggested batch number, but you can change this number. How the batch number should be designed is decided in the Number series procedure.
If the setting Apply best-before date is activated in the part register, you must enter such a date in the field Best-before date. In the part register you can also configure if the best-before date should be suggested based on two different criteria.
If the part has traceability level Serial number A serial number is a number that is used for traceability for parts on entity level., then you must also select serial number for the location, one serial number for each entity of the part.
You can also enter charge number for the location and you can link a certificate file.

#### Quantity to reject
Under the Rejection list button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add a row to be able to enter rejected quantity and select rejection code. You can also enter comments regarding the rejection and link external files. You can add several rows with rejected quantities and rejection codes, if needed. Rejections made, comments, and linked files, can be seen in the Rejection list procedure. You can report rejection for serial numbers.

#### Time to report
Here you enter the total unit time of the quantity that is being reported.

#### Goods location
(This field is not available for the final operation) Here you enter the goods location for the number of parts you are reporting. This is not done for the last operation. The goods location is printed on the transport label for manufacturing in progress and is entered as a reference to where you physically placed the reported quantity. This is done in order to make it easier for the following operators.

#### Remaining quantity
Here you can see the remaining number of parts that are left to report.

#### Previously rejected quantity
Here you can see the quantity that has already been rejected.

#### Setup time
In this field you report the setup time separated from the unit time. If the work center has an own defined cost for setup time, it can be crucial to report the setup time separately. The setup time is also governed by the setting that determines the suggested planned time. The setup time, however, is only suggested when the operation is reported for the first time. Regardless of which quantity that you report, the entire setup time will be suggested here.

#### Goods location previous operation
Here you can see the goods location entered for the previous operation.

#### Planned quantity and Reported quantity
In these fields you can see the operation's planned quantity and its reported quantity.

#### Planned time for reported quantity
Here you can see the operation's planned total time (unit time and setup time together).

#### Reported time
In this field you can see how much time that has already been reported for the operation (unit time and setup time together.)
Miscellaneous

#### Employee
In this field you can select an employee from the personnel records. This person will then be set as the executor or the person responsible for the reporting. This information will be saved in the manufacturing order log.

#### Work center
Here you can see the work center that is planned to perform the operation. It is displayed by default. However, you can change to another work center for the reporting in question. The costs will then also be based on that selected work center's cost factors. You cannot report an operation that has a pool work center as work center. In order to save, you then have to change the work center. You can only enter one work center which belongs to the pool group.

#### Actual reporting date
Here you can see/enter the date when the operation was reported. Today's date is shown by default. You can choose any date, but if you select a date that is a non-working day or more than a year back/ahead in time, you will see a warning.

#### Cause code
This field becomes available in cases where the Remaining quantity for the operation is zero and the Time to report differs more (in percent) from the planned time for the reported quantity than what is allowed according to the system settings called Mandatory cause code if time used exceeds planned time (in %) and Mandatory cause code if time used is less than planned time (in %). In such cases you must select a cause code. It can also be mandatory to enter a comment.
You can select among the active cause codes for time loss and time gain that are registered under the Time used tab in the Cause codes procedure. In that procedure you also enter if a comment is mandatory for the cause code.

#### Comment
Here you can enter a comment regarding the reporting. It is displayed in the manufacturing order log. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
Files to be linked to the reporting. By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.

#### Manufacturing order log
With this button you can access a log showing reporting items for the operation.

#### Manufacturing order log previous operation
With this button you can access a log containing reporting items made for the previous operation.

#### Change traceability
The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) is activated if there are serial numbers or batch numbers withdrawn for the operation. By clicking it you access a dialog where you can change these traceable parts' links to each other. You may need to do this if, for example, a traceable material which has been withdrawn for the operation, must be replaced during the manufacturing. Please note! A withdrawal of the new traceable part has to be made in the manufacturing order. Otherwise it will not be shown in the dialog.
