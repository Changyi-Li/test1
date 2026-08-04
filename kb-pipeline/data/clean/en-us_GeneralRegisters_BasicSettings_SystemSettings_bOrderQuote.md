### Order/Quote

#### Check quantity on order/quote against quantity/package
This system setting determines if a check should be made to make sure that the order's or quote's quantity is a multiple of the part's quantity/package entered in the Qty/pkg field under the Sales tab in the Part register procedure. If the entered quantity is not a multiple of the part's quantity/package a warning appears in the Quantity field.

#### Check quantity on order/quote against minimum quantity for warehouse
This system setting determines if a check should be made of the entered quantity on an order row or quote row against minimum quantity for the warehouse on the order row. If the entered quantity is less than the part’s minimum quantity, you will see a warning in the Quantity field. If the warehouse is changed on the order row, the check will be made against the new warehouse when saving.

#### Clear the "Delivery date" when qty is less than part's minimum quantity
This system setting is activated if the Check quantity on order/quote against minimum quantity for warehouse system setting has been set to Yes. Here you decide if the delivery date on order rows should be empty when the order row’s quantity is less than the part’s Minimum quantity.
Order rows without a delivery date are not included in the requirements planning and you cannot create any manufacturing orders or purchase orders based on these order rows. Order rows without a delivery date cannot be delivered.
By activating this setting you get an extra opportunity to check order rows with low or uneconomical order quantity before you start manufacturing or purchasing a part.

#### Check quantity on order/quote against the part's quantity for lead time
This system setting determines if a check should be made of the entered part quantity on an order/quote row against the entered Lead time Number of days between ordering date and delivery date. Normally used for purchased parts. quantity primarily on the affected customer link and secondarily on the part. If the entered quantity is greater than the lead time quantity a warning appears in the Quantity field.

#### Check if the part exists on a valid quote
This system setting determines if a check should be made at the customer order registration to see if the part on the order row already exists on a valid quote to the same customer, that is, the quote has not been finished or converted into an order. If the part is included in a quote, a message appears and you can go to the quote in question.
The purpose of this setting is to observe existing quotes. Perhaps you should turn the quote into a customer order instead of registering a customer order for the part.

#### Fictitious part with price on customer order/quote
If the system setting has been set to Yes a fictitious part will be seen as row type 1 with price on order/quote rows. Included parts will be placed on underlying order/quote rows with the price set to zero. Additional name, purchase comment, and comment on customer link are only displayed for the fictitious part.
If the system setting has been set to No a fictitious part will be seen as row type 4 with price set to zero on order/quote rows. The name of the part is displayed. Included parts will then instead get row type 1 with price on the order/quote rows. Additional name, purchase comment, and comment on customer link are only displayed for the included part.

#### Basis for CM and COGS posting is loaded from fictitious part
This system setting determines that the basis for calculating contribution margin (CM The contribution margin (CM) is the difference between the standard price and the sales price.) and posting cost of goods sold (COGS) will be loaded from fictitious part. If you do not activate this setting, then the basis for the CM calculation and COGS posting will be based on the total of the included parts in the fictitious part and be used on main rows.

#### Merge same material from fictitious parts
If a material (with the same part number) exist on several order rows that belong to several included fictitious parts on a customer order, these material will be merged into one row when activating this setting.
If the setting Show structure when registering orders has been activated for fictitious parts, then these material rows will not be merged.

#### Default delivery date on order rows
- Today – With this option the suggested delivery date will be the same date as the date on the row above when adding a new row in the Register customer order and Register invoice directly procedures. If it is the first row, today's date will be suggested.
- Today + lead time – With this option the date will be set to the delivery date on the row above if the part has no lead time. This also applies to parts on row type 2. If there is a lead time for the part, the delivery date will be calculated for each individual order row based on that lead time.
The lead time for the part is defined as:
1. Primarily it is the Lead time in the customer link (the customer on the order) for the part. This is done regardless of the lot sizing rule applied for the part.
2. Secondarily it is the Lead time to customer (the general lead time under the Sales tab) entered for the part. This is done regardless of the lot sizing rule applied for the part.
3. For a purchased part, the third alternative is the Lead time from the supplier link, otherwise Lead time under the Planning tab. This only applies to purchased parts with the Order oriented control method. For a Stock driven purchased part, the lead time in item 1 and 2 is used. If these are missing, today's date will be suggested.
4. For a manufactured part, the third alternative is the Throughput time The throughput time is the time it takes to manufacture a part, from start of the first operation to finish of the last operation. In principle, it consists of production times, queuing times and setup times. including material procurement, otherwise Lead time under the Planning tab. This only apply to parts with the Order oriented control method. For a Stock driven manufactured part, the lead time in item 1 and 2 is used. If these are missing, today's date will be suggested.
A warning appears if a delivery date is entered on the order row which is within the part's lead time as of today.

#### Manage delivery date in order header
With this setting you determine if the Delivery date field should be displayed under Terms under the Header tab. This system setting is deactivated by default. It makes it possible to change the delivery date for the entire order directly in the order header.

#### Default posting on additional order rows on orders/quotes/invoices
This system setting determines if and how the posting of additional order rows (row type 2) should be made. The system setting is used to assist when posting additional order rows. The alternative No posting is selected by default. You can also select posting according to standard account or that posting should be made according the order row above.

#### Default order type
With this setting you decide if the default order type should be According to user or None. If you leave the order type empty during registration, you cannot save until an order type has been selected. This applies to the following procedures: Register customer order, Register customer agreement, Register blanket order, Register stock order – Sales, and Register quote.

#### Account string will be copied from the part row above
The system setting is used to assist when posting part rows on quotes, customer orders, and invoices. This system setting is deactivated by default. If you activate the system setting, then accounts and posting dimensions such as cost center will mainly be loaded from the posting matrix. If these are missing in the posting matrix they will instead be copied from the part row above. Posting dimensions are only copied from the row above if this is managed by the account. This system setting does not apply to advance rows/in arrears rows on invoicing plans. The posting of these should be loaded from each respective row on the plan.

#### Posting of setup price is set as posting of the part
This system setting determines that the setup price on the order row will be posted in the same way as the part on the order row. If the system setting has not been activated then you must manually configure posting for Setup cost per product group and customer group in each posting group. This is made under the Sales account tab in the Posting matrix procedure.

#### Mandatory posting on order row
During purchase order registration, you can enter a sales account for each order row. This account can be used as assistance when posting customer invoices. This system setting determines if the account field should be mandatory or not on the order row. No is selected by default for this system setting. However, linked purchase order rows are created in the Register manufacturing order or Register customer order procedures. Then a warning appears saying "Account must be entered".

#### Specification on order row
With this setting you decide if the part number and/or part name should be displayed automatically as a specification on quote rows, order rows, and invoice rows. This specification can then be seen in the general ledger after the customer invoice has been recorded. The purpose is to provide additional information about which goods and services have been sold, without having to register Part as a separate dimension for posting.
> For this system setting to take effect, it is required that the Specification checkbox has been marked for the sales account in the Chart of accounts procedure.

#### Number of decimals in price on quote, customer order and invoice
You must at least select two decimals, but you cannot select more than six decimals for unit price. Here you determine how many decimals you want to use (and save in the database) when registering quotes, customer orders, and invoices. This system setting also determines how many decimals that will be shown in the column Price each/Setup price on documents. This system setting also applies to Blanket Order – Sales and Customer agreement.
> If you change the number of decimals in this system setting, already registered order rows will not be affected. The number of decimals on existing order rows will be printed on documents.

#### Number of decimals for calculation costs on quote rows
This system setting determines the number of decimals for calculation costs under the Calculation button on quote rows. You can use a maximum of 10 decimals.

#### Show disposable balance on order row/quote row
When registering customer orders and quotes you can use this system setting to choose if disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. should be shown or not. There are three options for this system setting. These will determines how the disposable balance is calculated: Yes, for delivery date. Yes, for all reservations. Yes, for all reservations and orders.

#### Include part's sales comment as text row on customer orders/quotes
This system setting determines if the part's comment, entered under the Comment button under the Sales tab in the Part register procedure, should be included in quotes and customer orders. The comment will be printed as additional text on row type 4 under each respective quote/order row.

#### Show sales comment on
When registering new parts and when creating a new customer link for a part, this system setting will determine which documents that by default should be marked for printing with sales comment.
If the system setting above has been set to No then this setting will be not be active. This system setting applies to new parts you register. Existing parts are not affected if you make changes to this setting.

#### Include part's additional name as text row on customer orders/quotes
This setting determines if the part's additional names should be printed as additional text on row type 4 under each respective quote/order row.
> Please note! The possibility to include the additional name as text row on order/quote rows can be activated via this system setting but also via a setting in the Document settings procedure. If this has been activated both here and in the Document settings, then there will be duplicates of the additional name on the printout.

#### Handling of credit limit during order registration
This system setting determines if a check should be made of the credit limit during order registration. The check could either result in a warning or a block for order registration when a certain credit amount has been reached. This amount is entered per customer in the Customer register procedure. If you enter zero (0) then no check will be made for the customer in question.

#### Credit limit compared to
If you have activated the system setting above, then here you select to what you want to compare the credit limit. The available alternatives are Order backlog, or Order backlog + accounts receivable, Accounts receivable, or Overdue accounts receivable. Order backlog is excluding VAT VAT is included in accounts receivable.

#### Handling of overdue invoices during order registration
This system setting determines if a check should be made of overdue invoices during order registration. The check could either result in a warning or a block for order registration when overdue invoices exist.

#### Handling of overdue invoices during delivery reporting
This system setting determines if a check should be made regarding overdue invoices during delivery reporting. The check can either result in a warning or a block for delivery reporting when overdue invoices exist.

#### Type of document used when direct printing orders
This setting determines which type of document should be printed when direct printing orders using the print button in the Register customer order procedure. The available alternatives are Order confirmation, Delivery note, and Both.

#### Question when changing delivery date, applies to frozen initial/desired
- No, do not change initial/desired – This option does not provide a question. The initial/desired delivery date will not be changed when the current delivery date is changed on an order row after the "freezing" point is reached.
- No, change always initial/desired – This option does not provide a question. The initial/desired delivery date will be changed when the current delivery date is changed on an order row after the "freezing" point is reached.
- Yes, default: do not change initial/desired – This option provides a question. The initial/delivery date will not be changed by default when the current delivery date is changed on an order row after the "freezing" point is reached.
- Yes, default: change initial/desired – This option provides a question. The initial/desired delivery date will be changed by default when the current delivery date is changed on an order row after the "freezing" point is reached.
The "freezing" point for the desired delivery date is reached when a new order is saved. The "freezing" point for the initial delivery date is reached when the order receives status 2 (printed).

#### Warn if delivery date is within lead time to customer
This system setting determines if a check should be made to make sure that the delivery date on an order/quote row is within the lead time to customer primarily on the affected customer link for the part and secondarily on the part. If the selected delivery date is within lead time to customers a warning appears in the Delivery date field. This check is only made for parts with the control method Order oriented.

#### Handling of "zero price" on row
With this setting you decide what should occur if there is no sales price for a part. The following options are available:
- Inactive
- Warn
- Block
The setting affects the following procedures: Registr quote, Register customer order, Register customer agreement, and Register blanket order – Sales.

#### Warn if order row price differs from imported price
With this setting it is possible to deactivate the warning which indicates a difference between the price each on the order row and the imported price (price from order imported via Monitor-to-Monitor or EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system.).
The following options are available:
- Yes – This is the default option and it will provide a warning if the price each on the order row differs from the imported price.
- Yes, but not if imported price is 0 – With this option you will receive a warning if the price each on the order row differs from the imported price, but will not warn if the imported price is 0 (zero).
- No – Will never provide a warning of price difference.

#### Show delivery date "At customer" on order row/quote row
The Delivery date plus the Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver. is by default the date At customer, that is, when the part on the row should have arrived at the customer's location. However, this can be changed. If you activate this setting you will find the field At customer on the order/quote row. It is suitable to enter the same date here as on the customer's order, if there is another date there for the delivery at customer.

#### Default package type
This system setting applies to packaging parts. If no package type has been entered for a packaging part, the package type selected here will be shown by default on package rows for the packaging part when printing shipping documents.

#### Default goods type
This system setting applies to purchased and manufactured parts. If no goods type has been entered for a part, the goods type selected here will be shown by default on package rows for the part when printing shipping documents.

#### Manage mark-up on quote
This setting determines if quote rows should manage mark-up in percent on standard price to provide a quote price. In addition to the contribution ratio (CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage.) you will also see the contribution margin (CM) for both the quote row and in total for the quote.

#### Load sales price from quote calculation
This system setting determines if the sales price should be updated from the calculation. Otherwise, only the standard price will be saved on the quote row and the sales price is configured as usual (price linked to the customer or price from the part’s price list).

#### Log outgoing e-mail
This system setting determines that an e-mail log will be created, under the Activities tab in the Register quote or Register customer order procedure, when someone sends a quote or customer order via e-mail from one of these procedures.

#### Check customer link for part during order registration
This system setting determines if a check should be made to see if parts on new customer order rows have a customer link.
- No – No check is made.
- Yes – A check is made. If the part has no customer link, a warning appears on the order row.

#### Update/Create customer link when importing customer order (XML)
With this system setting you decide if you want to update/create a customer link for the part when importing customer order from an XML file via Monitor-to-Monitor. In the import window in the Register customer order procedure, it is by default set to update/create customer link for the customer order rows.

#### Warn if contribution ratio is lower than x %
Here you decide if a warning should be displayed if the contribution ratio is lower than the entered value. You activate the setting by selecting Yes and can then enter a warning limit in the next system setting (Warning limit for contribution ratio (%)).
This setting applies to the following procedures:
- Part register
- Register quote
- Register customer order
- Register customer agreement
- Register blanket order – Sales

#### Warning limit for contribution ratio (%)
If the system setting called Warn if contribution ratio is lower than x % has been activated, you can here enter a warning limit in percent. In case the contribution ratio falls below the entered value, a warning will be shown.

#### Comparative price
By using this setting you can work with a Comparative price for quote, customer order, and invoice. The comparative price is shown in the currency of the order. This setting makes it possible to follow up on how the comparative price develops due to currency changes. If you choose the Price list option, you should also select a price list in the setting below.

#### Price list
Here you select the price list that should apply if the price option for Comparative price has been set to Price list.

#### Enable temporarily unlocking "Price each" and "Discount"
This setting makes it possible to temporarily lock/unlock Price each and Discount for all rows on a quote or a customer order. A button displaying a padlock is shown in the function menu in Register customer order and Register quote when the setting is set to Yes. By using this button you can unlock the Price each and Discount fields on all rows.

#### Pre-select "Include" on text rows for customer order (M2M)
Determines which text rows on the customer order should be included when importing via Monitor-to-Monitor. The alternatives are: Yes, No, and Only for new rows.

#### Default delivery schedule type for import (M2M)
Here you can choose which delivery schedule type should be used by default when importing Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. (complete) via Monitor-to-Monitor. Delivery schedule types must first be registered in the Delivery schedule types – Sales procedure.

#### Increment of positions
This setting determines how position numbers will increment on Quotes, Blanket orders – Sales, Stock orders, Customer agreements, and Invoices. The following options are available:
- Ones – 1, 2, 3...
- Tens – 10, 20, 30...
- Hundreds – 100, 200, 300...

#### Recalculate locked positions
When a position number is manually edited, it will be locked. This system setting determines whether locked positions will be recalculated when position numbers are recalculated. The following options are available:
- Yes
- No

#### Position numbers when using "Insert new row"
- Insert position number – Recalculate if no available position number – When a new order row is inserted between two existing order rows, this row will be given a new position number between position numbers that are already being used. That way, you can insert several new rows between the original order rows without them affecting the position numbering of the subsequent rows. If there are no available position numbers left and a new row is inserted, all position numbers will be recalculated.
- Insert position number – Manually add position if no available position number­ – When a new order row in inserted between two existing order rows, the new row will be given a position number between the position numbers that are already being used. That way, you can insert several new rows between the original order rows without them affecting the position numbering of the subsequent rows. If there are no available position numbers left and a new row is inserted, the user must manually enter a position number.
- Recalculate all positions – Each time a row is inserted, all position numbers will be recalculated.
This system setting is used if the status for:
- Quotes, Customer orders, Stock order – Sales, and Blanket order – Sales is equal to or higher than 2 – Printed.
- Customer agreements are equal to or higher than 3 – Active.
- Invoice bases are the equal to or higher than 1 – Registered.
Otherwise the position numbers are recalculated every time a new row is inserted.

#### Function of "Split row" button in Register customer order
This setting determines whether a dialog should open when you click the Split row button. In the dialog you can select the quantity, delivery date, position number (depending on the above system settings) and whether the quantity should be taken from the original row. The following options are available:
- Split, no dialog – This is selected by default. If you choose the Split row button in Register customer order, no dialog opens.
- Split, with dialog – If you choose the Split row button in Register customer order, a dialog opens where you can select quantity, delivery date, and whether the quantity should be taken from the origin row.

#### Position on new row when splitting order row
This determines the position numbering on a new row when you use the Split row function. The following options are available:
- Calculate new position – This is the default option. The system will calculate a new position when the new row is created.
- Same as on original row – If the order has the status Printed or higher, the suggested number position will be the same as on the original row.
