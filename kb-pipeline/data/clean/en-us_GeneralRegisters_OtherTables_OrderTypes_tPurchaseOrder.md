### Purchase order
Under this tab you register order types for purchase orders. When you first start up the system, you find the order types Buy material and Subcontract with these basic types. If you have installed the option Warehouse you also find the order type Stock order. These order types cannot be deleted or inactivated, nor can you change the basic type.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series. For example when registering purchase orders and the next number in the number series is 1001 and the prefix is S on the order type, then the order number will be set to S1001.

#### Name
The name of the order type. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Basic type
The basic type indicates the function of the order type. Here you find Buy material when creating a new purchase order type.
> You cannot create own order types of the type Subcontract. Purchase orders of the type subcontract are automatically created by the system when reporting subcontracts.

#### Rate type strategy
With this setting you decide which rate type should be used for the order type. According to supplier is selected by default. This means the rate type entered for the supplier primarily will be used. When choosing the According to order type alternative, you get to select a specific rate type. The different rate types in the system are the ones registered in the Currencies procedure, under the Rate types tab.

#### Posting group
Posting group for the order type (does not apply to the basic type Stock order). The available posting groups are of the type Purchase in the Posting matrix procedure.

#### Document structure
By using the Document structure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can define which documents should be printed by default together with purchase orders of this order type. The documents can, for example, be front pages, and agreements. The documents that you select here will be automatically added to the Document structure tab in the Register purchase order procedure. This applies to new purchase orders of this order type.
You can add or insert documents in the order you please, to the main document. Click on Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) to add the actual main document (quote, order). This document is displayed as a gray row (see the below image).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/DocumentStructure.png)
> If you do not use document structures, the main document will be printed even if you have not added the main document here (the gray row marked in the above image).
External document files can, for example, be PDF files that you select from a path, using the Browse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png), and give a name in the table. Please note! It should preferably be a UNC path and not a path to a shared unit or a local unit. The reason for this is for the path to be accessible for other users if they should be able to print the documents. A UNC path is written as follows: \\ComputerName\SharedFolder, for example, \\file_server\documents.
One example of document structure is that you first have a front page, then a page with agreement text, then the actual main document, a finally an end/final page.
A document structure can be default. This is primarily decided by the order type and the language of the recipient's mailing address, but you can change the specific document files which should be included in this particular document structure together with the main document. You define default document structures per order type in the Order types procedure.
You add or insert an optional number of document files in the table, and place them in the order you want them. Changes you make will be saved for the record in question in the procedure.
> Please note! To add an external document file ahead of the main document, you must mark the Document row (putting it in focus) and then click the button called Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5) on the function menu.
The result is a compound document containing all document files including the main document in the order they were placed in the document structure. If you send this as an e-mail to the recipient, a single PDF file will be created of all the document files including the main document, and it will be attached in the e-mail. If you print the document structure, all the documents will be printed in the same order as in the table.

#### Purchase statistics
Here you determine if purchase statistics should be created for orders with this order type.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
When the priority of the purchase order is set, the priority of the order type is always combined with the priority of the supplier. The highest priority of the order type and supplier is therefore the order's priority.

#### Activity template
The activity template you select here will by default become linked to new orders you create using this order type. Activity templates are predefined sets of activities for the order. They are managed under the Activity templates tab in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – SRM procedure. The activity template of the order is possible to change at a later time.

#### Exclude from EDI
This setting is available if the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. option with formats for purchase order is installed in your system. With this setting you decide if purchase orders with this order type by default should be excluded from EDI. This way you can handle orders outside the EDI flow in parallel with EDI orders, to suppliers connected to EDI. You should register an additional order type for the Buy material basic type when you have this setting activated. That is, register it in addition to the regular order type for "Buy material" for which this setting is not activated.

#### Intrastat
For each order type you can configure different settings regarding transaction types and which value should be reported in the Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. report. Which fields can be entered and which options are available in each respective field depend on which basic type the order type has.

#### Active
Here you determine if the order type is active. A deactivated order type will no longer be available for the users in the system.
