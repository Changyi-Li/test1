### Miscellaneous

#### Administrator
You can select an administrator via employee number of the reference persons registered in the Personal records procedure. The name of the administrator is shown to the right of the field. By using the button More information ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see additional general information and contact information about the selected administrator. Part administrators are used as selection terms in many lists. This way all planners are able to print lists of parts that they administer.

#### Cases
The Cases button is activated if there are cases regarding the part. By clicking this button you access information about those cases.
> This button is activated if there are records in a some of the available warehouses in the company. This means that the button can be activated but has no content. Then the records are found in another warehouse than the one you are working in. You select warehouse under the button Warehouses ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) on the toolbar.

#### Service type
There are three sub-categories for service parts:
- Freight – used for freight charges on orders
- Alloy cost – used for alloy costs on parts on orders
- Unspecified – used for other services and can also be used for alloy cost.
The service type is used to, for example, inform the buyer what the service concerns, in connection with the communication taking place via Monitor-to-Monitor. This can be seen as a way to make it easier for the buyer to register the supplier invoice. In the receiving system, the customer (the receiver of the Monitor-to-Monitor invoice) can configure which part number the different services should be registered on when the supplier invoice is imported and linked to the purchase order.

#### Partial quantities
Partial quantities is an option, that is, not included in standard functionality. By clicking the Partial quantities button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access a window where you can register partial quantities of the part. It is useful if you store the part in bulk or in free lengths (e.g., cable on cable drums). You can then add the number of different partial quantities of the part, the quantity of each partial quantity, and link a packaging part to the respective partial quantity.
When registering an order for a part with partial quantities, you load the quantity on the order via a button called Partial quantity which is then available on the order. Use this button to show the partial quantities registered here, and you can choose between one or multiple partial quantities, as well as quantity from each partial quantity, which is then totaled and put in the quantity field on the order. You can also add/delete rows with partial quantities for an order. The partial quantities you enter t´for an order will only be saved on that specific order and not here for the part.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.
