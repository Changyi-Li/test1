### Service
Under this tab you add the shipping services that should be used for the selected shipping agent.
It is also possible to copy an existing service by using the button Copy row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) (Ctrl + Shift + C) on the function menu. Any additional services will also be copied.

#### Service
Here you enter an internal name of the service.

#### Code
Here you enter the shipping agent's code for the service.

#### Shipment template
Here you enter a shipment template that you want to link to the service. Shipment templates must first be registered under the Template tab.
Specific settings for Pacsoft Online, nShift Delivery, LogTrade:
These settings exist if the shipping agent is linked to any of the following export plugins: Pacsoft Online, nShift Delivery, or LogTrade. If the shipping agent is linked to nShift Web-TA, there are specific settings under the Template tab.

#### Integrated printer queue
Applies to LogTrade. Here you enter a name for the printer queue that will be used for printouts.

#### Options
By using the Additional services button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add additional services in the shipping service that should be possible to select in shipments with this shipping service. You can also set the additional service as Default. Then it will automatically be added to shipments. When you have added an additional service, this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png) will be shown on the button instead.
If the shipping agent is connected to nShift Web-TA, you select the additional services via different "templates" in the nShift Web-TA account. You can register shipment templates for these additional services under the Template tab. And then you link a shipment template to each respective nShift Web-TA shipping service.

#### Sender’s ID
Here you can enter an ID number for the sender. You can also leave this field empty. 0 (zero) is entered by default for new shipping services.

#### Use Sender's ID
- If you activated this setting the sender's name, address, and contact information field will be emptied in the file (the API call).
- If you activated this setting it means nShift Delivery will use the sender based on the "quick ID" (the sender’s ID).
- If you have not activated this setting, nShift Delivery will use the sender's name and address form the file.

#### Sender/Warehouse
If you use the Warehouse option, you can by clicking the Sender/Warehouse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) enter a sender ID per warehouse. This will then override the general sender ID entered in the previous field.

#### Consolidated shipment
Here you decide if shipments using this shipping service by default should be added to a consolidated shipment. The field called Consolidated shipment is by default set to Yes in the shipments. And the Consolidation key in the shipments you either use the customer number or today's date. This is determined by the system setting called Consolidated shipment.

#### Complement/Print in nShift
Applies to nShift Delivery. Here you decide if shipments in this shipping service by default should be complemented or printed in nShift.
The setting can also be activated/deactivated for specific a shipment in the Register shipment procedure as long as the shipment has not received status 4 (Exported).
This setting means that you export shipments to nShift and that you can later complement them and print the shipping documents from your account on nShift's website. In nShift, these shipments are referred to as "stored printings".
In order for these shipments to become complete in Monitor ERP, you should in the Update shipment status procedure activate a scheduled loading of printed shipments. The shipments will then be complemented in Monitor ERP with for example the shipping agent's shipment number, shipping agent's package number, and gets the status updated from 4 (Exported) to 5 (Booked/Printed). In that procedure you can also load a list of shipments to check that they are complete.

#### Use "Other quantity" and "Other unit"
Applies to nShift Delivery. With this setting you can determine that the contents of the Other quantity and Other unit fields are by default filled in with the same values as the Quantity and Unit on order fields when you use the Customs information tab in Register shipment.

#### Seller's address
Here you decide if you want to also export the seller's address in shipments when using this shipping service.

#### Seller's ID
Applies to nShift Delivery. This ID is exported if you use Seller's address. The ID is used to match the address with a sender in nShift.

#### Use Seller's ID
- If you activated this setting the seller's name, address, and contact information field will be emptied in the file (the API call).
- If you activated this setting it means nShift Delivery will use the seller based on the "quick ID" (the seller’s ID).
- If you have not activated this setting, nShift Delivery will use the seller's name and address form the file.

#### Purchaser's address
Here you decide if you want to also export the purchaser's address in shipments when using this shipping service.

#### Freight payer address
Here you decide if you want to also export the freight payer address in shipments when using this shipping service.
