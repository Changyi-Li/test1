### Blanket Order – Sales
Under this tab you register order types for blanket order – sales. When you first start up the system, you only see the order type Blanket order. This order type cannot be deleted or inactivated, nor can you change the basic type.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series.

#### Name
The name of the blanket order type. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Basic type
The basic type indicates the function of the order type.

#### Price strategy
The price strategy determines how the price should be entered for the order type. The basic type "Blanket order" has the price strategy According to customer by default. This means that the price is primarily determined by the price linked to the customer and the price list in the customer register. The price strategy Standard price uses the part's standard price. When using the selection Price list, you select a specific price list that should apply to the order type.

#### Rate type strategy
With this setting you decide which rate type should be used for the order type. According to customer is selected by default. This means the rate type entered for the customer will be used primarily. When choosing the According to order type alternative, you get to select a specific rate type. The different rate types in the system are the ones registered in the Currencies procedure, under the Rate types tab.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
Priority 9 is always set for blanket orders.

#### Activity template
The activity template you select here will by default become linked to new orders you create using this order type. Activity templates are predefined sets of activities for the order. They are managed under the Activity templates tab in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – CRM procedure. The activity template of the order is possible to change at a later time.

#### Active
Here you determine if the order type is active. A deactivated order type will no longer be available for the users in the system.

#### Validity period
Here you determine the validity period for the blanket order. If you do not enter anything here, the default validity period is 365 days.

#### Warehouse
This is shown if you have installed the Warehouse option. Here you select to which warehouse this order type applies.

#### Document structure
By using the Document structure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can define which documents should be printed by default together with blanket order – sales with this order type. The documents can, for example, be front pages, and agreements. The documents that you select here will be automatically added to the Document structure tab in the Register blanket order – Sales procedure. This applies to new blanket orders of this order type.
You can add or insert documents in the order you please, to the main document. Click on Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) to add the actual main document (quote, order). This document is displayed as a gray row (see the below image).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/DocumentStructure.png)
> If you do not use document structures, the main document will be printed even if you have not added the main document here (the gray row marked in the above image).
External document files can, for example, be PDF files that you select from a path, using the Browse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png), and give a name in the table. Please note! It should preferably be a UNC path and not a path to a shared unit or a local unit. The reason for this is for the path to be accessible for other users if they should be able to print the documents. A UNC path is written as follows: \\ComputerName\SharedFolder, for example, \\file_server\documents.
One example of document structure is that you first have a front page, then a page with agreement text, then the actual main document, a finally an end/final page.
A document structure can be default. This is primarily decided by the order type and the language of the recipient's mailing address, but you can change the specific document files which should be included in this particular document structure together with the main document. You define default document structures per order type in the Order types procedure.
You add or insert an optional number of document files in the table, and place them in the order you want them. Changes you make will be saved for the record in question in the procedure.
> Please note! To add an external document file ahead of the main document, you must mark the Document row (putting it in focus) and then click the button called Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5) on the function menu.
The result is a compound document containing all document files including the main document in the order they were placed in the document structure. If you send this as an e-mail to the recipient, a single PDF file will be created of all the document files including the main document, and it will be attached in the e-mail. If you print the document structure, all the documents will be printed in the same order as in the table.
