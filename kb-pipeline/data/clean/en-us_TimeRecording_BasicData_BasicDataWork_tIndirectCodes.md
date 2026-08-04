### Indirect codes
Indirect codes are used for work recording of indirect work, for example during machine maintenance, cleaning, meetings, or when there is a waiting time caused be a machine error or tool error.

#### Code
In this column you see/enter the indirect code. It can consist of a maximum of 6 characters.

#### Name
Here you see/enter the name of the indirect code. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Reported as direct time
With this checkbox you decide if the code should be shown as direct time in statistics lists. Direct time for indirect work is seen as value-adding time, that is, the type of indirect work for which you can invoice customers.

#### Comment
In this column you determine if it should not be possible to enter a comment, or if it should be optional or mandatory, when you stop indirect work with this code. By default this is set to "Optional" for a new code.

#### Included in group
Here you decide in which group the code is included. You register groups under the Groups tab. This tab is available if you have installed the option Machine integration.

#### Employees
By clicking the Employees button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can, when needed, link personnel to the code in question. This setting is selective in a way meaning these persons can then only select among the codes to which you have linked them. It is possible both to manually add rows of personnel and insert records via Clipboard.

#### Excluded from follow-up
This is used for the option Machine integration. This setting can be used for codes such as "night rest" or "weekend rest" which are not affected by the arrival to the terminal and should be excluded from calculations of OEE. This setting is not activated by default.

#### Affects order
This is used for the option Machine integration. In this column you can select if the code for indirect work should affect unit time, setup time, or not affect these on order.
For a code that affects order, the time will be registered both as indirect time and unit time/setup time. This means that there will be double time for these records. This way, you can follow-up on the time used for a stop cause which has affected the order. When the time is registered on the order, it will also be registered as indirect time on the actual stop.

#### Color code
This is used for the option Machine integration. You can use the color code to group similar stops to show them in a certain color on TAK/OEE on the dashboard and in the machine terminal. Color codes can be selected any way you please for indirect codes.
