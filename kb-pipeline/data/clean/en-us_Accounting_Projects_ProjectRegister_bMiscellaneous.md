### Miscellaneous

#### Status
Here you see/select the status of the project. Status 1 Registered is used by default on new projects, unless the selected project type is not set to be inactive. In that case the status 6 Inactive will be used for the project.
The system will then automatically change the status of the project to In progress if any of the project's activities is reported as started or finished. The project is also set as "In progress" if a value occurs in the Planned or Result columns under the Costs/Income tab.
The system can automatically change the project status to Finished when all activities on the project have been reported as finished. This applies if the system setting Finish project automatically is activated.
A project with status Inactive, Finished, or Historical will not automatically get its status changed by the system as stated above.
When a project status is changed to Historical (this must always be made manually), you can no longer perform accounting on the project. You can perform accounting on a project up to and including status Finished.
Status Inactive can be entered manually for a project, for example if there are some uncertainties regarding the project. This way you can have the project "resting" for a while with the status Inactive. An inactive project can be excluded in reports. You can still perform different reporting items on an inactive project.
The status of a main project cannot be set to Finished or Historical if there are linked sub-projects with status In progress or Registered. However, it is possible to finish sub-projects where the main project is in progress.

#### Project group
The project group can for example be used as a statistics and follow-up term for different types of projects. The default option here is loaded from the selected project type.

#### Project category
Here you can enter a project category. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.

#### Project dimension (the field name is entered in the Posting dimensions procedure)
Project dimension is used to be able to group different projects to a "parent term" for reporting purposes in the accounting. The dimension group can be set by default during project registration if you have set a default dimension group per project type in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure. Dimension groups can be used as selection terms when you create accounting reports. You first register dimension groups in the Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure.

#### Priority
PriorityThe priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty. The default option here is loaded from the selected project type.

#### Cost mark-up
Here you enter the cost mark-up of the project in percent. This will be added to the project costs when calculating the project result. The mark-up can for example be used to cover the administrative costs. The default option here is loaded from the selected project type.
If you have entered an Exception from cost mark-up for a cost type in the Basic data – Project procedure, this will be applied for the specific cost type for which the exception was entered.
