### Delivery/Shipping
In this box you enter information regarding delivery and shipping that should be used on the customer order. See the explanation of the information in the help chapter for [Delivery/Shipping](../../Customers/CustomerRegister/bDeliveryShipping.htm) in the Customer register procedure.

#### Delivery rules
By using the button Delivery rules ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) it is possible to make changes of the delivery rules for the customer order in question.
- Apply delivery planning – With this checkbox you decide if delivery planning should be applied for the order. This setting is automatically activated if both the order type and the customer on the order have it activated.
- Apply preliminary pick list – With this checkbox you decide if preliminary pick list should be applied for the order. This setting is automatically activated if both the order type and the customer on the order have it activated.
- Delivery horizon – Here you enter the delivery horizon that applies for the order. It is entered in number of work days. The field is possible to edit if the setting called Apply delivery planning is activated. The value is loaded from the customer on the order. If you leave the field empty, then it is the general delivery horizon which have been entered using the system setting called Delivery horizon which will apply. Please note! Even if the field is deactivated by unchecking Apply delivery planning, the work days in the field will still be taken into consideration. Only an empty field will cause the system setting’s Delivery horizon to be used as backup value.
- Partial delivery – With this setting you decide if partial delivery is allowed order row, on entire order, or not at all. This is loaded from the customer on the order.
- Create delivery note number when delivery planning – With this setting you determine if a delivery note number should be created when a pick list is created and where the order is included via the list type Picking plan, in the Delivery planning procedure. This setting becomes available if the setting Apply delivery planning is activated. This is loaded from the customer on the order.

#### Freight payer
The freight payer is by default loaded from the selected delivery term for the order. You can modify this for the order in question. The alternative you select will affect which customer number at the shipping agent that will be loaded:
- Purchaser pays – With this alternative the number will be loaded from Customer number, shipping agents for the customer on the order. This is for the shipping agent that is linked to the selected delivery method. You cannot change this number in the next field.
- Seller pays – With this alternative the number will be loaded from Customer number, shipping agents in the Company information. This is for the shipping agent that is linked to the selected delivery method. You cannot change this number in the next field.
- Other payer – If this alternative is selected, the next field will become available. You can then enter the customer number used at the shipping agent.
- Incoterms – Internationally recognized rules which describe who has the financial responsibility of the goods during the transport. If this alternative is selected you can, a few fields down, enter a place of terms of delivery.

#### Customer number, shipping agent
Customer number, shipping agent is the goods address number or customer number that the freight payer has got at the shipping agent’s. The setting above determines if you can enter this in the field.

#### Place of terms of delivery
Here you can enter a "Place of terms of delivery". The place of terms of delivery is loaded from the customer register and describes the place or city where the financial responsibility for the shipped goods will pass to another party. You only need this information if the city entered in the delivery address should not apply. To show the place of terms of delivery on documents, you have to activate the document setting Show place of terms of delivery in the Document settings procedure.

#### Transport time
By default, you will here see the transport time entered for the customer. You can change this for the order in question.

#### Transport distance
By default, you will here see the transport time entered for the customer. You can modify the transport distance for the order in question. The transport distance is used for sustainability calculations.

#### Delivery instructions
This instruction is by default loaded from the customer and is displayed on the shipping documents. It can be changed for the order in question.

#### Shipping exceptions
Here you can choose to use exceptions regarding shipping and by this override Shipping service, Shipment template, and you can enter which Additional services should be active for the specific customer order. These values will be used instead of the regular values (loaded from the delivery method of the order) when you create a shipment.

#### Pick instruction
The instruction which you enter here will be printed on pick lists for order. By using the button to the right, you can also link external files to the instruction. These will then be printed automatically when the pick list is printed.
