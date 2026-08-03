### The New calculation list
Under the List tab you see all selected parts for which you can perform a pre-calculation if you chose the New calculation list type. In this list you can check and adjust quantity and deselect parts that should not be included in the calculation. If you under the Saving heading in the Selection tab selected a price alternative to save to, then it is possible to after the calculation deselect parts for which you do not want to save a new price. You will e.g. see warnings and new prices for those parts.
If you choose to explode or recalculate manufactured parts, those parts will be displayed after the calculation has been made. The exploded quantity is only used to save the exploded part. In the selection rows’ calculation, the exploded quantity is always used for that part in question.

#### Part number
In this column you can see the part number of the selected part.

#### Configuration
This column is shown if the option Complete has been selected in the setting Configuration. You find this setting under the heading Miscellaneous under the Selection tab. Then it is possible to here click a button and change the part's default configuration (template) before the calculation. This button is only shown on the rows which contain a part possible to configure (a part linked to a configuration group). If there is a default configuration, you will see this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png). If there is no configuration, you will instead see this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png). If configuration is missing or should happen to be incomplete (in the template), you will see a warning after the calculation, see Warnings (W) below.

#### Warnings (W)
If any warnings exist after the calculation, you can here click a button in this column to directly go to the warnings, if any, under the Warning list tab. If you have not clicked the button it shows an orange warning triangle ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png). If you have clicked the button it shows an orange exclamation mark !. Warnings are not saved for calculations.

#### Name
Here you see/enter the name of the part.

#### Part type (T)
Here you see a symbol indicating which type of part the part is. When you hover over the symbol, a tooltip will display the part type in text form.

#### Quantity
The number of parts on which the calculation is based. You can change the quantity for the parts in your selection. This value is saved as the part's calculated quantity if you under the Selection tab have chosen to save calculated quantity. If you have configured quantity terms for the part in the BOM and routing, these will be taken into consideration.

#### Standard price
Here you can see the current standard price of the part.

#### Existing price
If you have selected a price to save to, you will here see the existing price of the part according to the price alternative selected on the first row in the table under Saving. A tooltip is shown when you hover over the field, displaying the price alternative.

#### Include
By default, all records are included in the calculation. You can deselect individual records by unchecking the respective box, or deselect all underlying records by unchecking the box in the column heading.

#### Last calculation
The date and time of the last (most recent) calculation that has updated a price for the part, that is, when you have chosen to save a cost to a price for the part.

#### Last price change
The last price change from the part register which is corresponding to the price alternative which you under Saving under the Selection have selected to save to (on the first row in the table). A tooltip is shown when you hover over the field, displaying the price alternative you have selected. This column is only shown if you have chosen to save to one or several prices alternatives.

#### Finish date
The suggested Finish date of the order is today's date, but this can be changed. If you have configured date terms for the part in the BOM and routing, these will be taken into consideration.

#### Revision
Here you see the part's active revision, but it is possible to change. Revision terms are taken into consideration if you have configured them for the part in the BOM and routing.

#### Order number
Here you can enter an order number if you wish to perform the pre-calculation for a certain order number. Terms for the order number will be taken into consideration if you have configured such for the part in the BOM and routing.

#### Customer/Customer number
Here you can enter a customer if you wish to perform the pre-calculation for a certain customer number. Terms for the customer will be taken into consideration if you have configured such for the part in the BOM and routing.

#### Variant code
You can enter a variant code if you wish to perform the pre-calculation for a certain variant code. Variant code terms are taken into consideration if you have configured such for the part in the BOM and routing.

#### Created when
The date when part was created.

#### Last modification of BOM and routing
Here you see the date when the BOM and routing was most recently modified.
Columns that are displayed also after the calculation:

#### Existing price
The existing price from the part register which is corresponding to the price alternative which you under Saving under the Selection have selected to save to (on the first row in the table). A tooltip is shown when you hover over the field, displaying the price alternative you have selected. This column is only shown if you have chosen to save to one or several prices alternatives.

#### New price
Here you see the new calculated price corresponding to the alternative you have selected to save from under Saving under the Selection tab.

#### Setup price
Setup price amount in the alternative which you chose to save from. This column is only displayed if you under Saving under the Selection tab have chosen to save from one of the alternatives with a separate setup price.

#### Difference
Here you can see the difference between the new price and the existing price.

#### Difference in %
Here you see the difference between the new price and the existing price in percent.

#### Save calculation
By default, the pre-calculation should be saved for the part, even if warnings have occurred during the calculation. With the setting Save calculation in spite of warning under the Selection tab you determine if it should be possible to save the calculation even though there are warnings. If the calculation is not saved, it is also not possible to save price for the part.

#### Save price
By default it is activated to save prices which have been calculated for the par to the price alternative you selected under Saving under the Selection tab. If you have not selected a price alternative to save to (and from), this column will not be available.
It is only possible to save price on part if the pre-calculation is saved on the part.
