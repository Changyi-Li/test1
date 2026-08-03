### Miscellaneous

#### Warehouse
If you have installed the Warehouse option, you here see the operation's warehouse.

#### Employee
In this field you can enter an employee which is loaded from the personnel records. This employee will be entered as who performed the reporting or who is responsible for the reporting. This information will be saved in the manufacturing order log.

#### Work center
By default you can here see the work center that is planned to perform the operation. However, you can change to another work center for the reporting in question. The costs will then also be based on that selected work center's cost factors. You cannot report an operation that has a pool work center as work center. In order to save, you then have to change the work center. You can only enter one work center which belongs to the pool group.

#### Actual reporting date
Here you can see the date when the operation took place. The field shows today's date by default. You can choose another date, but if you select a date that is a non-working day or more than a year back/ahead in time, you will see a warning.

#### Cause code
This field becomes available in cases where the Remaining quantity for the operation is zero and the Time to report differs more (in percent) from the planned time for the reported quantity than what is allowed according to the system settings called Mandatory cause code if time used exceeds planned time (in %) and Mandatory cause code if time used is less than planned time (in %). In such cases you must select a cause code. It can also be mandatory to enter a comment.
You can select among the active cause codes for time loss and time gain under the Time used tab in the Cause codes procedure. In that procedure you also enter if a comment is mandatory for the cause code.

#### Comment
Here you can enter a comment regarding the reporting. It is displayed in the manufacturing order log. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
Files to be linked to the reporting. By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can link files to the reporting. It is displayed in the manufacturing order log.

#### Manufacturing order log
With this button you can access a log showing reporting items for the operation.

#### Manufacturing order log previous operation
With this button you can access a log containing reporting items made for the previous operation.

#### Change traceability
The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) is activated if there are serial numbers or batch numbers withdrawn for the operation. By clicking it you access a dialog where you can change these traceable parts' links to each other. You may need to do this if, for example, a traceable material which has been withdrawn for the operation, must be replaced during the manufacturing. Please note! A withdrawal of the new traceable part has to be made in the manufacturing order. Otherwise it will not be shown in the dialog.
