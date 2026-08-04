### Customer agreement
Under this tab you register order types for customer agreements. One order type is included in the system. This cannot be deleted or inactivated, nor can you change the basic type.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series. For example when registering customer orders and the next number in the number series is 1001 and the prefix is S on the order type, the customer order number is set to S1001.

#### Order type
The name of the order type. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Basic type
The basic type indicates the function of the order type. The Agreement basic type is available to choose when you create a new order type for agreement.

#### Price strategy
The price strategy determines how the price should be entered for the order type. The Agreement basic type has the price strategy called According to customer by default. This means that the price is primarily determined by the price linked to the customer and the price list in the customer register. When using the selection Price list, you select a specific price list that should apply to the order type.

#### Rate type strategy
With this setting you decide which rate type should be used for the order type. According to customer is selected by default. This means the rate type entered for the customer will be used primarily. When choosing the According to order type alternative, you get to select a specific rate type. The different rate types in the system are the ones registered in the Currencies procedure, under the Rate types tab.

#### Posting group
The posting group for the order type. The available posting groups are of the type Sales in the Posting matrix procedure.

#### Variants
By clicking the Variants button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access settings where you can configure a default document variant for customer agreement and modified customer agreement.

#### Document structure
By using the Document structure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can define which documents should be printed by default together with agreements of this order type. The documents can, for example, be front pages, and agreements. The documents that you select here will be automatically added to the Document structure tab in the Register agreement procedure. This applies to new agreements of this order type.
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
The priority is used to prioritize quotes, inquiries, orders, agreements, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
This priority of the order type is always combined with the priority of the customer, when the priority of the agreement is decided. The highest priority of the order type and customer will become the agreement's priority.

#### Update status automatically
This setting is activated by default. The system will check the "Valid from" date in cases where the agreement has status Signed/Valid. When the Valid from date is reached, the agreement will automatically get status Active.

#### Notice period
Here you can enter a default notice period for the agreement type.

#### Invoicing method
Here you decide which invoicing method should be default for the agreement type; In advance or In arrears.

#### Invoicing interval
Here you can choose a default invoicing interval as well as if accrual accounting should be applied for the agreement type. "Monthly" is the invoicing interval suggested by default. If you choose to apply accrual accounting, you should also enter an accrual account. The following invoicing intervals are available:
- Monthly
- Every other month
- Quarterly
- Every four months
- Every six months
- Annually
You can also decide if an accrual account should be used for a specific invoicing interval.

#### Planned invoice date
You can use this function to decide how many days before or after a period the Planned invoice date will be set.
For example, if an agreement has Invoicing method = Advance, Invoicing interval = Month, and Planned invoice date set to 5 days, then the Planned invoice date on the agreement basis will become February 24 for the period 2022-03-01–2022-03-31.

#### Enter "Valid from" to
Here you decide how "Valid from" should work on an agreement. The available options are Today and Empty, where Today is the default for new order types.
By choosing Today it means that the "Valid from" date for a new agreement will be today's date.
By choosing Empty it means that the "Valid from" date for a new agreement will be empty. A validation will then be shown in the Valid from field indicating that a value must be entered before the agreement is saved.

#### Release basis automatically
This setting is not activated by default for new order types.
With this setting you decide if "Release basis automatically" should be activated by default when a new agreement is registered.

#### Trigger upward adjustment
With this setting you can decide if a change made during an invoiced period should trigger an upward adjustment or not.
- Always – Will always trigger an upward adjustment.
- Never – No upward adjustment will be triggered.
- Minimum amount on row – If the total amount for changes on a customer agreement row exceeds the entered amount in the Trigger value column, an upward adjustment row will be suggested. This is useful in order to avoid invoicing small amounts.
- Min. amount for all rows – If the total amount for changes on all customer agreement rows exceeds the entered amount in the Trigger value column, an upward adjustment row will be suggested. This is useful in order to avoid invoicing small amounts.
- Min. days to next invoice – This option will only take the next invoice into consideration. If changes are made to a row prior to the entered number of days before the next invoice, an upward adjustment will be suggested. This is useful if changes are made to customer agreement rows close to sending of a new invoice.

#### Trigger
Here you enter the trigger values for the following options: Minimum amount on row, Minimum amount for all rows, and Min. days to next invoice in the setting called Trigger upward adjustment.

#### Activity template
The activity template you select here will by default become linked to new agreements you create using this order type. Activity templates are predefined sets of activities for the order. They are managed under the Activity templates tab in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – CRM procedure. The activity template of the order is possible to change at a later time.

#### Active
Here you determine if the order type is active. A deactivated order type will no longer be available for the users in the system.

#### Log
By using the Log button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find a changelog for the order type. Here you see who modified the information as well as when. You also see what has been changed, with the value before and after the change.
