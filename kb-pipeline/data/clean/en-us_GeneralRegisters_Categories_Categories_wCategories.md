## Categories
In this procedure you create rules regarding what the user should be able to enter and select in category fields in the system. The purpose of this is to guide or make sure that the users fill in categories correctly according to the company in question.
In Monitor ERP there is support for categories for records of the following types:
- Part
- Customer
- Supplier
- References for customers and suppliers
- Project
- Fixed assets objects
- Case
- Personnel
- Quote
- Customer order
- Inquiry
- Purchase order
- Account
- Manufacturing order
- Option list
- Work center A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations..
The records above will now be referred to as category types.
A category field for a category type can contain a maximum of 20 characters. The length is decided by what is entered in the Length field which can be set to a value from 1 to 20. The category field can be described as a field with maximum 20 fixed positions where each position can be given a specific meaning.
You can choose to not use categories at all, to just add one category per category, or to select the type called Optional. Regardless if you have selected to apply categories or not, you can leave the category field on records empty.
The strength of categories in Monitor ERP is that you can create rules with category items containing optional or mandatory selection lists for each category type. In these selection lists you add values. The user can then, via the Category selection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button, choose from these values in the category field in order to create an entire category. This button is also available when selecting by categories in list procedures.
For each category type, you can add several category items containing one selection list each. For the Customer category type you might select one category item with selection list for region/area, one category item for selection list for business, etc. For the Part category type you may want to have category items with selection lists for different variants of the part, such as, material, surface finishing, alloy, color, etc.
In the image below you see how you can create category types according to the Part example above. Click the image to enlarge it.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/categories_selection_list.png)](../../../../Resources/Images/SubProjects/categories_selection_list.png)
The Part category type in the example has four category items for material, surface finishing, alloy, and color. Each category item has the length set to 1.
The first category items are of the Selection list (mandatory) type. This means a user can enter or select a value from the selection list in the category field for the part. If you enter a value, it must be a value available in the selection list, otherwise a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will appear in the category field.
The forth category item is of the Selection list type. This means the user can enter any value in the category field, but it cannot contain more characters than what is specified as allowed for the category item.
In the example, 4 positions are used out of the 20 that are available for the category field. That is, there are 16 available positions for category items to be added in the future.
In the image below, you see how a part is categorized by using the four category items in the image above. The categorization indicates that it is a part made out of aluminum (position 1), anodized (position 2) in wrought alloy (position 3), in black color (position 4).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/category_field.png)
> Tip! Use as short length as possible for each category item. If you enter length 1 for each category item (as in the example above), you can use up to 20 different category items per category type.
