### Dependency types
The procedures Direct project reporting, Report activity – Project, and the function Tasks, can all handle dependencies. Activities with one or multiple related preceding activities that are not finished, can not be started and will be filtered from the list. These will not be shown (cannot be reported on) until the related preceding activities have been finished/started.
The following dependency types exist between phases or activities:

#### Finished – Start
Activity B cannot be started until activity A is finished.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/RelationTypeFinishedStarted.png)

#### Started–Start
Activity B cannot be started until activity A is started.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/RelationTypesStartedStart.png)
> Please note! There is a limitation of dependencies, a project can either have dependencies between activities or dependencies between phases.
