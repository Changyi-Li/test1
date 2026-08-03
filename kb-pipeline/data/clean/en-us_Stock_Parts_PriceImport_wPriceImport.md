## Price import
In this procedure you can import prices from text files. The prices that can be imported are:
- Standard prices
- Supplier prices (this also applies to subcontract parts)
- Customer prices
- Price lists
You can import future prices for standard prices, supplier prices, customer prices, and price lists if the system setting Manage future sales prices has been set to Yes. You can also import staggered prices.
The part number in the file must be registered to be able to import prices. The part number must either be registered as our part number or as supplier's/customer's part number. Supplier links must exist for the part for the current supplier in order to be able to load supplier prices. This also applies to customer prices.
Import file
In the Import file box you enter the path to the file from which you will import data. To start the import click the button Import ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) in the toolbar. All data will be loaded to the list in the Loaded records box. You can manually add and delete rows. You can also filter to decide which rows to see. To complete the import you must check the box Include for the rows you wish to save and then click Save ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png). When you save, the included rows will be removed from the list.
Format templates
You can configure the format of the file at the time of the import. You can create a temporary format or a format template which can be used again.The function Format templates is found in the backstage of the procedure. There you can select for which columns data should be loaded/imported. For the content of the file you can also configure which limiters should be used as column limiter and decimal limiter. Furthermore you can enter a specific number of initial rows which should be skipped during the import.
Read more about [format templates](../../../UserGuide/GeneralFeatures/FormatTemplates.htm).
