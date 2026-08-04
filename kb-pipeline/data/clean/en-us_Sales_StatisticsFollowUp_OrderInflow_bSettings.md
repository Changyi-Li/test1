### Settings
View

#### Include orders from
You can select which order rows to include in the list. Here you based it on where the order row in question was created: at customer order registration, at delivery reporting, or at invoice registration.

#### Include preliminary customer orders
With this setting you determine if preliminary customer orders should be included in the list.

#### Show alloy cost
With this setting you decide whether or not rows with alloy costs should be displayed in the list.

#### Show order inflow for deleted customer orders
With this setting you decide if deleted customer orders should be included in the list. This box is checked by default. If order inflow records did not become deleted at the time of deleting the customer orders, these will be shown if this setting activated. If order inflow records were deleted when the customer orders were deleted, these orders will never be shown, regardless if this setting is activated or not.

#### Show called order rows
With this setting you determine if customer order rows called from a blanket order should be shown in the list. When this setting is not marked, customer order rows that are called from blanket order are hidden. In that case a total of Order inflow and Order inflow – Blanket order will result in the total order inflow.

#### Show foreign currency
With this setting you determine if price, setup price, and value on the order rows should be displayed both in the currency of the order and in the company currency.
Price alternative

#### Convert price each according to rate type
With this setting you determine if "price each" in foreign currency should be converted to the present exchange rate in the Currencies procedure. If the checkbox is not checked, the exchange rate saved on the record will be used instead. Which rate type to use is selected in the field below.

#### Rate type
The rate type you select here is used to convert "prices each" and price lists in foreign currency to the now applying exchange rate for the selected rate type. The default rate type is From customer/order type. You register rate types in the Currencies procedure.
Unit

#### Unit according to
Here you decide which unit should be used to display ordered quantity, delivered quantity, and remaining quantity. Applies to the Detailed and Total list types. The following units can be chosen:
- Customer order row – selected by default
- Standard unit
- According to usage – If you choose the option "According to usage" you must select which unit in the setting below.

#### Unit usage type
Here you select which type of alternative unit should be used for the calculation. The following options are available: Material withdrawal for manufacturing order, Purchase order, Report arrival, Customer order, Report delivery, Stock count and stock reporting, Statistics, and Pack for delivery.

#### Price alternative for CM/CR
