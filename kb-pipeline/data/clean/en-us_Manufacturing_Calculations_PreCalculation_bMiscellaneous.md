### Miscellaneous
Here you find additional settings for the pre-calculation. These settings are available for the list type New calculation.

#### Quantity if order qty is missing
Here you enter the lot size – according to which the pre-calculations should be made – for those parts that are missing an order quantity. Under the List tab, before you run the calculation, you will see the calculation quantity either as order quantity or the quantity entered in this field. If order quantity is missing for parts, the quantity will be displayed in red color. When the calculations are saved, this lot size can be configured as order quantity for those parts. If you use alternate BOM and routing, it will be taken into consideration, if quantity terms have been entered in the BOM and routing for the parts included in the pre-calculations.

#### Consider max. quantity
The calculation is performed with maximum quantity and not with EOQ. If you deactivate this setting, the calculation is performed with EOQ even if there is a maximum quantity registered for the parts.

#### Configuration
This setting is available if you have the option Product configurator. Then it is possible to here select if it should be possible to configure parts before the pre-calculation is calculated. The default setting here is Complete. If you select the Complete alternative, the Configuration column (Conf.) will be displayed when you load the list. In this column there is a button to configure parts. The button is shown with this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) when the part has to be configured. By clicking this button you access a configuration window where you can configure the part before you run the calculation. When you confirm the configuration using the button Confirm ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) in that window, the symbol on the button will change ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png), to illustrate that the part has a valid configuration. This setting is appropriate to use if certain parts in the configuration are included in the price of a "standard product".
The option No is suitable if each selected part in the configuration should have its own calculation.

#### Comparative price
Here you can select a price alternative in order to compare the result of the calculation to another price for the parts. It is the same price that is used to calculate CM The contribution margin (CM) is the difference between the standard price and the sales price. and CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. % in relation to the actual costs per unit.

#### Price list
Select a price list for comparative price. This field will become available if you have selected Price list as comparative price.

#### Rate type
In this field you select the rate type to use when valuing purchased parts based on a price list in another currency. This field becomes available if you have selected a price list in a different currency. Rate types must first be registered and activated in the Currencies procedure. The default type is determined by the system setting Default rate type.

#### Print result tabs
In this field you select which lists that you want to include when printing to a printer. By default, only the Summary list is selected for printout.

#### Terms
By clicking the Terms button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can enter different default terms in the BOM and routing to be used in the calculation of the selected parts.
