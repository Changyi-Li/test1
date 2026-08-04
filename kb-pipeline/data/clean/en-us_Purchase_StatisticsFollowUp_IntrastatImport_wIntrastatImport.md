## Intrastat import
The purpose of this procedure is to be able to create a report for Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. import. Data can be exported according to a fixed format that can be sent to the affected authority. In the procedure you can make additions/adjustments in the report. Additions and adjustments are saved in a separate table in the database.
Intrastat import is based on statistics loaded from the supplier invoice log (invoices), arrival log (stock orders and purchases from suppliers where you link the supplier invoice), and adjustment log for intrastat. Order price is used instead of invoiced price for orders not linked to an invoice. This procedure considers warehouses.
In order to include values in the report, the following is required:
- The part must have a CN code that is configured to be reported in the Intrastat report.
- The country in the delivery address must be within EU. Your own country will not be taken into consideration. Please remember that your country is loaded from the delivery address for the selected warehouse. That is, if you are logged in to a warehouse in Denmark (DK), then data will be loaded from all EU countries except for Denmark (DK).

#### Work flow in the procedure
1. Make a selection by date
2. Load the list
3. Check the outcome
4. Adjust/add records
5. Save
6. Print or export the list via the Export button
> If it is not possible to load the list, it might be because settings are missing. If that is the case, you will see a text under Settings letting you know which settings are missing and in which procedure you can adjust them.
> Read more under Using Monitor about [Intrastat](../../../UserGuide/Using/Intrastat/Intrastat_export_import.htm) and the related settings.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
