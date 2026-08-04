### Units
In this box you can add units and conversion factors. You set one unit as default. You can also choose usage for each unit.

#### Default
Here you set the unit as the standard unit. Other units that you register in the table will be alternative units.
If there is a BOM and routing for the part (operations or material) or if the part is included in a material list in a BOM and routing, then you cannot select another default unit for the part. In that case you must use the button Change default unit ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) on the function menu in order to change the default unit. The button is available for users who are authorized to change default unit on parts.
If you change the default unit, the part's quantity and price are recalculated in all logs, balances, orders, material rows, and operation times in BOM and routings, etc. This way the values will correspond with the new default unit. If the part has partial quantities, the partial quantity's quantity will be recalculated for manufacturing order and in the stock transaction log, when changing the default unit. But for customer orders, purchase orders, and stock orders, the partial quantity's quantity will not be recalculated.
When changing the default unit you can choose if the price should be adjusted for supplier links and customer links. To adjust the price for the links that are using the unit, you should activate the setting called Change price on supplier and customer links.
> Please note! Rounding errors might occur on the last decimal when changing default unit. If you use the option Product configurator, formulas for included quantities will not be recalculated if the unit is changed for a main part.

#### Unit
You can register as many units as you want for a part. The units that are not marked to be the standard unit becomes alternative units. Units are selected from a list, and they must first be registered in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure.

#### Conversion factor
In this column you enter a conversion factor. It is used to show the relation between the alternative unit and the standard unit. The factor is entered as "standard unit divided with alternative unit". Default conversion factor is 1.00 and can be entered using a maximum of six decimals. The conversion factor cannot be negative.
> Before you change a conversion factor you should review existing customer orders in order to see if you have promised the customer one quantity and then deliver in another quantity. This is especially important if you use standard unit on the customer order but deliver using alternative unit.

#### Standard price per unit (Std price/unit)
Here you see the alternative standard price, that is, Conversion factor x Standard unit.

#### Unit usage
By clicking this button you get to select when an added unit should be set as default. This button is activated if two or more units have been added to the part. The available alternatives are: Material withdrawal for manufacturing order, Purchase order, Report arrival, Customer order, Pack for delivery, Report delivery, Stock count and stock reporting, and Statistics. Regarding statistics, this unit will be shown for the parts if you have activated the setting Use unit for statistics in the invoicing log
