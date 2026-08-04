### Edit report
By clicking the Edit report button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) in the function menu you open an editor you use to create/construct the customized report. This editor is available both in the List type box and in the Sub-reports box. The editor consists of the following tabs: Layout, Selection rows, Settings, and SQL. For a sub-report, the Selection rows tab is not shown..
Layout
There are two variants of the tab depending on if you selected List or Free-format layout under Type. If you have selected Free-format layout, you can select Include company logotype in “Field list”. By doing this, the company logotype will appear in the list with different database fields that can be added to documents.
List
If you chose List as the Type, you find an editor under the tab where you enter different properties for the data columns in the report. The data columns are displayed as rows under the tab. The columns are loaded from the result of the SQL query entered under the SQL tab.
For each data column you can configure a number of properties according to the following. You can also change the order of the columns in the report by using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png), or by using the "drag and drop" function.

#### Heading
Here you enter the heading of the column in the report. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Grouped
If this box has been checked, the column will be grouped.

#### Width
The default column width in number of pixels in the report.

#### Sorting
Determines if the columns should be sorted in ascending order, descending order, or not at all.

#### Display format
Here you decide the display format of the column. Both numerical and date and time formats are supported.
You can see which [standard numeric formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings) .NET supports here.
You can see which [custom numeric formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings) .NET supports here.
You can see which [standard date and time formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings) .NET supports here.
You can see which [custom date and time formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) .NET supports here.

#### Aggregation
Determines if the values on all rows in the column should be aggregated or not in the report. The different types of aggregation that can be selected are: Total, Average value, Quantity, Min. (value), Max. (value), First record, Last record, Median, and External. The result of the aggregation is shown in bold font under the column in question in the report.

#### Show in chart
Here you determine if the column in question should be shown in chart by default. When you choose to view the report in chart form, the columns for which this setting has been configured will be included. If the checkbox is not available for a column, it means that the data in this column cannot be shown in charts.

#### More info
Check this box if the column should be available under the button More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the report.

#### Print
Check this box if you want to include the column in the printout of the report.

#### Hidden
Check this box if you want to exclude the column when loading the list in the report.

#### Clipboard
Here you can configure which register in Clipboard that data in the report should be able to be copied to.

#### Procedure link
Here you configure, based on the type of data record, to which procedure it should be possible to go to from the report.

#### Follow active record
You can activate Follow active record here ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_follow_active.png).
Free-format layout
If you chose Free-format layout as the Type, you can in the tab both preview the layout of the report and edit the report.

#### Edit
At the top of the tab you will find the button Edit ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_xtrareport_designer.png). This button opens the report editor DevExpress Report Designer used to create you report. In the editor you have access to the settings you have added to the report under the Settings tab. You also have access to the columns resulted from the SQL query you wrote under the SQL tab.
> To edit reports you must also have knowledge about the report design tool DevExpress Report Designer. Editing of reports is also available as a service you can order from our consultants or from our Support Center at Monitor ERP System AB.
Selection rows
This tab is available for reports in the List types box. Here you determine which selection rows you want to include in the selection for the list type. You add selection rows and configure them according to the following.

#### Name
This text is shown as the name of the selection row. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Database field
Here you enter the table and column name from your SQL query for the selection row. You can NOT enter an alias that you have created in the SQL query.

#### Grouping name
If you would like the selection rows to be grouped under a heading, such as Manufacturing order or Part, this can be entered here.

#### Type of field
The database field's type. Here you can select Text, Numerical, Date, or Date + Time.

#### Category type
If you are using Categories, you can here select a category type. Before you start using categories, these must first be registered in the Categories procedure.

#### Default value: From
Here you can configure a default value in the From field of the selection row.

#### Default value: To
Here you can configure a default value in the To field of the selection row.

#### Exclude
Here you choose if the selection row should have Exclude checked by default.

#### Type of selection
This field is active if the Enum field is set to None. Here you can select Equal to (Eq), Between, or Contains.
Equal to and Contains only activate the From field on the selection row. Between activates both the From and To fields.

#### Enum
Here you can select a predefined enumeration type of data for the selection row. The None option is selected by default. This means no predefined enumeration type is used. If you choose any of the other options, the preceding Type of selection field becomes deactivated. You will instead get to choose a type of selection for Enum in the next Type of selection field.

#### Lookup
This field is active if the Enum field is set to None. Then you can here choose a lookup feature for the fields on the selection row. You can choose among the lookup features available in the database.

#### Clipboard
This field is available if a lookup feature has been selected in the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. field. Here you can then configure from which register in Clipboard it should be possible to copy data to the selection row.
Settings
Under this tab you can configure an optional number of settings for the report or sub-report. The settings are shown at the bottom of the Selection tab in the customized report procedure that you create.

#### Code
Here you enter a unique code for the setting. This is the name to which you refer in the SQL query. You can enter a maximum of 50 characters.

#### Name
This text is shown as the name of the setting. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.You can enter a maximum of 100 characters.

#### Test value
Setting for sub-report Here you can enter test values.

#### Type
Setting for report. The different types of settings that can be used: Checkbox, Text field, Integer, Decimal number, Date without time, Date with time, Option – Register, and Option.

#### Register
Setting for report. Here you can select register if you have chosen Option – Register under Type.

#### Selection list
Setting for report. If you have chosen Option under Type, you can add rows to a selection list by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). On each row you enter an internal name and name. The user will then see the name in the selection list. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Default value
Setting for report. Here you can enter or configure a default value, dependent of the selected Type. If one of the alternatives Date without time or Date with time has been selected as type, you can here enter a macro.

#### Mandatory
Setting for report. Here you can enter that the setting must be entered before the report can be used.
SQL
Here you create an SQL query. The result of the query will also be displayed here. The report is then based on this SQL query.

#### SQL query
Here you type the SQL query for the list type.
> You must have knowledge about names of Monitor's tables, columns, and alias in the database. You must also know how to write SQL to be able to write correct SQL queries.
By using the Test ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) button, you can test the SQL query and the result will be displayed in the Result box.
By using the Insert placeholder for warehouse ID button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) you insert a code (where the cursor is placed) for the warehouse ID. The code is :w#Id.
By using the Insert placeholder for language ID button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_url.png) you insert a code (where the cursor is placed) for the language ID. The code is :lng#Id.

#### Result
Here you see the columns and rows returned by the SQL query as result.
In the Maximum result (rows) field you enter the greatest number of rows which should be possible to be returned by the test run of the SQL query.
In one of the fields a message is returned about the test run of the SQL query.
