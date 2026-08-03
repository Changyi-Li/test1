### Standard price

#### Current
Each part can have one current standard price per unit. The standard price is always entered in the part's main unit and in the company currency. The standard price is by default 0,00 when a part is created. Standard prices are saved with a minimum of two and a maximum of six decimals. Normally, the standard price is entered manually for parts of type Purchased, and calculated via pre-calculation for other part types.
The current standard price for manufactured parts is validated against an active calculation. If the standard price is entered manually and differs from the calculation, the price is shown in red font.
If there is a price formula on the part, a formula symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png) is shown to the right of the field. Then the standard price on the part in the configuration is calculated using this formula by multiplying the current standard price with the result of the formula. Price formulas are entered by using the button Other ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the Configurator box.
If the system setting Block stock reporting if the part has no standard price is activated and standard price is missing for parts which are stock updated, the following message is shown: "Standard price is not entered. Part will be blocked from stock transactions". The part will then be blocked for all types of reporting in and out of stock, as well as stock count (this also applies to parts that are tools).

#### Future
The same rules apply for the future standard price as for the current standard price, but no validation will be made against an active calculation. If the future standard price is 0,00, the calculation procedures (Pre-calculation, Post-calculation, and WIP value) will use the current standard price instead.

#### Standard price log
Under the Standard price log button you see a log containing old standard prices. Regardless of where the standard price is changed it will be saved in this log.
Read more about [part prices](../PartPrices.htm) in Monitor ERP.
