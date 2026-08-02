::: {#mc-main-content role="main"}
### The basics of the warehouse function

#### Company information

You register warehouses in the [Company information]{.italic} procedure. When the [Warehouse]{.italic} option is installed, the [Warehouses]{.italic} box appears in this procedure. In this box, you can add the warehouses you want to use in your company. Internal customers and suppliers are linked to the warehouses between which parts are distributed.

[Please note!]{.bold} It is possible to add warehouses, but they cannot be deleted later. So consider this carefully, and make sure you only add the warehouses the company actually use.

#### Internal customers and suppliers

Internal customers and suppliers are added in the [Customer register]{.italic} and [Supplier register]{.italic} procedures. An internal customer is a warehouse which \"purchases\" parts from an internal supplier; which is thereby a warehouse which \"sells\" the parts. This is done using [stock orders]{.italic} (see below).

With the [Internal (stock order)]{.italic} setting, you can specify whether or not a customer or supplier is internal. When this setting is activated, a number of other settings/information become unavailable for the customer/supplier. This is information which is not relevant for stock orders.

Internal customers and suppliers have limitations which mean they can only be selected for stock orders. This means they cannot be selected for regular customer and purchase orders, quotes, inquiries, customer invoices, and supplier invoices. As a result, they cannot be selected in customer links and supplier links for parts either.

#### Stock order

Stock orders are used in order to distribute parts between warehouses. Stock orders work in the same way as regular customer and purchase orders, however, you register them for internal customers and suppliers that are the receiving warehouse and sending warehouse for the order. This means you must always have internal customers and suppliers registered which are linked to the respective warehouses, in order to be able to register stock orders. You can monitor, report, and view information about stock orders in the same procedures as other customer- and purchase orders. However, stock orders are registered in separate procedures called [Register stock order -- Sales]{.italic} and [Register stock order -- Purchase]{.italic}.

When you register a stock order for sales (the customer order) it will always be linked to a stock order for purchase (the purchase order), and vice versa. The linked order is automatically created, regardless of whether or not the user creates the purchase- or customer order first. You could say the stock order for sales \"owns\" the stock order for purchase. The price of parts in a stock order can only be entered on the customer order row. The same price is automatically used on the corresponding purchase order row. The default price is the standard price of the part. Information in the order header of a stock order is synchronized with the linked order. That is, if information is changed in the order header, the same information is also changed on the linked order, regardless of whether the user changes the purchase- or customer order first.

Stock orders are registered with your own order types for customer orders and purchase orders respectively. You register the order types in the [Order types]{.italic} procedure. One order type each is included for customer orders and purchase orders of the basic type [Stock order]{.italic}, when the Warehouse option is installed. If necessary, you can register more order types for stock orders later.

In list procedures, users can select by order type for stock orders, and there are list types for stock orders in certain procedures. This means the user can choose only to view stock orders when working in these procedures.

Stock orders are also managed during requirements planning. The [Requirement calculation]{.italic} and [[Net requirement calculation![Closed](../../../../../Skins/Default/Stylesheets/Images/transparent.gif){.MCHelpControl_Image_Icon height="11" width="16" mc-alt2="Open"}[[ ]{.MCTextPopupArrow}You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts.]{.MCTextPopupBody .popupBody}](#){.MCTextPopup .MCTextPopupHotSpot .MCTextPopup_Open .MCTextPopupHotSpot_ .#text}]{.italic} procedures create suggestions for stock orders (purchase), if a shortage should occur for parts which have a warehouse selected with the setting [Refill from warehouse]{.italic}. This means these parts -- purchased or manufactured -- will be primarily acquired via stock order instead of with a normal purchase order or manufacturing order. Suggestions for stock orders are released for actual stock orders for purchase in the [Purchase order suggestion]{.italic} procedure.

Stock orders are exempted from statistics and forecasts. It is not relevant to include stock orders in the order inflow, sales statistics, purchase statistics, and cash flow forecast. No actual sales or purchase activity is taking place, so the income and costs relating to the stock order should therefore not be included. A stock order is a part balance and its stock value, which are moved from one warehouse to another.

If you want to undo a delivered quantity for a stock order, this is done in the [Undo delivery reporting]{.italic} procedure in the sending warehouse. It is possible to undo delivery reporting, as long as none of the delivered quantity has been arrival reported in the receiving warehouse. That is, it is only possible to undo delivery reporting as long as the entire delivered quantity (delivered at the same time) is in transit, that is, being transported between the warehouses. If a portion of this quantity has been arrival reported, you must firstly undo the arrival reporting in the [Undo arrival reporting]{.italic} procedure, in the receiving warehouse. After that, you can undo the entire delivery in the sending warehouse.

#### Stock value between warehouses

The quantity of parts in the stock order which have been delivered -- but not yet reported as arrived in the receiving warehouse -- is not included in the regular stock valuation in the [Stock value]{.italic} procedure, as the quantity does not exist in any of the warehouses. The quantity is in transit between the warehouses. You can valuate this part quantity in the [Stock value between warehouses]{.italic} procedure. Please note that parts which are clear for arrival reporting at the receiving warehouse are also classed as \"in transit\". You may need to carry out a stock valuation between warehouses if there are long transport times between the warehouses.

If the transport times between the warehouses are very short, for example, when the warehouses are next door to each other on the same factory premises, it may be useful to apply automatic arrival reporting. This means that as soon as the customer order is delivery reported, the [Report arrival]{.italic} procedure opens automatically, so the same user can report arrival of the same quantity directly in the linked purchase order in the receiving warehouse. You can specify whether automatic arrival reporting should be used with a setting for order types of customer orders of the basic type Stock order. If automatic arrival reporting is applied, there will never be any stock value between the warehouses.

#### User

A user is linked to the warehouse in which the person concerned primarily works. This is done in the [Users]{.italic} procedure. This is the warehouse the user will log in to when [Monitor ERP]{.mc-variable .Variables.ProductName .variable} is launched. The name of the warehouse is then shown in the title bar.

A user can temporarily switch between the warehouses registered for the company. This can be done under [Warehouse]{.italic}, in the backstage of the desktop. When you change warehouse here, this will apply in all procedures. A temporary change of warehouse can also be made via the warehouse selector in a procedure (see below). This change of warehouse will only apply to the specific procedure.

Under [Settings]{.italic} -- [General]{.italic}, in the backstage of the desktop, the user can select the [Default warehouses]{.italic} from which to view records. The options available are [All]{.italic} and [Warehouse at login]{.italic}. By choosing the [All]{.italic} setting, the users can view records from all warehouses for which they have viewing permission, at a minimum. [Warehouse at login]{.italic} is the default setting. This means the user will only see records in different procedures from "their" warehouse, selected in the [Users]{.italic} procedure.

#### User rights

User-specific rights, user rights groups, and roles assigned to users are saved per warehouse. For example, a user could be a purchaser in one warehouse and a planner in another. The user may have the right to change, create, and delete records in a procedure within a warehouse, but is only permitted to view records within the same procedure in another warehouse. If the user only has viewing permission, the name of the warehouse is shown in italics in the warehouse selector (see below). When the user only has viewing permission in a procedure where records can be updated, you cannot save the procedure (the [Save]{.italic} button is inactivated).

It is possible to synchronize user rights between warehouses in the [Users]{.italic} procedure. This is used to configure the same user rights in all warehouses for a user. When you choose to synchronize, you get to select which warehouse the user rights should be based on.

If a new warehouse is created in the [Company information]{.italic} procedure, the default setting is to include rights for all users from the warehouse you have chosen to copy from, however, you can choose not to include the rights in the event they are to be uniquely set up for the new warehouse.

#### Warehouse selector in procedures

In procedures handling data which is partly or fully affected by warehouse, there is a warehouse selector on the toolbar. You can use this to temporarily change warehouse for the specific procedure you are working in. The warehouse selector is the button [Warehouses]{.italic} ![](../../../../Resources/Images/button_warehouses.png){.icon} (Ctrl + Q).

In the warehouse selector you can see which warehouses are available, and as a user, which you can choose to view data from. In the warehouse selector you'll see all companies in the system as a heading, and all warehouses in each company are listed under the respective heading. The user will only see the warehouses for which they have permission in the procedure in question. If the user is only permitted to view records in the procedure, the name of the warehouse is shown in [italics]{.italic}.

If the user has temporarily changed warehouse in the procedure or in the backstage of the desktop, or has selected [All]{.italic} as the default warehouses in the backstage of the desktop, the warehouse selector is shown in orange ![](../../../../Resources/Images/button_warehouses_alt.png){.icon} in order to indicate that the user is not working in their warehouse, and that records will be shown from all warehouses. This symbol is also shown for rows containing records belonging to another warehouse, for example, material rows on manufacturing orders.

There are three variants of this warehouse selector:

- Variant 1 is found in the procedures in which the user can choose a warehouse to work with. The user can only select one warehouse at a time. This variant is used in the [BOM and routing]{.italic} procedure, for example.
- Alternative 2 is found in the procedures in which the user can both select a warehouse to work with, as well as choose to show records from the other warehouses. In the warehouse selector, the user can choose a warehouse as well as select the warehouses from which records will be shown in the procedure. This variant is used in the [Part register]{.italic} procedure, for example, in which the selected warehouse determines the warehouse to work in and the warehouses that have been selected to view determine the other warehouses from which records are to be shown.
- Alternative 3 is found in procedures in which the user can only choose to view records from one or more warehouses. In this warehouse selector, the user can select the warehouses from which to view records. This variant is mainly used in list procedures: In the [Operation list]{.italic} procedure, for example, where the user can select operations that belong to certain warehouses.

Subcontract work centers do not have to belong to a warehouse -- they will be displayed regardless of the warehouses from which the user has chosen to show records.

#### Warehouse in records

In certain single-record procedures, such as [Register purchase order]{.italic}, a warehouse is chosen for an order using the [Warehouse]{.italic} field. This field is found in the [Miscellaneous]{.italic} box under the Header tab. All records such as orders, customer invoices, quotes, and inquiries are linked to a warehouse via this field. There is no warehouse selector in the toolbar within these procedures.

In the [Register customer order]{.italic} procedure, you'll also find the [Warehouse]{.italic} field on the order rows. This means it is possible to have customer order rows linked to warehouses other than those in the customer order.
:::
