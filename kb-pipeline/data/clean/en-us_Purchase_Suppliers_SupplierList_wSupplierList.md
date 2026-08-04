## Supplier list
In this procedure you can create lists with data from the supplier register. These lists can be updated/modified for existing records. It is not possible to create new suppliers or sub-records such as reference persons, etc.
There is a standard list type which loads suppliers in a simple list. Depending on which presentation you have selected, different data will be loaded to the list. You can also load addresses, references, communication information, and exception accounts.
The lists can be convenient to use to mass-update different information for existing suppliers.
List types

#### Standard
This list type handles different presentations of data registered directly for the supplier and of which there is always only one set. The following presentations are available:
- Terms/Prices – Here you can see payment terms, delivery terms, etc.
- Import/Printouts – Here you can see language, currency, date format, decimal separator, time zone, print order via, etc.
- Receiving inspection – Here you determine if receiving inspection should be applied.
- XML/Documents – Here you see order where an XML file can be attached, delivery schedule where an XML file can be attached, cases where an XML file can be attached, see document variants for inquiry, purchase order, claim reports, waybills, etc.
- Delivery/Shipping – Here you can see delivery days, transport time, etc.
- Outgoing payments – In this presentation you can see payment method, etc.
- Exception – Here you can see account for outgoing payments, purchase account, offset account for accrual, etc.
- SRM – Here you can see district, purchasing agent, etc.
- Miscellaneous – Here you can see supplier role, VAT group, calendar, etc.
- Inactive suppliers – shows suppliers that have been deactivated.

#### Addresses
This list handles different addresses that have been entered for the supplier. This list can present the supplier’s:
- mailing address
- delivery address
- visiting address.

#### References
This list handles different addresses that have been entered for the supplier.

#### Communication
This list handles the supplier’s phone number, fax number, and e-mail address.

#### Level list
This list type shows supplier relationships according to the setting Parent company (supplier).

#### Exception accounts
This list handles the exception accounts that have been entered for the supplier.

#### Bank accounts
This list handles the bank accounts that have been entered for the supplier. Many of the information items in the list can be updated.

#### Receiving inspection
In this list you can update receiving inspection for multiple supplier at a time.

#### EIM Workflow settings
(This list is included in the EIM Workflow option.) This list is used to update supplier settings for EIM Workflow.

#### EIM Workflow exceptions
(This list is included in the EIM Workflow option.) This list is used to update exceptions for EIM Workflow.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
