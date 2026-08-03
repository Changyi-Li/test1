### General
This box contains general information about the part selected in the structure in the Navigation box.

#### Part number
Here you see the part number of the part.

#### Name
Here you see/enter the name of the part. This field is mandatory for a new part. You can edit the name text for an existing part by clicking the "padlock" button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) to the right in the field. You enter the name in the company language. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Part type
Here you select the type of the part. The default part type for a new part is Manufactured. In a BOM and routing you can also create purchased and fictitious parts.

#### Production engineer
Here you select a production engineer who is the person responsible for the part's BOM and routing. You can select a person from the personnel records. The name is shown in the field to the right. Click ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to see more information about the person.

#### Drawing
Here you enter the part’s drawing number. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button, you can add drawing numbers in a table.
For each drawing number you can add drawing revisions and enter which of these should be the active revision. Click the Revision button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the row of the drawing number to select which should be active. Please keep in mind that it is the drawing number on the top row in the table that is shown in the field. You should place the "most important" drawing or, for example, the summary drawing at the top.

#### Revision
Here you see the revision of the part. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button, you can add part revisions in a table. You can enter which revision should be active, enter from which date the revision applies, enter a revision comment, and link files.
The part's revision is a term which can be selected for operation rows and material rows when using alternate BOM and routing.

#### Status
There are seven different statuses for a part. These reflects a part’s life cycle (and an additional status for inactive parts) as seen in the status stages in the table below:
| Symbol | Code | Name |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeFictitious.png) | 1 | Quote |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypePrototype.png) | 2 | Prototype |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) | 3 | New part |
|   | 4 | Normal |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeUpgrade.png) | 5 | New revision |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDowngrade.png) | 6 | Phasing out |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDeleted.png) | 9 | Obsolete |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png) | 99 | Inactive |
The different part statuses are fixed. It is not possible to add or delete a part status. The status of a part is shown, for example, on order rows. You can select by the part status in different lists.
New parts will get a default part status which is determined using the system setting Default part status for new part.
The part's status is a term which can be selected for operation rows and material rows when using alternate BOM and routing.

#### Balance
Here you see the part's total balance for the warehouse you are in.
The part's default unit is shown to the right of the balance field. BOM and routing is always created in that unit. This unit is, unlike the balance, common for all the warehouses.

#### Comment
Here you can enter/see a manufacturing comment. It is the same comment that you can enter under the Manufacturing tab in the Part register procedure. This comment will be printed on the manufacturing order documents.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
Here you see files linked to the part. These will be printed together with the manufacturing order documents. The files can also be linked under the Manufacturing tab in the Part register procedure.
Viewing of PDF files is supported.Using the option Extended file viewer you can view/show more file types, such as different drawing formats and Office formats. By clicking this link you access a complete list of the [supported file formats](https://www.rasterex.com/file-formats?hsCtaTracking=f7142bf7-4cfa-4c3b-8be8-cde24df7f2b4%7Cdae7ecbb-26b0-43cd-b9d0-3579248ec31b).

#### Calculation mark-up
Under this button, you can select general calculation mark-ups for the part or select exceptions. These must first be registered in the Calculation mark-up procedure. For a purchased part, the SO mark-up field is the only field available. For manufactured parts, there are fields for SC mark-up, Sales OH, and Profit. No calculation mark-ups are available for fictitious parts. General calculation mark-ups are selected by default.
Exceptions for calculations mark-up can be either SC, SO, or both.

#### Calculation date of standard price
Here you can see the date when the standard price was saved. By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png), you can open the calculation that was made then.

#### Net weight
In this column you see the part's net weight. By using the Calculate weight button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) the weight can be calculated as the total of the net weights of the incorporated material rows. This weight calculation can also be made for multiple parts at a time in the list in the Calculate weight procedure.

#### Fixed weight
By activating this setting you decide that the part's net weight should be fixed and the recalculation will not automatically be saved by default in the Calculate weight procedure. Fixed weight is used, for example, for parts processed from a raw material where the finished product's weight is lower than the weight of the total material. For these parts you manually enter the net weight and it will not be overwritten during the next calculation.
However, for a part where Fixed weight is activated it is possible to calculate the weight and save it here or in the Calculate weight procedure.

#### Filter terms
By clicking the Filter terms button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can configure a filter for terms selected for the operations and materials incorporated in the part. You also select if the filter should be activated and you can choose which parts of the filter that should be active. You can filter by the different terms available to select for operations and material.
When the filter is active, all operation rows and material rows not fulfilling the filter will be hidden. This is useful if you only want to see the operations and materials concerned for a certain term. It is also useful when calculating the part's net weight since it is only the material rows shown when a filter is active that will be included in the calculation.
