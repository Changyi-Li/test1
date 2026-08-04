### Grouping/Posting

#### Purchase order category
Here you can enter a purchase order category. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.
Purchase order categories can be of help when you for example load statistics from the order register.

#### Supplier group
Here you see the supplier group to which the order belongs. The supplier group selected for the supplier (in the Supplier register) is loaded by default. However, you can change supplier group for the order in question. Supplier group together with the order type's posting group determines the posting on order rows and is handled in the Posting matrix procedure.

#### VAT group
Here you see the VAT group to which the order belongs. The VAT group selected for the supplier (in the Supplier register) is loaded by default. However, you can change VAT group for the order in question. The VAT group determines which VAT code that by default is used on the order rows. This is registered in the VAT settings procedure.

#### Project
Here you enter the project to which the order belongs. If all purchase order rows should be labeled with the same project number, you can enter it in this field instead of on each order row. The project number is then shown in the project field of the posting on the order rows.
If you enter a project number of an order with existing order rows, you will be asked if the order rows should be updated with the entered project. If you enter a project number that does not exist already, you will be asked whether or not you wish to create the project. In that case you need to have sufficient user rights to be able to create a project.

#### Priority
Priority of the order can be 1 to 9, where 1 is the highest priority. By default, you will see the priority that is the highest, either the supplier's priority or the order type's priority. The priority field cannot be left empty for orders.
