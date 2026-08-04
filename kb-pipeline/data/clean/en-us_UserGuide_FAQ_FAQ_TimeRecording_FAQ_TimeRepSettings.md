### FAQ – Basic data and settings for time recording
What settings do I need to enter to allow employees to clock in/out for breaks?
Flex zones for breaks must be specified in order for employees to be able to clock in/out for breaks. The flex zones are added to the schedule, and can be applied to breaks as required. In order for an employee to be able to clock in/out for breaks, flex time must be allowed in the employee’s parameter group. This can be checked in the Parameter groups procedure.
Why are no employees shown in the Schedule exceptions procedure?
It is most likely that you have forgotten to check the Show all I can adjust box before clicking Load ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png).
Where do I register bridging days and the like?
You can register bridging days by selecting Holiday for the days in question in the Calendars procedure under General registers.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/FAQTimeRecording4.png)](../../../../Resources/Images/UserGuide/FAQTimeRecording4.png)
In the Schedule cycles procedure, under the Holidays acc. to column, you can select the calendar number with your bridging days.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/FAQTimeRecording3.png)](../../../../Resources/Images/UserGuide/FAQTimeRecording3.png)
> Please note that all handling of payment days and production days is based on the standard calendar. With this in mind, it is a good idea to create a separate calendar for time recording.
What do I do when an employee leaves the company?
When an employee leaves the company and the final salary payment is processed, the employee should be blocked. This is done by checking the Blocked box in the Personnel records – Time recording procedure. You can also enter an end date here for the period of employment.
How can I delete an absence code which is no longer to be used?
It is not possible to delete an absence code which has been used previously. If you don’t want employees to be able to see and use the absence code any more, you can hide it in the Parameter groups procedure. Select the absence code/s to be hidden under Invalid absence codes.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/FAQTimeRecording5.png)](../../../../Resources/Images/UserGuide/FAQTimeRecording5.png)
How do I set up for managers to sign/authorize their employees?
Under the Signer tab in the Personnel records – Time recording procedure, you can set Main signers and Secondary signers of an employee. The users that you set in the System signer will automatically become secondary signers for all employees.
How do I set it so that a user will be able to access employees’ records in Authorize/Adjust recording?
If the user should be able to access all employees in the company, you can register the user as a System signer in the System signer procedure.
Can I set it so that we can only record attendance with a card and not record work?
If you are able to record attendance with a card, you will also be able to record work with a card. You are not able to deselect one of these. This is determined by the Only recording with card system setting.
How do I activate training mode in the recording terminal?
You need to activate the Enable training mode in the procedure Terminal settings system setting. You then need to activate Training mode in the Terminal settings procedure for the user in question. To start training mode in the Recording terminal, you use the shortcut Ctrl + Shift + D before entering the employee number.
How do I change the number of seconds before the recording terminal is cleared?
You enter the desired number of seconds in the Number of seconds before clearing of recording terminal system setting.
How do I get an automatic printout of drawings when someone starts work?
Automatic printing of drawings can be determined per work center (in Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register) or per employee (in Personnel records – Time recording) where you activate Automatic printing of shop packet and select Print files for the Travelers document. The drawing will then be printed automatically IF the drawing file linked to the part is selected for automatic printout. It is possible to link files to the main part, the part's revision, the operations in the BOM and routing, and the material in the BOM and routing.
The recording terminal is showing the wrong time, how do I change it?
Monitor ERP uses the time from your server. As the IT department to change the server’s time settings.
Our employees get the wrong salary type when they record overtime, where do I change this?
You change salary type on the overtime schedule in the Schedules procedure.
What do I need to do with the calendar and schedules before a new year?
In Monitor ERP you do not need to do anything with the calendar or schedule when it’s a new year. It will just continue as usual.
If an employee has a morning schedule and an afternoon schedule that will be every two weeks, are two schedule cycles needed?
No. You first add these two schedules in the same schedule cycle in the Schedule cycles procedure. You then select this Schedule cycle and start date (From) for the schedule cycle for the employee in the Schedule cycles box in the Personnel records – Time recording procedure. You then click the Days button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) and select whether it is week 1 or 2 that the employee begins the schedule cycle. A schedule cycle can consist of more than two schedules.
