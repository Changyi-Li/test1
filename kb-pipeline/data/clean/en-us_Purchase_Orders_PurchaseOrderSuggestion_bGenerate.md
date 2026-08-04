### Generation
Here you find settings regarding how the list should be handled and settings regarding generation of actual purchase orders based on the purchase order suggestions in the list.

#### Dividing
With this setting you determine how the purchase orders should be divided. Supplier is selected by default. This means that the system will suggest that one purchase order will be generated for each supplier. Different parts are then gathered in one order. If you select Part, the system will suggest that one purchase order will be generated for each part. In that case, different parts are not mixed in the same order. If you choose the Order row option, one order row will be created per purchase order.

#### Purchase order type
Here you decide the order type that the generated actual orders will have. The choice made here affects e.g. the posting, purchase statistics, and priority of the generated orders. You can select among the order types with the basic type Buy material that are active in the Order types procedure.

#### Purchase order type – Stock order
This setting is available if the Warehouse option is installed in your system. Here you decide which order type for stock order that the generated actual orders will have. The choice made here affects e.g. the purchase statistics and priority of the generated orders. You can select among the order types with the basic type Stock order that are active in the Order types procedure.

#### Our reference
The person you select in this field is the person in the company that will be registered as Our reference on the purchase orders that are generated.

#### Goods label
The goods label you enter here will be registered as Goods label on the purchase orders that are generated.

#### Disregard lead time on part
With this setting you determine if the calculation of suggested delivery date in the list should disregard the lead time of the parts and instead be based on the actual requirements.
When this setting is activated, the suggested delivery date is calculated as the requirement date minus the safety time. This setting is not activated by default, and this means the suggested delivery date is calculated as the requirement date minus the safety time and minus the lead time. If Disregard lead time has NOT been selected and the date falls within the part’s lead time, the suggested delivery date will set according to the part’s lead time.
If Disregard lead time has been selected and the date is within the part’s lead time, the suggested date will be used as the requirement date.

#### Suggest "Apply" for all suggestions
With this setting you determine whether or not the checkbox Apply should be marked by default for all suggestions in the list.

#### Suggest "Apply" for rescheduling suggestions
This applies to the Detailed list type. With this setting you determine whether or not the checkbox Apply will be selected by default for all the rescheduling suggestions in the list.

#### Suggest "Match" for qty in linked purchase order
This setting determines if the Match column (in the list) is selected by default when suggestions are generated. This makes it so that the purchase order suggestion’s quantity matches the quantity that the manufacturing order requires in cases when the quantity on the manufacturing order has been increased or decreased. Applies to purchased parts with Linked requirement.
