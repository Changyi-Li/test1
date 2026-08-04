### Other general differences

#### Date format
There are two date formats in G5. These are YYYY-MM-DD and YYWWD. The format YYWW is not supported in G5.

#### Handling of time zones
Now it is possible to choose time zone per warehouse. This makes it possible to use local time for attendance recording and work recording, instead of the time on the server's clock.
Also, all logs will be using the time zone of the warehouse. This applies to logs from all modules in the system.

#### Everything is displayed in the language of the user/recipient
A basic principle in G5 is that all data shown to the user should be shown in the user's language. That is why all data in registers now can be translated and not only the information shown on documents. An English users will then be able to see for example a part name, part code, price list, etc. in English when he/she loads the part in the Part register. If the data is not translated, it will be shown in the company language.
Another scenario is if you register a customer order to a customer where the mailing address is Great Britain and the delivery address is to Germany. And you run the program in Swedish. When you register the customer order row you will see the part's Swedish name. On the order confirmation the English name is shown and on the delivery note the German name is displayed. If a Finnish colleague works in the shipping department and prints a pick list, then the part's Finnish name is shown.

#### Address format
Different address formats can be applied, in most cases linked to different countries. In the Countries procedure you can select default address formats for specific countries. This will then apply for new customers and suppliers in the country in question. When a new customer or supplier is registered you enter country as the first field in the address. As a result of the selected country, the following address rows might vary because of the address format.
The available address formats are:
- General (same as in G4)
- Zip code + City
- City + State/Region + Zip code
- City, Zip code (two rows)
- City/Province + Zip code.
Zip code is handled as a separate field and it is linked to a city or state/region which makes it easier to enter the address. The zip code is shown in the way it should be shown in the country where the city/state/region is located. Even though you start by entering the country in the address it will always be shown last in capitals on the documents.

#### Tip for user
You can get tips for certain fields, selections, or procedures. These tips are shown in a yellow tip window which can be closed and you can also choose not to show the tip again. However, the tip in question is always available via a button illustrated with a yellow light bulb.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Hints.png)](../../../../../Resources/Images/News/Hints.png)

#### Built-in calculator
In all numerical fields it is possible to write formulas to calculate a new value. As long as the text is green it means that the formula expression is okay. If the expression is not okay the text will instead be shown in red.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Calculator1.png)](../../../../../Resources/Images/News/Calculator1.png)
When you leave the field, the value is calculated and shown in the field.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Calculator2.png)](../../../../../Resources/Images/News/Calculator2.png)

#### Filters in tables
In all columns in tables (in lists as well) it is possible to filter by using a filter function in the column heading. You can filter out data by unchecking checkboxes or by entering what should be filtered out.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/FilterInGrid.png)](../../../../../Resources/Images/News/FilterInGrid.png)

#### Searching in tables and lists
In tables and lists you can use the button Find ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) (Ctrl + B) to search for data. This function opens a search field above the table or the list, and there you enter what you search for.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/SearchLists.png)](../../../../../Resources/Images/News/SearchLists.png)

#### Lookup
Find-as-you-type and the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature have been merged into one function. A search window with different tabs opens under the field in question when you start typing something or when you press F4 to search.
The Browse tab is active when you open the Lookup feature and you have not typed anything in the field. The Pattern search tab is active when you have started typing. It always searches in all columns shown in the Lookup feature. If you add own columns the search will also include these.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Lookup.png)](../../../../../Resources/Images/News/Lookup.png)
Under the Recent tab you see the ten most recently loaded records.

#### Data validation
When data is not correctly entered a red symbol with an exclamation mark is shown. The problem might be that nothing has been entered in the field even though it is mandatory, or that you have not correctly entered data in the field, for example an incorrect format for an e-mail address.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Error.png)](../../../../../Resources/Images/News/Error.png)
The e-mail address is missing an @.
You do not have to correct the error straight away, but when there is an error it is not possible to save in the procedure. The Save symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save_error.png) is in that case shown in red.
In certain cases you receive a warning instead or an error indication. This might for example be when you enter a delivery date which has already passed or if you enter an order quantity which is not a multiple of the part's quantity/package. You are then allowed to save, but you will be informed that the data you have entered might be problematic.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Warning.png)](../../../../../Resources/Images/News/Warning.png)

#### Validation window
When errors and warnings exists in the procedure you will see a summary of these in a list in the bottom right corner of the procedure (the validation window). There might for example exist an error in a field under a tab which is not open at the moment. The errors will always be shown at the top and the warnings are listed below them.
The validation window can be minimized and you will then only see the number of errors and warnings.
| [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Validation1.png)](../../../../../Resources/Images/News/Validation1.png) Expanded mode. | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Validation2.png)](../../../../../Resources/Images/News/Validation2.png) Minimized mode. |
|---|---|
If you click on an error or a warning in the list the focus will go to the field which is concerned by the error or warning. This makes it possible for you to quickly find the error/problem, and to adjust it.

#### Extra fields
To add extra fields in the procedures Part register, Customer register, Supplier register, Register case, and Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material., Project register, Register fixed assets object, and Company information, you use the procedure called Extra fields in the General registers module.
In each register you add, name, and decide which type of field the extra field is. When one or several fields have been created in a register, a tab will become activated in the procedure in question. Here you can then see the extra fields.
The extra fields can be used in the Lookup feature, as selection rows, and as columns in lists.
