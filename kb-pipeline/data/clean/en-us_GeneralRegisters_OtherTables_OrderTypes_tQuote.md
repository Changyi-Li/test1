### Quote
Under this tab you register types for quotes. When you first start up the system, you only have the order type called Quote. This cannot be deleted or inactivated, nor can you change the basic type.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series. For example when registering quotes and the next number in the number series is 1001 and the prefix is S on the quote type, then the quote number will be set to S1001.

#### Name
The name of the quote order type. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Basic type
The basic type decide the function of the quote order type. Today, only the Quote basic type is available when creating a new order type for quote.

#### Price strategy
The price strategy determines how the price should be entered for the order type. According to customer is selected by default. This means that the price is primarily determined by the price linked to the customer and the price list in the customer register. When using the selection Price list, you select a specific price list. When using the selection Standard price, the part's standard price will be used.

#### Order type discount
Here you can add a discount in percent straight to the order type. When you create a quote with this order type, this discount will be added to the quote rows as Order type discount (code 5).

#### Rate type strategy
With this setting you decide which rate type should be used for the order type. According to customer is selected by default. This means the rate type entered for the customer will be used primarily. When choosing the According to order type alternative, you get to select a specific rate type. The different rate types in the system are the ones registered in the Currencies procedure, under the Rate types tab.

#### Posting group
The posting group for the order type. The available posting groups are of the type Sales in the Posting matrix procedure.

#### Variant
You can select which document variant for quotes should be selected by default for this to order type of quote. Document variants are handled in the Document templates procedure. The option Default refers to the document variant for quote set as default in that procedure.
For quotes, you can use a document variant per quote type. This is registered under the Quote tab in the Order types procedure. For customer orders you can use document variants per order type for order confirmations, invoices, delivery notes, and transport labels. You register this in the Order types procedure under the Customer order tab. The document variant can be entered per customer in the Customer register.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### Document structure
By using the Document structure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can define which documents should be printed by default together with quotes with this order type. This can for example be front pages, agreements, and calculations. The documents that you select here will be automatically added to the Document structure tab in the Register quote procedure. This applies to new quotes with this quote type.
You can add or insert documents in the order you please, to the main document. Click on Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) to add the actual main document (quote, order). This document is displayed as a gray row (see the below image).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/DocumentStructure.png)
> If you do not use document structures, the main document will be printed even if you have not added the main document here (the gray row marked in the above image).
External document files can, for example, be PDF files that you select from a path, using the Browse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png), and give a name in the table. Please note! It should preferably be a UNC path and not a path to a shared unit or a local unit. The reason for this is for the path to be accessible for other users if they should be able to print the documents. A UNC path is written as follows: \\ComputerName\SharedFolder, for example, \\file_server\documents.
One example of document structure is that you first have a front page, then a page with agreement text, then the actual main document, a finally an end/final page.
A document structure can be default. This is primarily decided by the order type and the language of the recipient's mailing address, but you can change the specific document files which should be included in this particular document structure together with the main document. You define default document structures per order type in the Order types procedure.
You add or insert an optional number of document files in the table, and place them in the order you want them. Changes you make will be saved for the record in question in the procedure.
> Please note! To add an external document file ahead of the main document, you must mark the Document row (putting it in focus) and then click the button called Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5) on the function menu.
The result is a compound document containing all document files including the main document in the order they were placed in the document structure. If you send this as an e-mail to the recipient, a single PDF file will be created of all the document files including the main document, and it will be attached in the e-mail. If you print the document structure, all the documents will be printed in the same order as in the table.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
This priority of the order type for quote is always combined with the priority of the customer, when the priority of the quotes is decided. The highest priority of the order type and customer will become the quote's priority.

#### Activity template
The activity template you select here will by default become linked to new quotes you create using this order type. Activity templates are predefined sets of activities for the quote. They are managed under the Activity templates tab in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – CRM procedure. The activity template of the quote is possible to change at a later time.

#### Active
Here you determine if the quote type is active. A deactivated quote type will no longer be available for the users in the system.

#### Customer order type
Determines which order type for customer order should be suggested when creating a new customer order from a quote that has this order type. Selectable order types have the basic type New sales.

#### Requirement calculation
With this checkbox you decide if the order type should be included in requirement calculations and net requirement calculations. The probability code of the quote determines how big a percentage of the quote row quantity should be included in the requirement calculation/net requirement calculation. In the Requirement calculation and Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedures, Quote must also be selected to be included in the calculation.
