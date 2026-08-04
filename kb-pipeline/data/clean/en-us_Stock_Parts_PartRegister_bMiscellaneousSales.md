### Miscellaneous
In this box you configure other settings regarding sales of the part.

#### Lead time to customer
Here you can enter a general lead time to customer in work days. A check will be made against this date at order registration. This is overridden by the Lead timeNumber of days between ordering date and delivery date. Normally used for purchased parts. of the customer link in the Customer links box. This field does not exist for parts of the Service type.

#### Quantity for lead time
Here you enter the general quantity of parts on the order for lead time to customer. It is overridden by the Quantity for lead time of the customer link. This field does not exist for parts of the Service type.

#### GS1 code
In this field you enter the general GS1 code that applies to the part. You can use a maximum of 13 characters. It is overridden by the GS1 code for the part in customer links. This field does not exist for parts of the Service type.
Using the Generate GS1 code button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) next to the field you can automatically generate a GS1 code according to GTIN13 standard. The result of this generation is saved in the field. The code is also save under Other part identities. By using the Clear GS1 code button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) you can remove the GS1 code in the field of the part. Then it will also be deleted as other part identity.
A condition for this automatic generation to function is that GTIN13 is activated under the tab Other part identities, in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure. When GTIN13 is activated, it is not possible to edit directly in the GS1 code field, instead you have to use the automatic generation to get a GS1 code.
During the automatic generation the GS1 code is created from the company's GS1 company prefix from the Company information procedure and from the GS1 code number series under the Stock tab in the Number series procedure. A check digit is also added, giving the GS1 code a total of 13 digits.
A company prefix can be six to nine digits (the company is assigned a company prefix from a GS1 standard organization). If the company prefix is, for example, nine digits long you should enter the first to the sixth digit as the GS1 company prefix. The seventh to the ninth digit should then be entered in the number series plus three zeros for consecutive number, making the number series six digits long.
Example:
Received company prefix: 731234195. You then enter 731234 as GS1 company prefix and 195000 as number series. The control digit is calculated when the GS1 code is generated.

#### Other part identities
By using this button you can enter other part identities if for example GS1 code is insufficient for the part. You can choose between several GTIN (Global Trade Item Number), SGTIN (Serial Global Trade Item Number), or Other/No type. For GTIN, you find the variants GTIN8, GTIN12, GTIN13, and GTIN14. You must enter correct number of digits as Identity for the selected variant. The number must also have correct control digit at the end. Otherwise, a warning appears.
You can add several other part identities for the same part and set them as active. However, a specific part identity can only be active for one part at a time. This means that you cannot enter the same Identity for two parts and set both as active.
In the Basic data – Part procedure you can add other part identities that can be used in different situations for parts. Other part identities can be used to match parts in Monitor ERP with parts in import files when using EDIEDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. import. Other part identities can also be used if you have installed the option Customer order transfer. Then you can match parts in sales companies with parts in production companies

#### Default warehouse on customer order
The warehouse you select here will be the default warehouse for the part on customer order rows. If the field is left empty, the warehouse of the order header will be suggested on the order rows.
This setting is available if the Warehouse option is installed in your system.

#### Alloy cost/Mark-up
A part that you sell can be linked to one or several alloy costs. These can be calculated in the Pre-calculation procedure or added manually here for the part. The alloy code/mark-ups are handled in the Basic data – Part procedure. This field does not exist for parts of the Service type.

#### Invoicing log
By clicking this button, a dialog box will show a log of printed customer invoices. There is also a function that shows the customer invoice document itself, as well as a function to link to the procedure Register invoice directly, Customer register, and Customer order info for each log record. If you have installed the option Warehouse, the statistics is shown for the selected warehouse.

#### Sales statistics
By clicking this button you can see a total of sales statistics for the part. If you have installed the option Warehouse, the statistics is shown for the selected warehouse.

#### Show structure when registering orders
(For fictitious parts) If you have activated this setting, the material list with the included parts in the fictitious part are possible to edit when the part is selected on a quote, customer order, and invoice row. Then a dialog box opens where you can see the structure of the fictitious part. If it is a main part that has included fictitious parts, these are shown in the structure in the left portion of the dialog box. In the right portion of the dialog box, you find the selected fictitious part's included parts in a material list. It is possible to change the quantity and discount for each part in the material list. The user can also add and delete parts in the material list.
The BOM and routing is not affected, it is based on you creating a BOM for the fictitious part in the regular way.
When you click OK in the dialog box, the rows will be generated. Parts that have zero (0) in quantity in the material list will not be included.
If the setting has not been activated, you cannot see and edit material lists in the structure for the fictitious part. Then another dialog is displayed when the part is selected on quotes, customer orders, and invoice rows. There you can enter quantity, unit, variant code, and delivery date for all included parts according to the structure in the BOM and routing.

#### Deviation model
The deviation model is used to analyze delivery schedules. Deviation models are created in the Basic data – Delivery schedules procedure. [Read more](../../../Sales/DeliverySchedules/BasicDataDeliverySchedules/bDeviationModel.htm) on how deviation models are prioritized.

#### Deviation model definition
Here you can see the deviation model that you've selected.
