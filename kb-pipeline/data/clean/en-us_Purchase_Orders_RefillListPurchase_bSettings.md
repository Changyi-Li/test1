### Settings
Formulas

#### Order quantity
With this setting you decide which formula to use for calculating order quantity. The default formula for this field is configured in the Planning formulas procedure.

#### Refill signal
Here you decide which formula you want to use for refill signal. The default formula for this field is configured in the Planning formulas procedure.

#### Priority
Here you decide which formula you want to use to calculate priority. The default formula for this field is configured in the Planning formulas procedure.

#### Apply minimum quantity
With this setting you decide if the calculated value should be changed to the part's Min. quantity instead, if the calculated value is lower.

#### Apply rounding
With this setting you decide if the calculated value should be rounded up according to the part's rounding quantity.

#### Use current pace
With this checkbox you decide if current pace should be used in the calculation. This setting is only shown if you have Yes set in the system setting Show annual budget, annual volume, and order quantity with current pace.
Show

#### Consumption statistics
With this checkbox you determine if consumption statistics should be shown in the list. Three columns can be displayed for 3, 6, and 12 months' consumption.

#### Unit
This setting determines in which unit the part should be displayed. If you choose Default, the part is shown in the unit that is set as default in the part register. If you choose Purchase, the part is shown in the unit that is set as default for the purchase order under the button Usage in the part register.
Generation

#### Dividing
With this setting you determine how the dividing for the suggestions should be made. If you choose the option Supplier, then one purchase order is created per supplier and currency. Since the currency is loaded from the supplier link, the same supplier can receive orders in several different currencies. If you choose the option Part, then one purchase order per part will be created.

#### Purchase order type
With this setting you determine which order type should be given to the purchase order when you turn the suggestion into an order. The choice made here affects e.g. the purchase statistics and priority of the generated orders. You can select among the order types with the basic type Buy material that are active in the Order types procedure.

#### Purchase order type – Stock order
This setting is available if the Warehouse option is installed in your system. Here you decide which order type for stock order that the generated actual orders will have. The choice made here affects e.g. the purchase statistics and priority of the generated orders. You can select among the order types with the basic type Stock order that are active in the Order types procedure.

#### Our reference
Here you can select among the persons in the company who are registered as references in the personnel records. If you start typing in the field, the system will suggest the reference that matches what you have typed. The More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) becomes visible after you have selected/entered a reference. Using it you can access information about the reference in question. The Our reference field will by default show the name linked to the logged-in user.

#### Goods label
You can enter goods label on two rows. The goods label is used when you want the supplier to mark/label using a certain text or a reference number. The goods label is displayed on order documents and on transport labels. The total length of the goods label cannot be more than 78 characters.

#### Suggest "Apply" for all suggestions
With this setting you decide if all suggestions should be marked by default in the Apply column in the list.
Delivery address

#### Change address
By clicking the Change address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can change the delivery address, if needed. You can select among the following delivery addresses: the company's (the warehouse), the customer's, and the supplier's.
The selected delivery address determines some of the information on the order that is being registered. This information will be updated when you change supplier if it differs from the information on the default delivery address. The following information is updated: delivery terms, delivery method, goods receiver reference, customer number (shipping agent), transport time, destination, place of terms of delivery, customer group, VAT group, and communication information.
