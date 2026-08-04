### Channels
In this table you add the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. channels that you will need.
By using the buttons in the function menu you can add, insert, delete, and copy channels row by row.

#### Name
Here you enter the name of the channel. You see the name of the channel in the EDI configurations procedure.

#### Active
Here you determine if the channel is active. Only active channels can be used in the EDI configurations procedure.
If you try to deactivate a channel that is already used in one or several EDI configurations, this must first be confirmed in a dialog window. In the dialog window you see to which configurations the channel is linked as well as if the channel is active in these configurations.
If you make any changes in a channel, it will be inactivated by default. A warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) then appears indicating that the channel has been inactivated due to a change.

#### Format
Here you enter/see the EDI format. The available formats are the formats installed in the system. The format determines the module, direction, and transaction type.

#### Version
Here you select which version of the format should be used in the channel. You can select version in the field.

#### Version information
By using the button Ver. info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png) you can see which fields the selected format contain.

#### Module
Here you see the module for the selected format.

#### Direction
Here you see the direction for the selected format.

#### Transaction type
Here you see the transaction type for the selected format.

#### Source
If the direction is Import, you can select a Source for the channel among the sources you have registered. If the direction is Export, the Source is always set to Monitor ERP.

#### Target
If the direction is Export, you can select a Target for the channel from the targets you have registered. If the direction is Import, the Target is always set to Monitor ERP.

#### Schedule
If the channel should automatically be run based on a schedule, you select schedule here. The schedule must first have been created and activated under the Schedule tab.

#### Immediate export
If the Immediate export checkbox is marked, an EDI export will export the transaction directly to the target. This is done without having to wait for a scheduled event to occur. When you activate this setting it will automatically deactivate the Schedule column.

#### Save transactions
Here you determine for how long the channel's transactions and belonging files should be saved before they are deleted. The default value is 120 days, but this can be changed. When a transaction has been deleted, it is no longer visible in the Manage EDI transactions procedure.
> Transactions that are older than the entered value will be automatically deleted at 3:00 AM every night. If the Monitor ERP server is not started at that point, the records will be deleted as soon as the Monitor ERP server is started again.

#### Export extra fields
Here you can choose which fields to add to be included in the export. No alternatives are selected by default. The available options are:
- Order header
- Order row
- Customer/Supplier
- Part

#### Included in configuration
By using the button Included in configuration ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see in which configurations the channel is used. You also see if the configurations are active.

#### Trim
Here you decide if the fields in the delivery schedule file should be trimmed, that is, if the blank spaces in the beginning and in the end should be deleted or not, when importing delivery schedule. The fields are trimmed by default. This setting is only activated for Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. – Sales.
If you uncheck the checkbox, it means that if the customer’s part number starts with blank spaces in the file, the part number will be matched using also the initial blank spaces.
The initial blank spaces are kept when the customer’s part number is saved in the part link when adjusting the EDI transaction in the Manage EDI transactions procedure.

#### Log
By using the button Log ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find a changelog for the channel. Here you see who modified the information as well as when. You also see what has been changed, with the value before and after the change.
