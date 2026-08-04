### Activity templates

#### Type
Here you choose which type of template you wish to create. The following types are available: Inquiry, Purchase order, Blanket order – Purchase, and Supplier.
Templates

#### Default
Here you select which template should be default.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Name
Here you can write a descriptive text as a name. The name text is entered in the company language and is displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
Activities
In this box you select activities to the template that have you selected in the box above. You can also change the order of the activities. The activities which can be selected must be registered in the procedure Activities.

#### Number
Each activity will be given a consecutive number. The first activity is always given number one (1).

#### Name
The name of the selected activity. However, it is possible to change this name but the field cannot be left empty. We suggest you enter a name which is descriptive of what should be done.

#### Responsible
Here you can select a person responsible for the activity. The user linked to the logged-on user is displayed by default.

#### Reference
Loads the reference on the purchase order or inquiry as responsible for the activity. (Depending on if the activity template applies to purchase order or inquiry.)

#### Comment
Here you can enter a comment regarding the activity. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).
Here you can link external files to the activity. By clicking the Files button, it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic General features about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.

#### Due date
Registration date or Valid through date. The delivery date of the first order row will be entered as Valid through date.

#### Difference
Here you can enter a difference in work days from the due date. It is possible to enter a positive or negative difference.

#### Status
Here you can see the status of the activity. There are three different statuses: Not started (default), Started, and Finished. Finished activities are displayed in green text in the Activity field.

#### Reminder
The setting determines whether a reminder will be sent to the person responsible. The purpose is to inform the person responsible about the activity to perform. The message contains information about the part and activity in question, and when the activity should be performed. A hyper link to the part is also included in the message. The user in the conversation will automatically be set as the responsible user for the activity. If a reminder/message has already been sent, you see a small symbol of it next to the button.

#### Mandatory
Check this box for the activities that should be mandatory to perform.
Things to keep in mind when using activity templates
Values loaded from other places (Finish date and Responsible) are shown in italics. If you manually edit the value for an activity, the italic font is removed and the value must hereafter be changed manually.
A linked value on for example, responsible, can automatically be changed if it is loaded from Seller on the customer. When seller is changed, all linked open activities will be updated.
> Please note! There must be a link between the employee (who is used as seller or administrator) and a user. If such a link does not exist, or if the user cannot be selected as responsible for the activity, then the logged-in user will become administrator when the activity is created via the activity template. If the logged-in user is not allowed to be responsible for the activity either, then the activity will not be created at all.
It is not possible to link values in all templates, but for example in quote and on customer, it is possible.
