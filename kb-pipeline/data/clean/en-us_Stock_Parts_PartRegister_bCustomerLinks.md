### Customer links
In this box you can create, edit, and delete customer links for the part. The number of links here is unlimited. At the bottom of the box you will see the number of customer links.

#### Customer
Here you can select a customer from the customer register by using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature.

#### Price
Here you enter the customer price of the part. It should be entered in the currency of the customer. A minimum of two and a maximum of six decimals will be saved/displayed for the price.
If there is a price formula on the part, the text f(x) will instead be the name of the column. Then the customer price on the part in the configuration is calculated using this formula by multiplying the entered customer price with the result of the formula. Price formulas are entered by using the button Other ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the Configurator box.

#### Price incl. VAT
Here you see the customer price for the part (including VAT) in the currency of the customer.

#### Price calculation (PC)
By using this calculator you can calculate which appropriate price the part should have if you want a specific price including VAT.

#### Price unit
Here you select a unit for the price among the units registered for the part. The standard unit is displayed by default, but it can be changed. The price will be converted based on the conversion factor of the unit.

#### Staggered prices
Using the Staggered prices button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can add staggered sales prices (price ladder) with limit values for quantity, price, and future price. The prices are entered in the currency of the price list and in the part’s unit according to the main row.
| Interval | Limit value, qty | Price | Future price |
|---|---|---|---|
| 1-9 pcs | 1 pcs | EUR 100 | EUR 110 |
| 10-19 pcs | 10 pcs | EUR 75 | EUR 80 |
| 20 pcs or more | 20 pcs | EUR 65 | EUR 70 |
> You must always enter a price in the Price each field on the customer link in order for the staggered price from the customer link to show on the order row. Otherwise the price will be shown as 0.00 on the order row.

#### Setup price
Here you enter the setup price in the customer's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Currency
Here you see the currency of the customer. It is in this currency all the prices are entered for the customer link. If needed, the currency of the link can be changed to any of the currencies registered in the Currencies procedure.

#### Discount
Here you can enter a discount of the price in the link. It can override the discount category's discount on the order.

#### Price date
The date when the price was entered.

#### Contribution margin
Here you can see the contribution margin (CM The contribution margin (CM) is the difference between the standard price and the sales price.) in the company currency. It is the difference between the customer price and the standard price.

#### Contribution ratio %
Here you can see the contribution ration (CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage.) in percent. It is the relation between the sales price and the standard price. For example, if the standard price is 20 SEK and the sales price is 30 SEK, the CR will be 33 %. That is, CR = ((30-20)/30)*100 = 33 %,

#### Net
Here you will see the net customer price. It is the customer's price minus discount, if any.

#### Customer's part number
Here you see/enter the customer's part number for the part in question. It is printed on the quote and order.

#### Price comment
The price comment of the link is displayed when customer order and invoice is created for the part or the customer.

#### Comment
This comment overrides the part's general sales comment on each respective document in the Comment/Files box. This only applies if you have selected to show the comment on these documents in the setting mentioned below called Show comment on.

#### Show comment on
This setting determines on which documents the comment for the customer link should be displayed. The system setting called Show sales comment on, determines on which documents the sales comment should be included by default.

#### Pick instruction
If you have a pick instruction here in the customer link it will override the general pick instruction of the part available in the Shipping box. A pick instruction can be entered for all parts, except for those parts marked with The part is a packaging part in the box.

#### F (PI)
Files for pick instruction. By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
The files can be printed automatically together with the pick list.

#### Valid through
The valid through date indicates for how long the price in the link will be valid. If the date has passed, a warning appears when registering customer orders and invoices for the part or the customer. If there is a future price, a question appears asking if you wish to apply the future price.

#### Future price
Here you enter/see a future customer price of the part. It should be entered in the currency of the customer. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Future price incl. VAT
Here you enter/see a future customer price of the part. It should be entered including VAT in the currency of the customer.

#### Future valid through
The future valid through date indicates for how long the future customer price in the link will be valid.

#### Future setup price
Here you see/enter the future setup price in the customer's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Future setup price incl. VAT
Here you see/enter the future setup price (including VAT) in the currency of the customer.

#### Lead time
Here you see/enter the lead time to the customer. It is shown in work days. This is the lead time that applies to the part for the customer in the link. A check will be made against this date at order registration. This filed overrides the general Lead time Number of days between ordering date and delivery date. Normally used for purchased parts. to customer entered for the part in the Miscellaneous box under the Sales tab.

#### Quantity for lead time
Here you enter the quantity of the part on the order for lead time to customer. It overrides the general lead time quantity entered for the part.

#### GS1 code
Here you see/enter the GS1 code that applies for the link. It overrides the general GS1 code entered for the part.

#### Quantity/package
Does not apply to the Fictitious part type. The Quantity/package indicates the number of parts that fits in a package when the part is sold to the customer in the link. The field is empty by default, which means that one transport label is printed for the entire order quantity during delivery reporting. If you enter a quantity/package, one transport label will be printed for each package that has been delivery reported on the customer order. The quantity is displayed in the unit selected on the main row, but it will be saved in the standard unit. This field overrides the general qty/pkg entered for the part in the Shipping box.

#### Packaging part
Here you can link a packaging part to the customer link. It overrides the general packaging part, if this has been selected for the part in the Shipping box. By using the Lookup feature you can select among the parts for which the setting The part is a packaging part has been activated.

#### Packaging template
Here you can link a packaging template to the customer link. It will override the general packaging template, if such has been selected for the part in the Shipping box. When you have selected a packaging template, the packaging part used to pack the part in, will automatically be entered in the field called Packaging part.

#### Packaging template rows
The Packaging template rows button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) will become available if you have selected a packaging template. By clicking this button you can see the packaging parts included in the template. For these parts you can see level, packaging type, and minimum quantity.

#### Transport label variant
If the part is a packaging part you can here connect a document variant for Transport label – Package structure to the customer link. It overrides the general document variant for the transport label, if such has been selected for the part in the Shipping box.

#### Deviation model
The deviation model is used to analyze delivery schedules. Deviation models are created in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Delivery schedules procedure. [Read more](../../../Sales/DeliverySchedules/BasicDataDeliverySchedules/bDeviationModel.htm) on how deviation models are prioritized.

#### Deviation model definition
Here you can see the deviation model that you've selected.

#### Certificate
Here you decide if the selected product description incl. certificate should be printed when delivery reporting traceable part on customer order to the customer in the customer link. The printouts are made in the Report delivery and Print delivery documents procedures. If you have created several document variants in the Document templates procedure for the Product description including certificate document, you can in the filed choose which document variant you want to use.
When printing product descriptions incl. certificate in the mentioned procedures, you can activate the Use traceability document from customer link setting, if the documents from the customer link should be printed instead.

#### Cumulative quantity, start date
If cumulative reconciliation should be applied for delivery schedules to the customer in the link, you can enter the start date for cumulative quantity of this part in delivery schedules. This date will override the corresponding start date for cumulative quantity which is entered in the Customer register procedure.

#### Cumulative quantity, offset
In situations where cumulative start date cannot be “reset” and the shipped/arrival reported quantity are out of sync, you can offset the cumulative shipped quantity in order to perform a correct cumulative reconciliation.
Cumulative quantity, offset is always shown in the standard unit of the parts. The value in the field can be positive or negative. The standard value is 0 (empty).
The offset value is added to the cumulative value that is shipped. This means that:
- If the offset value is positive, the cumulative quantity that is shipped will increase.
- If the offset value is negative, the cumulative quantity that is shipped will decrease.
- The cumulative offset value is in the part’s standard unit. If the unit used in the delivery schedule differs from the standard unit of the part, the unit will be converted to match the standard unit by applying the conversion multiple.
In the Handle delivery schedules – Sales procedure, there is a column that displays the cumulative offset quantity under the More info button. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png)
