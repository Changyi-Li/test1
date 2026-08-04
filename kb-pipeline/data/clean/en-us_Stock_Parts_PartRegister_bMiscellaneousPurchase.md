### Miscellaneous
In this box you enter additional settings for the purchase of the part, and you can see the supplier invoice log and the purchase statistics for the part.

#### Quantity/package
Here you enter how many parts will fit into a package when the part is purchased. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, a transport label will be printed for each package that has been arrival reported on the purchase order. The quantity is displayed in the unit selected on the main row, but it will be saved in the standard unit. This field does not exist for parts of the Service type.

#### Default transport label
The default transport label type determines the type of transport label selected by default for the printout when the part is being arrival reported. This setting applies for all part types, except for Fictitious. Yes, select at printout is selected by default. The options available as default transport label in the field are: None, Transport label – A4, Transport label – A5, Label, or Transport label – Grouped.
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) next to the field you can select which type of Transport label, purchase should be the default for the part when it is being arrival reported, rejected, or returned. You can also select from you own transport label variants created in the Document templates procedure. If you choose a transport label under this button, this will override the transport label selected, if any, in the Default transport label field.

#### Alloy code/Mark-up
In this field you enter the alloy cost that applies when purchasing the part. The alloy code/mark-ups are handled in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure. This field does not exist for parts of the Service type.

#### Alloy quantity
Here you enter a quantity of the mark-up included in the part. The unit is loaded from the Basic data – Part procedure.

#### Distribute purchase
With this button you access the window where you can configure distributed purchases between suppliers in the supplier links for the part. Here you see the part's supplier links in the Supplier links table. Here you also see the information from the supplier links. In the Distribution by order table, you add the suppliers to be included in distributed purchase of the part by dragging and dropping the supplier link to the table, or you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_next.png) found on the function menu.
> Please note! It is only the requirement calculation and the net requirement calculation that can create purchase order suggestions with distributed purchase. If you manually register a purchase order for the part, distributed purchase will not be taken into consideration. At present, distribute purchase is not supported in the following cases: Subcontract purchase Fictitious parts Configured parts
> Distribution in % does not work for purchase orders created from customer orders or manufacturing orders. This is because it is only possibly to have a purchase order linked to one purchase order row/manufacturing order row.
Distribution by percentage
Distribution by percentage means that the purchases are distributed according to the entered percentage between the suppliers you have added in this table. For example, if the purchase order suggestion includes 100 pieces of the part and one of the suppliers has the distribution set to 70% and the other one has it set to 30%, it means that 70 pieces will be ordered from the first supplier and 30 from the second supplier.
You can only add a specific supplier link once in this table.
> Use the supplier link with the longest lead time as the Default (Active) supplier among the suppliers in the distribution. This will have the generation of purchase order suggestions works optimally.
You can also update the distribution in percentage for several part at a time. This is done using the Distributed purchase by percentage list type in Part list procedure.
If you use distribution by percentage, the net requirement calculation and requirement calculation will create multiple purchase order suggestions from a shortage.
The number of suggestions will be divided according to the distribution of parts and the part's planning settings. Each suggestion will get assigned to a supplier.
Example:
Rounding quantity = 5
Minimum quantity = 120
Required quantity = 100 which will be replaced by the minimum quantity 120. 120 will then be distributed between two suppliers:
70% to the first supplier.
30% to the second supplier.
This would create two suggestions, one with 84 pieces and the other with 36. 84 is not a multiple of 5 and will therefore be rounded up to 85. 36 is not a multiple av 5. This means the suggestions will be 85 and 40 pieces.
Distribution by order
Distribution by order means that the first purchase is assigned to the supplier on row 1 in this table. The second purchase goes to the supplier on row 2. The third purchase goes to the supplier on row 3, etc.
You can change the mutual order of the purchases between the suppliers by moving them with the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) on the function menu.
You can the same supplier multiple times in this table. Example: You want the first purchase to go to supplier A, the second purchase to go to supplier B, the third purchase to go to supplier A again, the fourth purchase to go to supplier C, etc. This means that you can have two order rows on the purchase order suggestion to supplier A.
In the Next column you can mark which supplier should be purchased from next time. This is useful if you at some point want a different supplier to be purchased from next. When that purchase has been made, the supplier on the next row in the distribution will get Next marked. This mark is automatically moved to the next row for each purchase and will then start over with the supplier on row 1.
You can also update the Next column for several parts at a time. This is done using the Distributed purchase per order list type in the Part list procedure.
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), there is information from the supplier links, such as part prices, currency, validity period, the supplier's part number and lead time.

#### Supplier invoice log
By clicking this button, a dialog box will show a log of final recorded supplier invoices. In this dialog box you can choose to see the actual supplier invoice document. You can also link to the procedure Register supplier invoice for each log record. If you have installed the option Warehouse, the statistics is shown for the selected warehouse.

#### Purchase statistics
By clicking this button you can view a total of the purchase statistics. If you have installed the option Warehouse, the statistics is shown for the selected warehouse.
