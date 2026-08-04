### General
Transport and pick-up

#### Transport date
Today's date is suggested by default, but it is possible to enter a different transport date in the field.

#### Automatic booking
With this setting you decide if the pick-up should be booked in nShift Delivery.

#### Pick-up date
Today's date is suggested by default, but in the field it is possible to enter a different date for when the shipment should be picked up. For the integration with Logtrade you must also enter a text in the Text for the booking in order for the information about pick-up date to be exported to Logtrade. This is due to the pick-up date not being a separate field in Logtrade, but is handled as a part of the booking text.

#### Earliest/Latest pick-up time
The time span you create by entering these fields, will be the interval within which the pick-up can be made. If this information is entered for the supplier, these values will be loaded. For the integration with Logtrade you must also enter a text in the Text for the booking in order for the information about earliest and latest pick-up time be exported to Logtrade. This is due to the earliest and latest pick-up time not being separate fields in Logtrade, but is handled as a part of the booking text.

#### Delivery date
Here you can enter a delivery date for the shipping agents and shipping services which require this information for shipments.

#### Delivery time
Here you can enter a delivery time for the shipping agents and shipping services which require this information for shipments.

#### Text for the booking
Here you enter an optional text for the booking, for example an instruction regarding the booked pick-up. If a text for the booking has been entered for the supplier, the text will be loaded form the Supplier register.

#### E-mail address to goods sender
The person who takes care of the pick-up can send a confirmation to the goods sender via this address. If an e-mail address to goods sender has been entered for the supplier, this address will be loaded form the Supplier register.

#### Delivery method
The delivery method is loaded from the selected source of information, but you can select a different method in this field. A validation in the field warns you if the delivery method is not linked to the selected supplier.

#### Shipping agent
Here you select the shipping agent for the shipment. The name is shown to the right. The information is loaded from the selected source of information. If a selected pick list is linked to a shipment, the shipping agent in question is shown here. Information about the shipping agent's identity and address is also exported to complex dispatch advice via EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system..

#### Shipping service/Shipment template
Here you select the shipping service and the shipment template for the shipment. You can select among what is registered for the shipping agent in the Shipping services procedure. If the shipping agent does not have any shipping service or shipment template registered in the Shipping services procedure, then these fields are inactive.

#### Complement/Print in nShift
If the selected shipping agent is linked to nShift Delivery or nShift Delivery for export, then this setting is available. Here it is possible to mark that the shipment should be complemented or printed in nShift.
This setting can also be activated by default. This is configured for the shipping service in the procedure Shipping services. It is possible to activate/deactivate the setting as long as the shipment has not reached status 4 (Exported).
This setting means that you export the shipment to nShift and that you can later complement it and print the shipping documents from your account on nShift's website. In nShift, these shipments are referred to as "stored printings".
In order for these shipments to become complete in Monitor ERP, you should in the Update shipment status procedure activate a scheduled loading of printed shipments. The shipments will then be complemented in Monitor ERP with for example the shipping agent's shipment number, shipping agent's package number, and gets the status updated from 4 (Exported) to 5 (Booked/Printed). In that procedure you can also load a list of shipments to check that they are complete.
Additional services
The Additional service button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is available if the selected Shipping service in the shipment has additional services registered (applies to nShiftDelivery). By clicking this button you see the additional services that should be include in the shipment. You select among the additional services registered for the shipping service.
The additional services where Active is checked will be included in the shipment.
For certain additional services, you might be required to enter extra information in one or several of the extra fields 1-5. In that case, this is described in the Lead text column for the affected additional service.
Miscellaneous
The settings configured under the button Miscellaneous ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) are loaded by default from the selected shipping agent in the shipment, but it is possible to change these for a specific shipment.

#### Delivery instructions
The delivery instructions is loaded from the customer order you selected in the Source of information box. You can change the delivery instruction for a specific shipment.

#### Number of EUR pallets
Here you enter the number of EUR pallets included in the shipment.

#### Return label
With this setting you decide if a return label should be printed and be included in the shipment.

#### Default shipping document printouts
Here you decide which shipping documents should be printed by default. The available options are Only waybill, Only label, or Both.

#### Warehouse
Applies if the Warehouse option is used. By default you will see the warehouse you are currently working in. When a source of information of the type Customer order/Delivery or Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. has been selected, the selected warehouse will determine which orders and pick lists that can be selected in the Source of information field.
It is possible to change warehouse as long as no source of information has been selected.

#### Sender
By default, the sender is the code entered for the selected shipping service in the shipment. But it can be changed to a different sender (for any of the registered shipping services). Sender is entered for each service in the Shipping services procedure.

#### Consignor address ID (Web-TA)
Here you enter the sender's consignor address in Web-TA that should be exported by default.

#### Pick-up address ID (Web-TA)
Here you enter the sender's pick-up address in Web-TA that should be exported by default.

#### Consolidated shipment
This field is available if the selected shipping agent (freight company) in the shipment is linked to any of the shipping services nShift or LogTrade (what you select as export plugin for the selected shipping agent in the supplier register).
With this field you determine if this shipment should be added to a consolidated shipment. Consolidated shipments get the same Shipping agent's shipment no. when they have been exported. The default option here is No. This means the shipment is not added to consolidated shipment. If you select Yes here for the shipment, you must enter a consolidation key in the next field. It is the consolidation key that adds the shipments to the same consolidated shipment. A default consolidation key can be shown in the field. This is determined by the system setting called Use default consolidation key for shipment.
The field is by default set to Yes with an entered consolidation key, if you have selected a shipping service for the shipping agent in the shipment and that shipping service has activated the setting called Consolidated shipment in the Shipping services procedure.
