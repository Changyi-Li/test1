### General

#### Language
Determines the language to be used in Monitor ERP when the user in question starts the program. The default company language is suggested when new users are created. Internal documents and lists that are printed from Monitor ERP will also be displayed in this language. You can select among the languages that Monitor ERP is translated into and which are active in the Languages procedure.

#### Regional formats
The selected regional format is saved in the user profile and is used to format and display dates, time, decimal separator (period or comma) for numbers and amounts in Monitor ERP. Only regional formats supported by .NET on the server will be shown.
Please note! After a change has been made to the regional format, you have to restart the client for the change to take effect. Log out and log back in again.
The following fallback behavior applies:
- If no regional format has been selected, the regional settings in the Windows client will be used.
- If a previously saved regional format is no longer available, the system will reset to the standard format.

#### Warehouse
This applies if the Warehouse option is installed. The warehouse to which the user shall belong. See also [User rights according to warehouse](bUserRightsAccordingToWarehouse.htm).

#### Employee number
If the user should be linked to a person, here you select the person's employee number. If the person in question is linked to another user, you cannot link the user to the person. You also receive a message about this.

#### Can be used as responsible for activity
Determines that the user can be set as responsible for different activities.

#### Allow modification of procedure instructions
Determines that the user is allowed to write new instructions in procedures as well as modify existing ones. If this setting is activated it means the user has access to Instruction in the backstage of the procedure, otherwise this section is not shown.

#### Export activities to calendar program by default
Here you determine if the user's activities should be exported to Outlook calendar program. You must then enter the User name (Exchange) and Password (Exchange) in the E-mail section. Please note! This setting does not apply to project activities.

#### Load sub-projects in Project register by default
With this setting you decide if sub-projects should be loaded when a main project is loaded in the Project register procedure.

#### Voucher number series
Determines the voucher number series selected by default when the user creates a new voucher.

#### Default order/record types
By clicking this button you access settings regarding different default order types and record types for the user in question. These will then be default when the user creates new records in the register in question.
These settings are not configured from the start. Then the system remembers which type the user used the last time in the single-record procedures in question and suggests this type the next time. However, if you configure a default type for the user, this type will always be suggested by the system.
Different order types for quote, customer order, purchase order, inquiry, and customer agreements, etc. should be registered in the Order types procedure. Case types are registered in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Case procedure. Project types are registered in the Basic data – Project procedure.
> The user for whom you have changed order types/record types must restart his/her Monitor client for this to apply.

#### Default delivery address
By clicking this button you access a window where you can select a default delivery address for the purchase order created by the user. The address will then be used by default when the user creates purchase orders from any of the procedures Register purchase order, Purchase order suggestion, Stock refill – Purchase, Requirement calculation, or from the Planning window in the Part register procedure. The address is also used when the user creates a purchase order, from customer order in the Register customer order procedure, and from manufacturing order in the Register manufacturing order procedure. By using the Clear button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) you can delete the default delivery address.

#### Capacity for project activities
By clicking this button you can choose how capacity for project activities should be calculated for the user in the Loading plan – Project procedure.
The According to schedule option calculates capacity based on the user’s schedule. In order to use this option, time recording must be used and the user must be linked to an employee number. If you choose this alternative you can also enter an Availability factor. There you enter how many percent of the calendar time (the schedule) that is available for project activities. The capacity calculation will also take planned absence for the user into consideration.
With the Fixed capacity option, the capacity is calculated based on the number of hours per work day that you have entered in the field called Work day capacity. If you for example enter 5 hours, it means the user is assigned 5 hours capacity per work day.
> Capacity for project activities can also be shown and updated in list form in the list type called General in the User list procedure.

#### Show new messages at login
With this setting you decide where your new chat messages from Monitor chat should be displayed.
The following options are available for Show new messages at login:
-   
Login – New chat messages will be shown when you start Monitor ERP. If you have received a new chat message, a red symbol with an exclamation mark is displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_messagecenter_message.png) on the Message center button. You will also receive a notification displayed for a few seconds at the bottom right corner of the program window.
-   
Recording terminal – New chat messages will be shown in the Recording terminal procedure. You find them by clicking the Chat messages button. If you have received a new unread message, the inbox will open automatically when you have entered your employee number. A notification on the button will also display the number of unread chat messages.
-   
Both – New chat messages will be shown both when you start Monitor ERP and in the Recording terminal procedure. You will also get notifications about new chat messages in both places.

#### Block
You can enter a block for a user. The following alternatives exist for Block:
- None/Cancel (default) – No block will be shown, alternatively it has been canceled.
- Block – In a window you select that the user should be blocked from logging in. It is mandatory to enter a cause text. When this is activated you can use the padlock button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png) next to the field to open the window and change cause text. Below the field you can see who has created the block and when. The symbol for Block is also shown in the field for the user name on the procedure’s main row. The user name is also displayed in red and bold font.
In the Block window, you find the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png). Using this you can link files to the block.
If a cancellation has taken place you can see information about this below the field. The ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right accesses an event log containing previous blocks.

#### Monitor News – Areas of interest
In order for you to receive as relevant information as possible in the Monitor News feed, you can select your areas of interest here. You choose areas of interest with the Roles/Areas and Countries settings. You will then get a new feed with content aimed at the country and role/roles you selected.
