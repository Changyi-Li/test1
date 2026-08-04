### The rejection codes table

#### Rejection code/Error code
Here you enter the rejection code/error code using a maximum of 6 characters.

#### Name
Here you enter a name text of the rejection code/error code. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Type
Here you select for which reporting items in the system the rejection code/error code should be available. The following options are available:
- Reporting – Manufacturing
- Receiving inspection – Purchase
- Customer nonconformity
- Supplier nonconformity
- Internal nonconformity
- 8D rejection

#### Mandatory comment
Here you determine if the user must enter a comment when selecting the rejection code/error code.

#### Only rejection
This setting is available if the option Machine integration is installed in your system. Here you determine if a rejection should affect the approved quantity or not. That is, if the setting is activated, it results in one rejected piece. If the setting is deactivated, it results in one rejected piece at the expense of one piece that earlier was reported as OK.

#### Automatic withdrawal of material
This setting determines whether the rejection code should automatically withdraw material when a rejection is reported on an operation. We recommend using this setting when using the Machine integration (MI) option.
In processes such as plastic injection molding where the mold has not been sufficiently filled, automatic material withdrawal is not appropriate. In such cases, the material can be re-melted or ground down and fed back into the machine.
However, if the material has become discolored during the injection molding process, it should instead be scrapped, and the setting Automatic withdrawal of material should be applied.

#### Active
Here you determine if the rejection code/error code should be active. This box is checked by default. If you deactivate a rejection code, it will be hidden in all places where rejection codes can be entered at reporting. However, it is possible to choose the deactivated code when selecting by rejection code. The purpose is to get statistics of previous reporting items.
