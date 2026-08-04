### Header row

#### Reference number
Here you can load a saved shipment. If it is a new shipment, leave the field empty, and the system will automatically load the next available reference number from the number series.

#### Shipping agent’s shipment no.
You get the shipping agent's shipment number, depending on service, when the shipment has been exported and is booked with the external partner (nShift or Logtrade).
If the shipment is part of a consolidated shipment, it will get the same "Shipping agent's shipment no." as the other shipments in the same consolidation.
If the selected shipping agent in the shipment has Other selected as export plugin (selected in the supplier register), you can manually enter the shipping agent’s shipment number for the shipment. The shipping agent’s shipment number can contain a maximum of 35 characters.
Shipments which have been exported to nShift Delivery or Logtrade with the setting Komplettera/Skriv ut sändning i Ta-system activated, can be updated by using the button called Load shipping agent's shipment number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png). The shipment is then updated with Shipment number as well as the shipment’s Status.

#### Shipping agent's package number
You get the shipping agent's package number, depending on service, when the shipment has been exported and is booked with nShift or Logtrade.

#### Status
The status of the shipment is shown in text in this field. The following status options exist for a shipment:
- Registered – This status means that the shipment has only been saved.
- Exported – This means you have used the setting called Complement/Print in nShift in Register shipment. The shipment is exported to Saved printouts in nShift Delivery where you can complete the registration and print the freight documents. When the shipment is completed at nShift Delivery, you can use the Update shipment status procedure to update the shipment's status to Booked/Printed in the Register shipment procedure.
- Booked/Printed – This status is used when nShift has sent the printout of the transport documents and booked the shipment.
- Must be complemented – This means that some type of information is missing. Check (depending on which integration is used) in nShift Web-TA or Saved printouts in nShift Delivery to see which information you need to enter to go ahead with the shipment.
- Failed shipment – This status means that the export of the shipment failed.
- Shipped – This status can be used if the shipping agent in the shipment has Other as plugin program for export.
If the shipping agent in the shipment has Other selected as plugin for export (configured in the supplier register), then it is possible to change Status between Registered, Booked/Printed, and Shipped for a saved shipment. The purpose is to be able to manually change status when shipments are to be exported via a software other than nShift Delivery or nShift Web-TA. When using nShift Delivery or nShift Web-TA, the status in the shipments is assigned automatically.

#### Price for shipment
Here you can manually enter a price for the shipment, if the shipping agent for the shipment has the Other option configured in the setting called Export plugin (that is, no export to third-party software). The field and the value can be updated regardless of the shipment status. By clicking the Update price button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update_price.png) to the right of the field, you can load the price for the shipment from nShift Web-TA.

#### Picked up
Here you see if the shipment has been picked up. The following options are available:
- Yes
- No
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to the right of the Picked up field, you can enter:
- Picked up date – Here you can enter the date when the shipment was picked up.
- Picked up by – Here you can enter who picked up the shipment, that is, the name of the driver.
- License plate – Here you can enter the license plate number for the vehicle that picked up and transported the shipment.

#### Log
Under the Log button, error/warning messages are shown for shipments sent via nShift Delivery or Logtrade. If there is an error/warning message, this is shown with a warning symbol on the button. If you remove the shipment, the related log entries will be deleted.
