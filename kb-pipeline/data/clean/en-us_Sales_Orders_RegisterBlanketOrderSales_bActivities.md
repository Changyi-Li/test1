### Activities
Using the button Add activity template ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_template.png) you can insert an activity template created in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – CRM. In the Order types procedure you can choose a default activity template for each customer order type/quote type.
Things to keep in mind when using activity templates
Values loaded from other places (Finish date and Responsible) are shown in italics. If you manually edit the value for an activity, the italic font is removed and the value must hereafter be changed manually.
A linked value on for example, responsible, can automatically be changed if it is loaded from Seller on the customer. When seller is changed, all linked open activities will be updated.
> Please note! There must be a link between the employee (who is used as seller or administrator) and a user. If such a link does not exist, or if the user cannot be selected as responsible for the activity, then the logged-in user will become administrator when the activity is created via the activity template. If the logged-in user is not allowed to be responsible for the activity either, then the activity will not be created at all.
It is not possible to link values in all templates, but for example in quote and on customer, it is possible.
There are function buttons you can use to add/remove activities and to show activities which have the status Finished.

#### Number
Each activity will be given a consecutive number. The first activity is always given number one (1).

#### Activity
Here you select an activity. Activities must first be registered in the Activities table in the Basic data – SRM procedure.

#### Name
Here you see the name of the selected activity. However, it is possible to change this name but the field cannot be left empty. We suggest you enter a name which is descriptive of what should be done.

#### Planned date
Here you select the date when the activity should start. Today's date is shown by default. The date will be displayed in red if it is in past time.

#### Responsible
Here you select a person responsible for the activity. The user linked to the logged-on user is displayed by default.

#### Purchase order
Select an order number if the activity belongs to a purchase order.

#### Reference
The reference you enter here shows who the person responsible for the activity should, for example, call or meet with. By clicking the button to the right ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can access information added regarding the reference, such as phone numbers etc. If you have selected a purchase order, the Reference will be loaded automatically from that order.

#### Comment
Here you can enter a comment regarding the activity. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
Here you can link external files to the activity. By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.

#### Status
Here you can see the status of the activity. There are three different statuses: Not started (default), Started and Finished. Finished activities are displayed in green text in the Activity field.

#### Reported date
Here you can manually select a date for when the activity was reported. This field will become automatically filled with today's date when the activity status is set to Finished.

#### Performed by
Here you can select the user who performed the activity. This field will automatically be filled in when the status is set to Finished. The user linked to the logged-on user will be entered by default.

#### Reminder
This setting determines whether or not a reminder will be sent to the person responsible. The purpose is to inform the person responsible that there is an activity to perform. The message contains information about the supplier and activity in question, and when the activity should be performed. A hyper link to the supplier record is also included in the message. The user in the conversation will automatically be set as the responsible user for the activity. If a reminder/message has already been sent, you see a small symbol of it next to the button.

#### Calendar
Here you determine if this activity should be synchronized with a calendar program. A calendar record is then created for the activity in the responsible user's calendar program. When you have activated this setting you can also configure Calendar settings.
When Calendar is activated, a check is also made to make sure there are e-mail settings in the system, and settings for the user who is set as responsible for the activity. If any information is missing for e-mail settings in the system or for the user, a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is displayed in the column. A tooltip for the symbol informs you of what information is missing.
E-mail settings
- In the Users procedure, in the E-mail section, the settings: E-mail address, User name, and Password, should be configured. The setting E-mail method can be set to Client based, via Microsoft Outlook if the user wants to use Outlook locally for calendar synchronization and to send e-mails.
- In the System settings procedure, in the E-mail section, under the System overall tab, you will find: E-mail sending method, Server address (Exchange/Exchange Online), Port (Exchange/Exchange Online), and Use SSL (as Yes or No, depending on whether or not the e-mail server requires it).

#### Calendar settings
If the setting Calendar is activated, you can by clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) configure calendar settings for a meeting which should be linked to the activity. In the dialog shown you configure Location for the meeting and Duration in hours, and add e-mail addresses to Participants in the meeting. An e-mail with a summons is sent to those addresses when you save the activity.
The Include reference contact information setting is activated by default. This will display information about the reference in the calendar record. This setting is available for activities on quotes, customer orders, inquiries, and purchase orders. The informations shown is loaded from the register entry to which the activity is linked.
