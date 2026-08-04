### Supplier links
In this box you can create, edit, and delete supplier links for the part. The number of links here is unlimited. You can also create multiple links for the same supplier, but in that case, the field Supplier's part number must differ. At the bottom of the box you will see the number of supplier links.

#### Default
In this column you will see/indicate which supplier link will be selected by default. The first link created will be the default one, but this can be changed if several links have been created.

#### Supplier
Supplier number is selected from the supplier register. By using the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature you can search the supplier register. The name of the supplier is shown in the Name field.

#### Receiving inspection
If receiving inspection is entered on the supplier link, it will override any receiving inspection entered on the part and on the general receiving inspection entered on the supplier in the Supplier register. The following options are available:
- No – Receiving inspection will not be applied.
- Yes – Receiving inspection will be applied for the supplier link. You configure settings for this via the Receiving inspection settings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
- Interval – Variable receiving inspection will be applied for the supplier link. You configure settings for this via the Receiving inspection settings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).

#### Receiving inspection settings
Here you configure settings receiving inspection settings if you have receiving inspection settings on the supplier link.
- From – If Receiving inspection is set to Yes or Interval, on the supplier link, this field becomes available and today's date is suggested. Here you can select a date from when the receiving inspection should be applied for the part.
- To – If the Receiving inspection is set to Yes or Interval, on the supplier link, this field becomes available. Here you can select a date to when the receiving inspection should be applied for the part.
- Instruction – If the Receiving inspection is set to Yes or Interval, this button becomes available. Here you enter an instruction regarding the receiving inspection. The text you enter here will be shown to the person performing the inspection. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).
- Inspection template – By selecting an Inspection template, you configure settings regarding variable receiving inspection. Inspection templates first have to be created in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure.
- Level – Level shows the current inspection level of the inspection template. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) buttons you can step up/step down the current level in the inspection template. You can see the settings on each level in the inspection template.
- Number of arrivals – Here you can see the number of reported arrivals.
- Completed inspections – Here you can see the number of performed inspections on the part. By using this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) you can reset the number of performed inspections to 0.00. If an inspection template is selected, the value for Frequency is loaded from the first row in the template. This cannot be updated. When the next level in the template has been reached, the value is loaded from the inspection template.
- Inspection frequency – How often a inspection should be carried out.
- Revert back to previous level – Activated when the inspections should revert back to the previous level.
- No. of inspections after nonconformity – With this setting you determine how many inspections should be carried out after a reported nonconformity.

#### Distributed
If the supplier is included in distributed purchase, the checkbox is this column will be activated. Purchase distributed among suppliers is configured by using the Distribute purchase button in the Miscellaneous box under the Purchase tab.
> Please note that Distributed purchase cannot be used together with maximum purchase order quantity, regardless of whether it’s in the Planning tab or the Supplier link.

#### Price
Here you enter/see the current purchase price of the part. It is entered in the supplier's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Price including VAT
Shows price including VAT.

#### Price calculation (PC)
By using this calculator you can calculate which appropriate price the part should have if you want a specific price including VAT.

#### Price unit
Here you select a unit for the price among the units registered for the part. The standard unit is displayed by default, but it can be changed. The price will be converted based on the conversion factor of the unit. This unit only determines in which unit the price is entered. It will not be used as unit on the purchase order. This is instead configured under the Usage button in the Units box under the General tab.

#### Staggered prices
Using the Staggered prices button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can add staggered sales prices (price ladder) with limit values for quantity, price, and future price. The prices are entered in the currency of the price list and in the part’s unit according to the main row.
| Interval | Limit value, qty | Price | Future price |
|---|---|---|---|
| 1-9 pcs | 1 pcs | EUR 100 | EUR 110 |
| 10-19 pcs | 10 pcs | EUR 75 | EUR 80 |
| 20 pcs or more | 20 pcs | EUR 65 | EUR 70 |

#### Setup price
Here you enter the setup price in the supplier's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Currency
Here you select the supplier’s currency. It is in this currency all the prices are entered in the supplier link. If needed, the currency of the link can be changed to any of the currencies registered in the Currencies procedure.

#### Discount
Here you can enter a discount of the price in the link. It can override the discount category's discount on the order.

#### Price date
The date when the price was entered.

#### Net price
The net price displays the comparative price in the supplier’s currency.

#### Comparative price
Here you will see the purchase price in the company currency and in the standard unit. The formula for comparative price is: Purchase price converted to the standard unit - Discount + Setup price ∕ Order quantity. The purpose of the comparative price is to be able to compare the price per piece from different suppliers.

#### Supplier's part number
Here you enter the supplier's part number for the part. This will be printed on the inquiry and order. The supplier's part number is also used when grouping the part on delivery schedules you can send to the supplier.

#### Brand
Here you see/enter the part's brand. This is displayed under the Price alternative ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button on inquiry rows and purchase order rows.

#### Price comment
If you enter a price comment on the link, this comment will be displayed when a purchase order is created for the part and the supplier.

#### Comment
Here you see/enter comments for the supplier link. This comment overrides the part's general purchase comment for each document in the Comment/Files box. This only applies if you have selected to show the comment on the documents in question in the setting below called Show comment on.

#### Show comment on
This setting determines on which documents the comment should be displayed. The system setting called Show purchase comment on, determines on which documents the purchase comment should be included by default.

#### Lead time
Here you see/enter the lead time from supplier in work days. This lead time applies to the part from the supplier in the link. That is, the time it normally takes from when the part is ordered until it is available in the stock. The field overrides the general lead time of the part that has been entered in the Basic information box under the Planning tab.

#### Valid through
The valid through date indicates for how long the price in the link will be valid. If the date has passed, a warning appears when registering purchase orders for the part or the supplier. If there is a future price you will also receive a question regarding if it should be used.

#### Future price
Here you enter/see the future purchase price of the part. It is entered in the supplier's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price. If the future price is 0,00, the calculation procedures (Pre-calculation, Post-calculation, and WIP value) will use the current purchase price instead. The system setting Automatically transfer future price to price determines if purchase orders created after the expiration date will automatically receive the new price if the supplier link has a price that has expired and there’s a price entered in the column Future price. Price in the supplier link will also be updated with the new price.

#### Future valid through
The future valid through date indicates for how long the future purchase price in the link will be valid.

#### Future setup price
The future setup price is shown in the supplier's currency. A minimum of two and a maximum of six decimals will be saved/displayed for the price.

#### Alloy cost
With this setting you indicate if the alloy cost of the part should be included on purchase orders to the supplier.

#### Quantity/package
In this column you enter/see the quantity per package, that is, the number of parts that fits in a package when the part is purchased from the supplier in the link. The field is empty by default, which means that one transport label is printed for the entire order quantity during arrival reporting. If you enter a quantity/package, a transport label will be printed for each package that has been arrival reported on the purchase order. The quantity is displayed in the unit selected on the main row but it will be saved in the standard unit. This field overrides the general qty/pkg entered for the part in the Miscellaneous box.

#### Maximum order quantity
Maximum order quantity shows the maximum order quantity allowed for this supplier. The value here overrides the value entered in the Maximum quantity on purchase order field in the Planning tab. If you are using purchase order suggestions and the maximum order quantity is exceeded, orders will be created based on the maximum order quantity that has been entered. If you create purchase orders manually and the maximum order quantity is exceeded, a warning is displayed.

#### Part in delivery schedule
With this checkbox you decide if the part should be included in delivery schedules to this supplier. This means that purchase orders/purchase order suggestions with this part will be included by default in the delivery schedules sent to the supplier.

#### Cumulative quantity, start date
Here you see/enter from which date the arrival reported quantity of the part from this supplier should be added together. The date and the cumulative quantity are shown on delivery schedules. A general cumulative quantity's start date can also be entered for the supplier, but that will be overridden by the date in the supplier link.

#### Dock
Here you see/enter the dock to which the delivery should be made from this supplier. This is often used on delivery schedules.

#### Storage
Here you see/enter the storage to which the delivery should be made from this supplier. This is often used on delivery schedules.

#### Material type
Here you select a material type for the part in the supplier link. You register material types in the Basic data – Sustainability procedure.

#### Emissions
If you selected a Material type in the field above, the general emission factor registered for the material type will be loaded. These values are loaded from the Basic data – Sustainability procedure. You can also enter own values here if you have received exact values from a supplier.

#### Remote configured
This setting is available if the options called Customer order transfer and Product configurator are installed in Monitor ERP. This setting is used for the default supplier link of the production company, in combination with a transfer profile for customer order transfer in the sales company. The transfer profile should have the same supplier (the production company) selected. This setting indicates that the part has a configuration registered with the supplier and determines that the configuration on the part in the production company is used when configuring customer order rows on the part in the sales company.
