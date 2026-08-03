### Header row

#### Option list
Here you enter the code of the option list. It can consist of a maximum of 20 characters. If you enter a code which has previously not been used, then you can create a new option list. You can also select an existing option list in the field if you want to edit the option list. The option list code is shown in rules. That is why it is good if it is logically created.

#### Name
Here you enter a name/description of the option list or of the parts in it. It can contain a maximum of 80 characters. The name works as a heading for the option list when you configure for example a customer order.

#### Category
Category for option list can be used when creating price lists etc. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.

#### Comment and Files
Under the buttons Comment ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) and Files ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) you can enter a comment and link files which should be of help (as a description of the option list) during configurations.

#### Inherit options
With this setting you can activate an inherit function. This way selections made on an order row/quote row will automatically become selected for the next order row/quote row that is entered. You can also choose to include the quantity selected in the function. The following options are available:
- No
- Option
- Option and quantity
If, at a later stage, you change the option on an order row, you can choose if these changes will be inherited by other order rows.

#### Identifier
This field becomes mandatory if you activate the Inherit options setting.
For example, if you enter "Color" as Identifier, the options in this option list will be inherited on the following order row/quote row, providing there is an option list in this configuration which has "Color" as identifier. That is, it does not have to be the same option list or the same main part on the next order row/quote row. This can be useful, for example, if you have a door frame in a certain color, and in the following option list, for a door leaf, you want the same color to be inherited automatically.
The identifier for the option lists will link the different options lists, even if, as shown in the example, there are two different option lists for door frame and door leaf.
