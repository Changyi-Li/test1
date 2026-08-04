### Property management
By using the function Property management you can configure user rights on field level. An administrator (a user with the role of ERP manager or System administrator) here has the ability to configure different properties for checkboxes, fields, buttons, boxes, and tabs, and save this in property sets.
The administrator accesses this function by using the button Property management ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_property_management.png) on the toolbar in each single-record procedure and table procedure. When using the button, a property window opens where the administrator adds one or several Property sets and there select which users, groups, or roles each property set Applies to.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PropertyManagement.png)](../../../Resources/Images/UserGuide/PropertyManagement.png)
In a property set the administrator select an Object in the structure map (e.g. a field) and then select which Properties should be used on the object by checking the box A (Apply) and entering or selecting a Value for the property.
In the Filter field above the structure map, you can enter names for objects and use the filer so only these object will be shown.
A different method to select object is to use the button Select object in the procedure window ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_select_control.png) (Ctrl + F7). When the administrator clicks that button, the procedure window is placed in a property management mode. There the administrator then select an object by clicking on it. Objects possible to select are displayed with a red frame when you hover the mouse pointer over them. Once the administrator clicks on an object, the property management mode closes and the object becomes marked in the structure map.
A property set can be tested to see the result in the procedure in question. This is done using the button Test ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_test.png) for the marked property set.
Properties
The properties available to configure depend on the object. The properties described in the table below are all the available properties regardless of the object.
| Property | Object | Description |
|---|---|---|
| Text | Checkbox | Text value. |
| Heading | Checkbox, Field, Button, Box, Tab | Label, lead text, heading. |
| Hidden | Checkbox, Field, Button, Box, Tab | The object is hidden. |
| Protected | Checkbox, Field, Box, Tab | The object becomes inactive, but is shown. |
| Mandatory | Checkbox, Field | The object becomes mandatory to enter, fill in, select. |
| Default value for new record | Checkbox, Field | The object gets the default value which is entered or selected here. The property will only apply to new records that are created. |
> An object which is given a default value for new record via the property management (e.g. a field) always overrides any default values from system settings, settings on customer, supplier, part, etc.
Administer properties
Property sets created in different procedures can be centrally seen, modified, or deleted, by the administrator in the procedure Administer properties.
Normally, only administrators should have access to that procedure. This access is automatically granted via any of the roles mentioned in the opening paragraph in this topic. They will then also automatically gain access to the button Property management ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_property_management.png) in all procedures.
> The property management can today be used in single-record procedures (such as Part register and Register customer order) and in table procedures (such as Terms and Number series). Property management is not supported in list procedures (such as Part list and Operation list). In these procedures you instead have the opportunity to configure default values in selections and create own list presentations.
> In the Users procedure in the box User-specific user rights, it is possible to configure the user's user rights (Allow/Deny, Show/Modify) in fields. Today this function is only available in the Standard price field. This setting is configured in the section Field permissions. The user right configured will then affect all procedures in the entire system for the field in question.
