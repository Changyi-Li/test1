## Invoice overview – EIM
This procedure is available if you have installed the Electronic invoice management (EIM) option. The procedure is also available to user with the license type called External authorization.
Here you find information about supplier invoices in the EIM flow. In the Standard list type you can, for example, see which invoices have been sent for authorization, which invoices are fully authorized, and which invoices are available for final coding. The list type Change signer is possible to update. There you can change the signer for invoices. By using the button called Show invoice information ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) you can find an invoice image as well as invoice information.
In the Statistics list type you find historical data (statistics) regarding signer information for invoices that have been fully processed in the EIM flow. The statistics show the number of invoices that have been handled and it also shows the handling time per invoice.
If the option EIM Workflow is installed, there are also two list types you can use to monitor and view information about invoices in the Workflow.
Data that is shown in this procedure is based on information in the accounts payable that is linked to EIM data.
Reminders via e-mail and forwarding of invoices that have awaited authorization too long or where the due date is approaching, are automatically taken care of by a monitoring function in the system. This function forwards/relocates the invoices and e-mails reminders to you. In the procedure Authorization settings – EIM you find a tab called Scheduling where you handle this function.
List types

#### Standard
By default, this list type shows information about invoices that have been sent for authorization. Using the settings under the Selection tab you can choose to include invoices in other stages of the flow, for example rejected invoices, invoices awaiting final coding, or invoices already filed. The list can be grouped by signer or consecutive number. It is not possible to update information in this list.

#### Change signer
This list type is possible to update and it is used to move invoices (in the list) from one signer to another. The list displays invoices with status Sent for authorization. You can also choose to show future signers in the list as well.

#### Statistics
This list shows statistics, for example handling time per invoice, and number of invoices per supplier or signer for a given period. You can total the list by order number, supplier, or action date. It is not possible to update information in this list.

#### Import overview
This list is available if the EIM and EIM Workflow options are installed in your system. This list displays which invoice and also how many have been imported for a selected date or for a selected supplier.

#### Current status in Workflow
This list is available if the option EIM Workflow is installed in your system. You can here see invoices' match result and the reason for authorization. The list also shows information from purchase order and invoice rows.

#### Workflow log
This list is available if the option EIM Workflow is installed in your system. Here you can view a log of when Workflow runs were started. You also see log of invoice status, match results, reason for authorization, and current invoice status.

#### CrossState invoices
This list displays information about e-invoices and interpreted invoices if you have activated CrossState (digital invoice flow). The list contains raw data imported from CrossState, such as data interpreted from the invoice header, invoice rows, and application settings.
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
