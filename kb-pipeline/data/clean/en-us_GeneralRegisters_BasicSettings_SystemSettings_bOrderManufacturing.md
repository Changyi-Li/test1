### Order

#### Automatic withdrawal of material
This system setting determines if automatic withdrawal of material should be made when reporting operations. When this system setting has been set to Yes, you can make exceptions per work center by using the setting Exclude from automatic reporting of material in the work center register.

#### Automatic reporting of tools
This system setting only applies if you have installed the Tools & Maintenance option. This system setting determines if automatic withdrawal of tools should be made when reporting operations. When this system setting has been set to Yes, you can make exceptions per work center by using the setting Exclude from automatic reporting of tools in the work center register.

#### Return reusable tools when return operation is reported as finished
This system setting only applies if you have installed the Tools & Maintenance option. If this system setting is set to Yes, then reusable tools that have been withdrawn to an operation on an order will be automatically returned. This takes place when the operation is reporting as finished. The condition for automatic return is that the remaining quantity of the operation will be zero and that no person is clocked-in on the operation. If the system setting has been set to No (default), no automatic return will take place. The return has to be performed manually in the Withdrawal list procedure.

#### Report material at shipment of subcontract
This system setting determines if reporting of material should be carried out at shipment of subcontract. By default, this system setting is Yes. The material will then be withdrawn on shipment and the material is shown in the list. If the system setting is set to No, the material will instead be withdrawn when arrival is reported. Please note! The system setting called Automatic withdrawal of material must be set to Yes in order for this setting to function.

#### Automatic printout of transport labels with subcontract del. note
With this setting you decide if automatic printout of transport labels should take place when printing subcontrac delivery note in the Subcontract documents/Shipped procedure.

#### Suggest total setup qty at first automatic material reporting
If this setting is activated for tools or parts, the total setup quantity is reported in the first reporting item and will not be reported again.

#### Merge same material from fictitious parts
If a material (with the same part number) exists on several material rows that belong to several included fictitious parts in a material list, these material will be merged into one row when activating this setting. For example, where both plus and negative quantities are included. When this system setting is activated, material from the BOM and routing and material from fictitious parts will also be merged. Provided that they contain the same material. For example, a manufactured part that consists of a purchased material in the BOM and routing and a fictitious part that contain the same purchased material.

#### Manage instruction from included fictitious part's material row
If the system setting Merge same material from fictitious parts has been activated, this system setting determines how material instructions for fictitious parts should be handled. The available options are:
- Add information – Information on the fictitious part's material row will be added to the information on the matching material at the higher level when registering the manufacturing order.
- Keep existing information – Information on the fictitious part's material row will be saved to the information on the matching material at the higher level ONLY if that material has no existing information. Otherwise, the information will not be saved to the matching material at the higher level.
- Replace information – Information on the fictitious part will replace the information on the matching material at the higher level. Any existing information will then be replaced.

#### Leave parts with a planned quantity of 0, in the material list
This system setting determines if material rows with 0 in quantity should be left in the material list when placing an order. These can thereby be displayed in different situations. Material rows with a zero quantity can occur via, for example, different formulas in the product configurator.

#### Copy the material row's manufacturing comment when registering orders
This system setting determines if the manufacturing comment on a purchased part should be shown as material instruction on a manufacturing order.

#### Manage instruction from included fictitious part's operation row
If the system setting Merge same material from fictitious parts has been activated, this system setting determines how operation instructions for fictitious parts should be handled. The available options are:
- Add information – Information on the fictitious part's operation row will be added to the information on the matching operation at the higher level when registering the manufacturing order.
- Keep existing information – Information on the fictitious part's operation row will be saved to the information on the matching operation at the higher level ONLY if that operation has no existing information. Otherwise, the information will not be saved to the matching operation at the higher level.
- Replace information – Information on the fictitious part will replace the information on the matching operation at the higher level. Any existing information will then be replaced.

#### Leave fictitious parts in order's material list
This system setting determines if rows with fictitious parts should be left in the material list when placing an order. These can thereby be displayed in different situations. If fictitious parts have additional text and linked files, these will also be left in the material list.

#### Include number of machines/persons per order in lead time calculation
This system setting determines if the number machines/persons in the work center should affect the lead time calculation.

#### Check capacity during manufacturing order registration
With this setting you decide whether capacity should be checked when registering manufacturing orders. Monitor takes the capacity into account when you register manufacturing orders and does not put all order driven nodes on the requirement date. This setting allows you to create structure orders with multiple nodes containing the same work center without planning to use more time per day than what you have capacity for.
The following options are available:
- No – The order is registered as per the requirement date in BOM and routing regardless of the work center’s capacity.
- Yes (within order) – The work center’s capacity is taken into account when the order contains multiple nodes with the same work center.

#### Price alternative for purchased parts when registering and reporting orders
This system setting determines which price alternative (price per unit) should apply to purchased parts when registering and reporting orders. This is used for costs for the Post-calculation. The default price alternative in Pre-calculation and WIP value are also affected. The default option here is the standard price.

#### Price list for purchased parts when registering and reporting orders
This system setting determines which price list should apply if the setting above has been set to price list.

#### Price alternative for stock driven parts when registering and reporting orders
This system setting determines which price alternative (price per unit) should apply to manufactured parts that are stock driven during order registration and reporting. This is used for costs for the Post-calculation. The default price alternative in Pre-calculation and WIP value are also affected. The default option here is the standard price.

#### Price list for stock driven parts when registering and reporting orders
This system setting determines which price list should apply if the setting above has been set to price list.

#### Increase remaining qty for following operations when excess reporting
This system setting determines if the remaining quantity should be increased for following operations when excess reporting. If the remaining quantity is instead decreased for an operation, the remaining quantity always decreases for the following operations.

#### Use fixed delivery day on subcontracts
This system setting determines if a fixed delivery day should be used for subcontracts. The fixed delivery day is entered for the supplier in the Supplier register procedure. The fixed delivery day is taken into account during, for example, order registration, net requirement calculation, and the calculation of new finish date.

#### Replan finished operations when replanning orders
This system setting determines if finished operations and parts should be replanned if the order is replanned. If this system setting has not been activated, then finished operations and parts (where the remaining quantity is zero) will remain when the order is replanned.

#### Replan previous operations when replanning orders from an operation
This system setting determines if previous operations (with lower operation number) should be replanned when a later operation (with higher operation number) is replanned. This applies when the re-planning is made from orders/work centers and the priority planning.

#### Check quantity on order against quantity/package
This system setting determines if a check should be made to make sure that the order's quantity is a multiple of the part's quantity/package entered in the Qty/pkg field under the Manufacturing tab in the Part register procedure. If the entered quantity on the order is not a multiple of the part's quantity/package a warning appears in the Quantity field. This applies to the procedures Register manufacturing order and Manufacturing order suggestion.

#### Suggest remaining quantity when reporting
This system setting determines if the remaining quantity should be suggested when reporting manufacturing orders.

#### Suggest planned time for reported quantity
This system setting determines if the planned quantity should be suggested when reporting manufacturing orders.

#### Check if reported quantity is greater than previous operation's reported quantity
This system setting determines if a check should be made in the Report operation procedure to see if the reported quantity is greater than the previous operation's reported quantity. The available options are:
- Inactive – no check will be made.
- Warn – a warning will be displayed. In the validation window you will see that the reported quantity is greater than the previous operation's reported quantity.
- Block – a block will be displayed. In the validation window you will find the same information as mentioned above. In this case you cannot save the reporting.

#### Check against remaining quantity of material when reporting final operation as finished
This setting determines if a check should be made in the Report operation and Report pick list procedures to see if a material has a rest quantity larger than zero when reporting the final operation as finished. That is, when the order reaches status 4 (Finished). The available options are:
- Inactive – no check will be made.
- Warn – a warning will be displayed. In the validation window you will see that there is material with remaining quantity.
- Block – a block will be displayed. In the validation window you will find the same information as mentioned above. In this case you cannot save the reporting.

#### Deduct remaining quantity of operation and material at rejection
This system setting determines how the remaining quantity on operation and material should be managed at rejection on operation.

#### Show dialog for serial number even though everything has already been linked
This system setting determines if a dialog box should be displayed in which you link a serial number of a manufactured part to traceable material. This applies in cases where there is a suggested serial number for the manufactured part and all materials have suggested batch numbers/serial numbers. This will also apply if there only is one remaining serial number for a manufactured part and there is only one material left to link. If you do not want to show the dialog box, you deselect this system setting.

#### Activate the document tab after reporting
This system setting determines if the Documents tab should open automatically. Under this tab you can print transport label after you have saved an operation reporting (with transfer to stock).

#### Orders generated from max. quantity (without linked requirement)
With this setting you decide if manufacturing orders with a quantity greater than the maximum quantity entered for the part, should be divided into multiple nodes on the same order or if it should be divided into multiple orders. The available options are:
-   
Use one order number – Multiple nodes will be created on one order.
-   
Use multiple order numbers – The quantity is divided into multiple manufacturing orders.

#### Include revision files to subcontract purchase orders
With this system setting you decide if files linked to a part revision should be included/attached when e-mailing subcontract purchase orders in the Subcontract documents/Shipped and Print purchase order procedures.

#### Printing of linked files
Here you decide a general printing order regarding linked files (for order, part node, operation, and material) which are printed together with order documents (traveler, operation document, material document) for manufacturing orders and maintenance orders. This setting is also available on user level in the Users procedure, and it will in that case override this system setting. You can also override the setting per printout in the Register manufacturing order, Print manufacturing order, and Register maintenance order procedures. The available options are:
- Do not print – Linked files will not be printed.
- Print last – Linked files are grouped together and will be printed last after the order documents for all orders that are being printed.
- Print by order number – Linked files are grouped together and are printed last after the order documents, per manufacturing order or maintenance order.
- Print by part – Linked files are grouped together and are printed last after the order documents, per part node in the order.
- Print by operation – Linked files are grouped together and are printed last after the order documents, per operation in the order.

#### Mandatory cause code if time used exceeds planned time (in %)
This setting decides if it should be mandatory to enter a cause code when you report a direct work item/operation as finished in the Recording terminal (Windows client and mobile client), Report manufacturing order or Report operation procedures. It becomes mandatory if the time used exceeds the planned time with this percentage or more. This validation is made using the planned time for the reported quantity.
If you enter zero (0.00) percent here, it means that it will not be mandatory to enter a cause code.
For batch recording it is the time used in total for all direct work items that is referred to. If the percentage results in a mandatory cause code for a batch recording, it is sufficient if the operator enters the code for one of the work items in the batch. This code is automatically copied to all other work items (rows) in the batch.
Cause codes for time loss and time gain must first be registered under the Time used tab in the Cause codes procedure. In the that procedure you also choose if it should be mandatory to enter a comment in connection with selecting the cause code when reporting.
Cause codes and comments, if any, which have been entered can be viewed in the Post-calculation, Manufacturing order log, and in Order info.

#### Mandatory cause code if time used is less than planned time (in %)
This setting decides if it should be mandatory to enter a cause code when you report a direct work item/operation as finished in the Recording terminal (Windows client and mobile client), Report manufacturing order or Report operation procedures. It becomes mandatory if the time used falls below the planned time with this percentage or more. This validation is made using the planned time for the reported quantity.
If you enter zero (0.00) percent here, it means that it will not be mandatory to enter a cause code.
For batch recording it is the time used in total for all direct work items that is referred to. If the percentage results in a mandatory cause code for a batch recording, it is sufficient if the operator enters the code for one of the work items in the batch. This code is automatically copied to all other work items (rows) in the batch.
Cause codes for time loss and time gain must first be registered under the Time used tab in the Cause codes procedure. In the that procedure you also choose if it should be mandatory to enter a comment in connection with selecting the cause code when reporting.
Cause codes and comments, if any, which have been entered can be viewed in the Post-calculation, Manufacturing order log, and in Order info.
