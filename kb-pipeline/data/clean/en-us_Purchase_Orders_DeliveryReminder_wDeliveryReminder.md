## Delivery reminder
In this procedure you can send reminders to suppliers that have not made the deliveries corresponding to your purchase orders on time.
The reminders are loaded in form of documents that you can either print or send by e-mail. The delivery reminders are grouped so that there is one document per supplier. If the supplier is marked as a Stray supplier A supplier from which you rarely make any purchases. A stray supplier is registered with a supplier number used for one-time purchases from different physical suppliers that you therefore do not want to register in the supplier register. For suppliers marked as stray suppliers, you fill in all the fields on the order instead. (a setting in the supplier register), then there is one document per purchase order (since a stray supplier can be different actual suppliers). If the currency or printing method differs between different purchase orders, then there is also one document per purchase order.
Grace Period
Order rows with a remaining quantity greater than 0 (zero) are included in the reminder. The setting Days of grace The term days of grace (or grace period) is used at requirements planning in order to calculate rescheduling of actual orders that cover the requirement but that are too late in time, instead of suggesting a new order. for delivery determines how many work days that can pass from the entered delivery date before the order row will be included in the delivery reminder list. If you enter e.g. 1 work day, the delivery date on the order row must be at least 1 work day delayed in relation to the row's delivery date in order for the row to be included in the reminder document. If you enter -1 (minus one) as days of grace, you will also include order rows that should be delivered the next day. With the setting Days between reminders you make it easier to avoid sending several reminders during a short time.
Subcontract
Orders of the subcontract type are also managed in this procedure. That reminder document also shows some information about the manufacturing order/operation. However, the order type subcontract is not mixed with other order types on the documents.
List types

#### Delivery reminder
As standard, there is only one list type in this procedure. It shows reminders regarding deliveries.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
