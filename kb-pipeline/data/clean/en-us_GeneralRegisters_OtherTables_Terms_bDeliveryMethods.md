### Delivery methods
In this table you register delivery methods. A delivery method describes how goods should be delivered and which shipping agent to use, if any. You select a delivery method for a customer and a supplier that will be selected by default on orders and delivery documents.

#### Default
Here you determine if the delivery method should be used by default when registering new customers and suppliers.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Name
Here you enter a description of the delivery method. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Transport mode
Here you select transport mode. This is used for customs declarations and also for Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reporting in some EU countries.

#### Code
Here you enter the code for the delivery using a maximum of 15 characters. The code is used by the option Customer order transfer in order to match this delivery method with a delivery method in the other company when customer orders are transferred from the sales company to the production company. If the same code is used for a delivery method in both companies, the delivery methods will match.

#### Shipping agent
Here you link a shipping agent to the delivery method. You can choose from shipping agents that have the supplier role Shipping agent. This is configured in the Supplier register procedure. You then see the name of the supplier in the Name field to the right.

#### Shipping service
Here you link a shipping service to the delivery method. This applies to suppliers that have a registered shipping service and shipment template. Then the following fields for shipping service and shipment template open. You register these in the Shipping services procedure.
> Creating shipping services requires certain specialist knowledge. If you need help with this, you should primarily contact a consultant at Monitor ERP System AB. Assistance regarding setting up shipping services is not included in the support and update agreement. Please contact the Monitor Support Center at Monitor ERP System AB by calling +46 650 766 03.

#### Shipment template
Here you link a shipment template to the delivery method. This applies to suppliers that have a registered shipping service and shipment template. Then the following fields for shipping service and shipment template open. You register these in the Shipping services procedure.

#### Emissions (CO2e)
Here you enter emissions in the unit g/tkm (grams per tonnes-kilometer) for the delivery method. This value is then used to calculate upstream transportations in the sustainability calculations.
> Check what has been entered in the Payer field under the Delivery terms tab to see if transportation will be included in the calculation or not. If Payer is set to Purchaser pays it means that the CO2e emissions form upstream transports will be included in the sustainability calculation (in accordance with the ESRS standard).

#### Active
Here you decide if the delivery method should be active or not.
