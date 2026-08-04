### Order
You can in this box create a customer order or blanket order based on the quote in question when it is saved. It is not possible to create a customer order or blanket order from a preliminary quote, that is, when the quote has the Preliminary checkbox activated in the Miscellaneous box.
You can choose which quote rows to be released as order rows on the customer order by using the C-order checkbox on the quote rows. The quote rows for which the checkbox is not activated, will not be included in the order that will be created. If you choose to turn some of the quote rows into a customer order and that the quote should not be finished, then it is not possible to check the C-order box on the same quote rows again. In that case, you will instead see the customer order number on those rows.
If there are quote rows left, for which the C-order checkbox is not checked, you will see a warning saying that there is no marked row to release to order.
When you create a customer order based on a quote and the customer has the setting called Alloy cost set to At order registration, and the part has alloy cost data, then alloy cost rows will be created on the customer order.
If the Product configurator option is used and you have a configured part on the quote row, then you cannot create a customer order based on the quote row as long as you have the configuration window. You open the configuration window with the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) button in the Configuration column. The Create customer order button in the box is then deactivated until you have closed the configuration window and saved any changes made in the configuration.

#### Create customer order
When you click the Create customer order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_new.png), a dialog box opens where you can enter information and what should take place when the quote or parts of the quote is turned into a customer order.
Settings in the Create order dialog.

#### Order
Here you decide if it is a customer order or a blanket order which should be created.

#### Order type
Primarily, the default order type from the Order types procedure is suggested. Secondarily, the customer order type/blanket order type configured for the logged in user, will be suggested. And thirdly, if order type for quote type and for user is missing, the last entered order type will be suggested.

#### Order number
You can enter a new order number or leave the field empty in order to load the next available order number from the number series.

#### Copy posting
With this checkbox you decide if the posting should be copied to the new order.

#### Priority
Here you enter the priority to be used on the order.

#### Finish this quote
With this setting you decide if the quote should be finished. Once you have finished the quote you cannot edit anything in it.

#### Finish related quotes
Here you determine if the related quotes should also become finished when you create the order.

#### Finished activities on quote
Here you decide if all activities on the quite should be set to status Finished. If you delete the order, the status of the activities will be reset.

#### Copy internal/external comment
These settings determine if the internal and external comments should be copied to the order.

#### Include document structure
If this setting is marked, it means the document structure is copied from the original order. If this setting is not checked, it means the document structure is copied from the selected order type.

#### Extra fields
With this setting you decide if Extra fields should be included to the order.

#### Extra fields – Rows
With this setting you decide if Extra fields on rows should be included to the order.

#### Lock price on order
With this setting you decide if the prices on the new customer order/blanket order should be locked. This way you avoid recalculation of prices in foreign currency if the exchange rate is changed.

#### Open order
With this setting you decide if the new customer order/blanket order should be shown in the Register customer order procedure or Register blanket order – Sales once you click OK in the dialog box and the order is created.
You can see the created orders in the table in the box, and from there you can go to these orders in the Register customer order or Register blanket order – Sales procedure via the link ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png). You can also preview ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) what they will look like at printing.
Customer order transfer
If you have the Customer order transfer option and create a customer order from a quote and you have selected an order type with a default transfer profile, the quote row's transfer profile will be copied to the customer order row. Rows without a transfer profile will be assigned the transfer profile from the part or the order type. Priority for transfer profile when customer order is created from a quote:
1. Transfer profile for quote.
2. Transfer profile for part.
3. Transfer profile for the order type.
