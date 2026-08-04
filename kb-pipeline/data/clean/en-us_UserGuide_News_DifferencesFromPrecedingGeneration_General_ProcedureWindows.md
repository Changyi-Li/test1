### Procedure window

#### Toolbar
The toolbar is a part of the procedure window, and not a part of the module window as in G4. This design change has mainly been made to make it possible to move a procedure to another screen. The toolbar will now accompany the procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/ToolBar.png)](../../../../../Resources/Images/News/ToolBar.png)
New buttons/functions on the toolbar:
- Reload ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) loads the data again to the procedure.
- Filtering ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search_form.png) opens a window where you can filter records in cases where you want to see/update multiple records at the same time in single-record procedures.
- Load default values ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_load_default_values.png) is active if there are saved filters, which you easily can switch between.
- Go to field ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) opens a window where you can search by field labels to find where a certain field is located. When you select a field this will be highlighted in the program.
- Follow active record ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_follow_active.png) means that the procedure automatically loads the active record or that it becomes highlighted in another procedure.
A list of the most commonly occurring buttons on the toolbar is found [here](../../../Interface/ToolBar.htm).

#### Focus
Blue color indicates where the focus is. The procedure which is in focus has a blue border in the upper part of the window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/ToolBar.png)](../../../../../Resources/Images/News/ToolBar.png)
An active tab is also indicated with a blue border in the upper part of the tab, and also with blue text in bold font.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Tabs.png)](../../../../../Resources/Images/News/Tabs.png)
A separate field which is in focus is shown with a blue border around the field.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Field.png)](../../../../../Resources/Images/News/Field.png)
In tables the field which is in focus is displayed with a blue border around the field at the same time as the heading is blue and the left border of the row is blue.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Table.png)](../../../../../Resources/Images/News/Table.png)
In total lists the focused row has a blue border.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Rows.png)](../../../../../Resources/Images/News/Rows.png)

#### Comments
Comments written via comment buttons are now possible to format. This also applies to row type 4 on order rows. You can enter font settings, text size, bold font, italics, underline, and text color. It is also possible to paste images.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Comments.png)](../../../../../Resources/Images/News/Comments.png)
Comment buttons where no text has been entered are illustrated with an empty speech bubble.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Comments2.png)](../../../../../Resources/Images/News/Comments2.png)
Comment buttons containing text are illustrated with a filled speech bubble.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Comments3.png)](../../../../../Resources/Images/News/Comments3.png)

#### Links
You can link to other procedures by using the link button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) available in the toolbar of the procedure. You can also go to other procedures from rows in tables.
By right-clicking you access both the links (Go to...) and other buttons in the table.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/RightClickMenu.png)](../../../../../Resources/Images/News/RightClickMenu.png)
From certain desktop components it is also possible to use a link to go to the related procedure. You can for example from the component displaying the order inflow go directly to the procedure BI – Sales for further analysis.

#### Side panel
In most procedures there is a side panel which you can open either with the function key F10 or by clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_sidebar.png) in the top right part of the procedure. In the backstage of the desktop you can configure if the side panel should be shown by default in the procedures.
The purpose of the side panel is to show more information about the record which is loaded in the procedure. This applies both to single-record procedures and to lists. For example, the side panel in the Register customer order procedure displays information about the customer and about the part which is active on the order row.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Sidepanel.png)](../../../../../Resources/Images/News/Sidepanel.png)

#### Floating windows
It is possible to unpin smaller windows, for example the Stock transaction log in the Part register. This is done by clicking on the small drawing pin in the upper right corner. This makes it possible for you to have several such windows open at the same time and you can modify the size and also move the window th another screen. The floating window will be updated when you change record in the main window and it will disappear when the main window closes.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/FloatingWindow.png)](../../../../../Resources/Images/News/FloatingWindow.png)
This functionality is not only available for small windows but also in certain boxes as for example the planning window in the Part register procedure.

#### More info column
In tables and lists you can hide columns which you do not want to show on the rows. This is done by getting a hold of the column heading and drag it downwards. A black X is then shown.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/RemoveColumn.png)](../../../../../Resources/Images/News/RemoveColumn.png)
The column will not be deleted, it is only placed in the More info column to the far right where you can access it via a button.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/MoreInfo.png)](../../../../../Resources/Images/News/MoreInfo.png)
If you want to restore a column placed under More information to the table, you just take the column heading and put it on the heading row.
In certain procedures the column More information is visible as standard. If the column is not visible it will be created when you hide your first column. If you want this placing to be saved you must save the layout by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_layout.png) in the toolbar. The design is saved per user.
In G4 there were many system settings handling this type of showing of columns. These do not exist in G5.

#### Backstage in the procedure window
To reach the backstage of the procedure you can click on the module symbol in the upper left corner of the procedure window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/BackstageInProcedure.png)](../../../../../Resources/Images/News/BackstageInProcedure.png)
There you can make settings on procedure level. These are:
- Adding and deleting the procedure in the desktop component called Favorites.
- Configure the side panel
- Copy hyperlinks to the procedure and record in question
- Configure selection rows
- Administer default values in the selection
- Configure presentations (only in list procedures)
