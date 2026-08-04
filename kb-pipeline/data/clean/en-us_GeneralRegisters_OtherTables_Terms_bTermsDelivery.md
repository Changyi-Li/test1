### Delivery terms
In this table you register delivery terms. A delivery term describes the responsibilities at transport and delivery of the goods. You select a delivery term for a customer and a supplier that will be selected by default on orders and delivery documents.

#### Default
Here you determine if the delivery term should be used by default when registering new customers and suppliers.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Name
Here you enter a name for the delivery term.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Explanation
In this column you can enter an explanation regarding the delivery term. The explanation can be used in case there are multiple delivery terms with the same name. The explanation is displayed in the procedures where you in a field can select delivery term, for example, in the Register customer order procedure.

#### Code
Here you enter a default code for the delivery term using a maximum of 10 characters.

#### Customer order transfer code
Here you enter the code for the delivery term using a maximum of 15 characters. The code is used by the option Customer order transfer in order to match this delivery term with a delivery term in the other company when customer orders are transferred from the sales company to the production company. If the same code is used for a delivery term in both companies, the delivery terms will match.

#### Payer
The payer is the party registered as the payer of the freight. The payer of the freight applies between the shipping agent and my company. This selection determines e.g. the goods address number (GAN) shown on the documents (your or the other party’s). There are four options:
- Purchaser pays – If Payer is set to Purchaser pays, it means that the CO2e emissions form upstream transports will be included in the sustainability calculation (in accordance with the ESRS standard).
- Seller pays
- Other payer
- Incoterms – This option is only selected during third-party integration. Incoterms are internationally recognized rules which describe who has the financial responsibility of the goods during the transport. For export/import of goods, it is especially important to use an Incoterm as delivery term. For an Incoterm it is recommended that you specify "Incoterm" in the name in the name field.

#### Payment reference
If the Payer is set to Purchaser pays, you can here enter a payment reference.

#### Shipping
By using the Shipping button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add shipping agents and their codes for the delivery term. This is entered as an exception from the default code for the delivery term. If you add the shipping agent's code for the delivery term here, it will override the default code of the delivery term. This is used by the integration with nShift and LogTrade.
> Creating shipping services requires certain specialist knowledge. If you need help with this, you should primarily contact a consultant at Monitor ERP System AB. Assistance regarding setting up shipping services is not included in the support and update agreement.

#### Active
With this checkbox you determine if the delivery term should be active.
