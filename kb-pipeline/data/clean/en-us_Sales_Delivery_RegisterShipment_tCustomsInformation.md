### The Customs information tab

#### Customs info – Header
Here you can manage customs information and include it when the shipment is exported to nShift Web-TA, nShift Delivery, or Logtrade.
With the Use customs info setting you decide if customs information should be managed for this shipment. This will make the fields available in the tab, as well as the Rows box.
If you are using customs information with EORI number and the shipping service is configured to export seller’s address and purchaser’s address, it means the EORI numbers entered under the Customs information tab only will be linked to the pick-up address and delivery address in the export file.
The Customs payer field makes it possible to create shipments in Web-TA with customs information and different delivery terms than Ex Works. Here you enter the correct agreement number with reference to the customs payer.
Customs payer
- Paying party – Here you select who should be the customs payer. The available options are:
Paying party
- Seller pays – The customs payer’s address and identifier is the same as for the seller.
- Purchaser pays – Default option. The customs payer’s address and identifier is set to the same as for the purchaser.
- Other payer – Here you can manually enter the customs payer’s address and contact information or select an address from an existing party in the company information, supplier register, or customer register.
- Customs payer – Show the address of the customs payer. Here you can, when needed, enter another address for the customs payer.
- Identifier – Shows the customs payer's identifier:
Identifier
- EORI – The EORI number of the customs payer.
- VAT registration number – The customs payer’s VAT registration number.
- Corporate ID number – The customs payer’s corporate ID number.
The Reason for export field is used and can be edited when integrating with Logtrade.

#### Rows
By using the Load customs information button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you load the customs information from the customer orders etc. which you have loaded to the Source of information box. First choose the Trade classification code type. The information is shown per Trade classification code, Country of origin and unit. This information is then exported to nShift Web-TA, nShift Delivery, or Logtrade, and is included on the customs document/documents you entered in the Customs documents field under Customs info – Header. Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you find the Trade classification information which shows the different types of classification codes.
If you have activated the setting Use "Other quantity" and "Other unit" for nShift Delivery in the Shipping services procedure, the contents of the fields called Other quantity and Other unit will be filled by default with the same values as the Quantity and Unit on order fields.
