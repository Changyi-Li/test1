### Filter lists
In lists in Monitor ERP there are different filter methods. These are described in this topic. You can filter values in all columns in the list by entering intervals. You can also create advanced filters in a list by using different Boolean operators and terms. In column headings you can search and filter by values in the column. On the context menu there is also a quick filter where you filter the value in the column on the marked row.
The Filter button
The Filter button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/button_filter.png) (Ctrl + Shift + F) on the function menu and the context menu opens the filter window. Here you can choose to create a standard filter or an advanced filter via the field at the top of the window. In a standard filter you enter value intervals in the available columns in the list.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/filter_window.png)](../../../Resources/Images/UserGuide/filter_window.png)
> A standard filter can always be changed to an advanced filter (via the selector in the window). But for an advanced filter it is in most cases not possible to change to a standard filter.
Advanced filter
In an advanced filter there is an editor where you can create advanced filtering of values with the help of Boolean operators and terms. The filter term is based on a structure which starts with And. It means that all underlying terms must be fulfilled for the filter to get a match. If you instead choose Or in the start mode, then it is sufficient that one of the underlying terms is fulfilled.
Example: You want either the term "Price each" to be fulfilled or the term "Amount" to be fulfilled or the term "Remaining" to be fulfilled. Then you create the filter with Or as a start according to the illustration.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterWindow.png)](../../../Resources/Images/UserGuide/AdvancedFilterWindow.png)
Explanation of the term in the image: Remaining is greater than 1,000.00 OR Price each is greater than 200.00 AND Amount is greater than 30,000.00.
Explanation of functions in advanced filter
For each Boolean operator there is a menu where you can change between And, Or, And not, and Or not. You can also choose to add a term or group from that menu. A group is an underlying section containing a Boolean operator and its underlying terms. By using groups you can create complex nested terms.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterWindowMenu.png)
Menu on Boolean operator.
You can also add terms using the plus sign in the editor, or by using the Insert key or Plus key on the keyboard.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterAddTerm.png)
Add terms using the plus sign, Insert or the plus key.
You create a term from a column from the gross list to the selected list type. Click the square brackets "[]" which initiate the term.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterWindowTerms.png)
Gross list of columns for the list type.
Starts with is included by default in the term but you can select among many different options.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterWindowOperators.png)
Selectable alternatives in terms.
You then enter the value for the selected column in the term.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterTermValue.png)
The value in the term.
Instead of entering a value you can in the term choose to compare the value in the selected column with a value in another column. Then click the pen symbol.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterTermCompare.png)
You then click the column link and select column to compare with the columns from the gross list.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterTermCompare2.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/arrow_right.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedFilterTermCompare3.png)
The function menu in the filtering window
On the function menu in the filtering window there are a few buttons which are described below.
- Manage filters ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_load_default_values.png) – Here you load saved filters, edit filters, or delete filters.
- Save the filter currently in use ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) – Here you save the filter entered in the filtering window, either to a new filter for which you get to enter a name, or you can choose to replace an existing filter.
- Add row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) – With this button you add (copy) the marked filtering row. This only applies to standard filters.
- Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) – With this button you delete the marked filtering row. Only applies to rows which you have added in standard filters.
- Clear filter ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) – This will only clear the filter entered in the filtering window. If you have loaded a saved filter, this will still be available.
Column filter
Under the filter button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/button_filter_column.png) in column headings you can search and filter by values in the column. See an image below of this column filter.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/column_filter.png)](../../../Resources/Images/UserGuide/column_filter.png)
> Column filters also work for columns for the type Extra fields.
Quick filter
You can quick filter the value in the column on the marked row. To quick filter you right-click in the list and hold the mouse pointer over the option Filter by xxxxxxx using value "yy" on the context menu. Then you select one of the different terms available on the sub-menu. See an image below of this quick filter.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/quick_filter.png)](../../../Resources/Images/UserGuide/quick_filter.png)
A filter which you have applied is shown at the bottom below the list in the window. Above it you also see how many rows the filtered list contains (of the total number of rows). You use the Edit button to the right to make modifications to the filter. This is then done in the editor for advanced filter.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/applied_filter.png)](../../../Resources/Images/UserGuide/applied_filter.png)
It is possible for you to remove a filter which you have applied. This is done at the bottom of the procedure window by clicking on the X button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_close.png) or by selecting Clear filter on the context menu, or in the filter window.
