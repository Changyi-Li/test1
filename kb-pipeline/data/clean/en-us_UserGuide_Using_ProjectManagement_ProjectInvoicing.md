### Project invoicing
In this section we describe how project invoicing works in Monitor ERP and which settings need configuring before you can start using project invoicing.

#### Basic data – Project
The Project types tab
Under the Project types tab, you can link an order type to the project that should be used when invoicing. You can only choose order types of the New sales basic type. If the field is left empty, the order type that is set as default for your user in the Users procedure will be suggested. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectTypes_OrderType.png)](../../../../Resources/Images/TrainingMaterial/ProjectTypes_OrderType.png)
You are also able to choose to override settings at project level via the Order type for invoicing setting in the Project register procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectRegister_OrderType.png)](../../../../Resources/Images/TrainingMaterial/ProjectRegister_OrderType.png)
> In the Order types procedure you can configure settings for order types such as price strategy, rate type strategy, and posting.
> Please note that the setting Create invoice basis must be activated for the order type.
The Costs/Income tab
Under the Costs/Income tab you choose which costs should be invoiced and which part should be used on the invoice basis. The setting in the Invoicing column determines whether an invoice basis should automatically be created based on reports for the cost type. The following options are available:
-   
No – no invoice basis is created.
-   
Yes, cost price – an invoice basis will be created automatically, the suggested price will be the reported cost.
-   
Yes, price acc. to part – an invoice basis will be created automatically, the suggested price will be based on the linked part’s price lists. A part is chosen under the Part for invoicing column (see below).
In the Part for invoicing column, you choose which part should be used on the invoice basis. Only parts of the type Service can be selected. The invoice invoice bases’ posting is based on the part's product group.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Project_CostIncome_Invoicing.png)](../../../../Resources/Images/TrainingMaterial/Project_CostIncome_Invoicing.png)
> It is important that the dimension named Project is applied on the sales account that is being used, and that the correct income type is linked so that the income is displayed correctly in the project. These settings can be found in the Chart of accounts procedure.
The Activities tab
To automatically create invoice bases when reporting activities, the activities need to be linked with cost types. Please note that the cost types need to be set to be invoiced.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Project_Activities_CostType.png)](../../../../Resources/Images/TrainingMaterial/Project_Activities_CostType.png)

#### Personnel records – General
In the Personnel records – General procedure, you can create exceptions for the settings that are selected in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure for specific users. Using the Project exceptions button, you can create exceptions per cost type for selected user. Under the Part for invoicing column, you can determine whether a part should be selected by default on invoice bases. Under the Hourly cost column, you can enter whether another hourly cost should be used when the user creates reports linked to the cost type.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Project_Exceptions.png)](../../../../Resources/Images/TrainingMaterial/Project_Exceptions.png)
> If you need to create an exception for multiple users, you can use the Project exceptions list type in the Personnel list – General procedure.

#### Project register
The Add to existing order when invoicing setting determines whether rows should be automatically added to the order number when an invoice basis is released in the Release invoice basis – Project procedure. This setting is available if an order number is linked to the project.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectRegister_AddToExistingOrder.png)](../../../../Resources/Images/TrainingMaterial/ProjectRegister_AddToExistingOrder.png)

#### Direct project reporting
When reporting is registered in the Direct project reporting procedure, you are able to exclude the reporting in question from being invoiced. This is done by changing the Invoicing status from Ready to release for invoicing (which is the default option) to Not to be invoiced.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectReporting_InvoicingStatus.png)
If the invoice basis has been released for reporting, the invoicing status Invoiced is displayed. You can also see order and invoice numbers once the invoice has been approved.
If you have the Yes, cost price for Invoicing on the selected cost type, it’s the value in the Amount field which will be forwarded, i.e., the same amount shown as the cost of the project. The Amount field can be edited.
The date on the report will be used as the delivery date on the invoice basis.

#### Release invoice basis – Project
In this procedure you can release invoice bases from project reporting. The invoice bases are based on reports and additions that are registered via Direct project reporting, Recording terminal, or the TimeCard option.
> To release an invoice basis you need to activate one of the following user rights. With the user right Release invoice basis – Project, only own reportings, you can release invoice bases for your own reportings. To release invoice bases of other employees’ reportings, you need the user right Release invoice basis – Project, for all employees. It is also possible to choose Release invoice basis – Project, only project manager which will only allow you to release invoice bases of projects that you are the project manager of.
The list is updatable and you are able to edit e.g. part, quantity, price, and posting on rows.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Project_ReleaseInvoiceBasis.png)](../../../../Resources/Images/TrainingMaterial/Project_ReleaseInvoiceBasis.png)
Under the Release column, you select which rows you want to release and then click ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) Save. You also need to answer a control question before the invoice bases are released. In the Released invoice bases dialog window, a summary of invoice bases that have been released is shown with a link to the corresponding invoice bases in the Register invoice directly procedure. You can also edit or cancel the invoice basis should you need to. When canceling, the reports’ status changes and you can release it again.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Project_ReleasedInvoiceBasis.png)](../../../../Resources/Images/TrainingMaterial/Project_ReleasedInvoiceBasis.png)
