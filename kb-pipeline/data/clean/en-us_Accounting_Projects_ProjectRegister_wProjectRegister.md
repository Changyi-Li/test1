## Project register
In this procedure you register and follow up on different projects. Project is a general term for different orders, income, costs, and hours. There are different types of projects, for example development projects, reconstruction projects, or manufacturing projects. You enter project number on manufacturing orders, when posting customer orders, etc. in order to link these records to the project.
[Read more about project accounting here](../../../UserGuide/Using/ProjectManagement/ProjectManagement.htm).
The projects you register in this procedure can be used for postings made in the system. A project cannot be deleted if there is data registered on it. For example, there may be transactions on the project or the project has been entered on, for example, orders, invoices, and so on.
Basic project information and functions
In this procedure you handle the basic project information. Here you find functions to:
- Register projects and adding basic project information
- Follow up on costs and income
- Follow up on the time recording made on the project
- Register budget and forecast
- Handle the phases and activities of the project
- Create dependencies between phases or activities
- Log e-mails and correspondence
- See an outline of the records registered on the project such as orders, invoices, etc.
- Handle project documents which summarize the project
Project calculation
When you load an existing project, a project calculation is automatically made in the background, for example if activities, costs or income have been reported in the project by another user while you had the project loaded in the procedure. The calculation will not take place for historical projects (except for projects which for example have been added via conversion and does not have a previous calculation).
Activities under Tasks
The project activities you register are sent to [Task](../../../UserGuide/GeneralFeatures/MessageCenter.htm#Uppgifter) in the Message center for the user who has been configured as responsible for the activity. If you have configured that the activity should send reminders, notifications about the activity will be displayed to the user who is responsible for the activity.
Link part to project
In the Part register procedure you can link parts to projects. This is done in the [Project](../../../Stock/Parts/PartRegister/bProject.htm) box. If you link a part to a project this will affect registration of rows on an order, on invoices, etc. If the part in question is linked to a project and the account is configured to handle projects, then the project will automatically be used on the row in the posting in procedures where you register orders, inquiries, invoices, and quotes. The project link on the part overrides all other logic for automatic entering of project on rows. For example if a project has been selected in the order header or in the posting matrix, a link on a part will override this.
> You need to allow the dimension named Project on your accounts. The settings for this are configured in the Chart of accounts procedure.
Main and sub-projects
In some large projects there might be a need to divide the project in several sub-projects to provide better clarity.
For main projects it is possible to:
- Register orders and report
- Book income and costs
- Register budget/forecast
- Handle phases and activities
It is possible to follow up on main projects and sub-projects separately, but it is also possible to follow up on a main project and include a total of the values of the underlying projects.
Save as
You can copy a saved project to a new project by using the function Save as with the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save_as.png) on the toolbar. A dialog will then open where you enter information about the new record and select what should be copied from the existing project. Comments and files, if any, will be included when copying if the header is copied.
If you use the function Save as on a main project, the copy will become a project. If you use the function Save as on a sub-project, the copy will also become a sub-project.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png)
