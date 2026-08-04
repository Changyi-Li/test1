### Discount categories and part grouping
Here you register all discount categories you will need in your system. You can also, per part category, add part groupings that should be assigned discount rates.

#### Category number
This is a consecutive number for the row. It cannot be changed.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Part grouping
Here you will see which part grouping term should be assigned discount rates. In the system setting called Part grouping term for discount categories you determine which part grouping term you want to use. The available alternatives are product group, part code, and part category.
- Product group – here you can assign discount rates to product groups registered in the Posting matrix procedure.
- Part code – here you can assign discount rates to part codes registered in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure.
- Part category – here you can assign discount rates to part categories registered in the Categories procedure. The button Category selection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is activated if there is a selection list to part categories in which you then can select part categories from the selection list. You can also use the wildcards % and _ when you create discount categories based on part category.

#### Discount
Here you enter the discount in percent that should apply to this part grouping.
This field is only available if you have not activated the setting Manage staggered discount rates in the procedure Discount categories. If the setting has been activated you must instead enter up to ten different limit values in quantity or amount in the fields described below.

#### Quantity/Value
Here you determine if the limit values for discount rates should apply to the quantity or value (amount) on quote rows, customer order rows, invoice rows, inquiry rows, and purchase order rows.

#### Limit 1-10
Here you enter limit values in quantity or amount. You can enter a maximum of 10 limit values.

#### Discount 1-10
Here you enter the discount in percent for each respective limit value.
