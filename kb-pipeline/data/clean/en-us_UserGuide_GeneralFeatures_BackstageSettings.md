### Settings
Under Settings in the backstage of the desktop you can make different personal settings.
Theme
Here you can select different themes with associated background image. You can choose from gray, blue, light, and a dark (beta) theme, based on your own personal liking or conditions of lighting. The default theme is gray.
There is also an option not to Show background image which you can use if you prefer a plain background.
Printouts
Here you settings regarding printing to printer.
- Include selection when printing the report – With this setting you determine if to, by default, include the selection you made in a list procedure and show it on the printed report/list.
- Include chart when printing report – With this setting you determine if to, by default, include the chart you configured under the Chart button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_chart.png) and show it on the printed report/list.
Use new printer dialog in these modules
Under this heading are settings regarding where the new printer dialog should be used. The default configuration is to use the printer dialog in all modules. But this can be deactivated module by module. Then the Windows printer dialog will be used instead for the deactivated modules.
Messages and reminders
Here you can configure settings regarding reminders for activities you should perform. The reminders for activities refer to Tasks for you to perform. You get a reminder to perform an activity each time you log on to Monitor ERP. This will appear until you have performed the activity. However, you should remember that a user can turn off the reminder for an activity. This is done directly for the activity in the affected procedure. In that case you will only see your activity to perform in Tasks.
There are a number of different activities in the system for which you can get reminders, see below. By default, reminders are activated for all different activities.
Activities you will receive reminders for
- SRM (Supplier)
- Inquiry
- Purchase order
- Part
- Case
- CRM (Customer)
- Quote
- Customer order
- Personnel
- Project
- Time recording
- Daily management
- Blanket order – Purchase
- Blanket Order – Sales
- Customer agreement
- Stock count – Approval
Notifications
- Backup – With this setting you decide if you should receive a notification if a backup in Monitor ERP fails.
If you have installed the option called Electronic Invoice Management (EIM), you can here also activate settings regarding reminders for EIM and also for being absent from authorization of invoices. The reminders for EIM refer to Tasks for you to perform.
> The settings below (and much more) can also be centrally configured for multiple signers in the procedure Authorization settings – EIM.
Messages in EIM
Controls whether – and how – the side panel with messages at the side of the invoice image is shown. The following options are available:
- Always
- If there are messages
- Never
Reminders regarding EIM
- Supplier invoice to authorize – If you are registered as a signer this setting is activated. Here you can then decide if you want to receive reminders for invoices you should authorize. This will then apply for the supplier invoices where you alone are registered as signer or are included in the authorization list or signer group. You will always get a reminder to authorize an invoice each time you log on to Monitor ERP. This will appear until you have authorized the invoice.
- Supplier invoice to final record – If you have the user rights to modify supplier invoices this setting is activated. Here you can then decide if you want to receive reminders for invoices you should final record. You will always get a reminder to final record an invoice each time you log on to Monitor ERP. This will appear until you have final recorded the invoice.
- Send reminder via e-mail – If you are registered as a signer this setting is also activated. Here you can then decide if you want to receive the corresponding reminders for invoices you should authorize, also sent to you by e-mail.
Absence from authorisation of invoice
- Activate absence – If you are a signer it is possible for you to, when needed, activate that you are not available to authorize invoices, for example when you are on vacation. Then the following three settings will become available, where you have to configure two of them.
- Forward to – Here you have to select which signer who should take over the authorization in your place. The authorization you should do henceforth will be forwarded to this signer for the time of your absence.
- Absence applies until further notice – Here you can activate that the absence will continue until you manually end it..
- Period of absence – Here you select the period of absence, unless you activate that absence applies until further notice instead.
General
Here you can make different general settings as described below.
- Show side panel in procedure window – If you check this checkbox the side panel will be displayed by default in the procedures which have side panels.
- Go to next field using Enter – If you activate this checkbox the cursor will jump to the next field in the tab order.
- Set focus in the record selector when saving – With this setting activated it means for example in the Part register procedure that the cursor will become placed in the Part number field in the header when you save, regardless of where the cursor was positioned when you saved.
- Always copy "From" to "To" in selections – With this setting activated it means that when you leave the From field the value you entered or selected in that field till be copied to the To field in list procedures.
- Open last used procedures during startup – Here you can select if the procedures you had open at the time you closed Monitor ERP should be opened the next time you start Monitor ERP. The available options are:
- Yes – The procedures which were open when you shut down Monitor will be reopened the next time you start Monitor ERP.
- No – No procedures will open.
- With dialog – A dialog box is shown where you can choose if you wish the procedures to open.
- When expanding procedure windows – Here you can select how the procedure window should behave when you maximize it: to cover the whole screen or to cover everything except the module menu. If the procedure window covers the entire screen you still have the opportunity to temporarily show the module menu by using the button Show the module menu (F9) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_module_menu.png) on the toolbar in the procedure in question.
- Fade background when dialog is shown – Here you determine if the procedure window in the background of a dialog window should be faded (less bright) when the dialog window is shown. This way the dialog window is emphasized in the procedure.
- Default warehouses – This setting is available if the option called Warehouse is installed. Here you determine which warehouses should be selected by default in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in different procedures. With this setting also you also decide form which warehouses you can show and load records using the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature in different fields. The available options are:
- Warehouse at login – This means the warehouse selected for you in the Users procedure.
- All – All warehouses in the procedures where you have at least permission to show. In the procedures where you only have permission to show, you will see the warehouse's name in italics in the warehouse selector.
- Enable dispatcher – Used by Monitor Support when troubleshooting.
- Use alternative date picker – Gives an alternate date picker on e.g. customer order rows. This is used by Monitor Support when troubleshooting.
- Insert a row when clicking in an empty table – Here you determine whether a new row should be inserted automatically when you click inside a table without rows.
- Activate extended touch screen support in daily management – Gives better support for touch screens in daily management.
- Use the following communication protocol – This setting determine which communication protocol should be used by your Monitor ERP client for the communication with the application server. The available options are HTTPS and WebSocket. The WebSocket protocol is selected by default. If Windows 7 is installed on the client computer, then HTTPS is default.
- Show company number/name in procedures – Here you can choose if company number, company name, or both, should be displayed on the title bar in procedures, or if it should not be displayed at all.
- Online help region – determines the online help domain (per region) that will be used. The available options are:
- Auto – determined by the (default) installed country package. For the Chinese country package, the domain help.monitorerp.cn is used. For other country packages, the domain help.monitorerp.com is used.
- Global – The domain help.monitorerp.com is used regardless of the country package installed.
- China – the domain help.monitorerp.cn is used regardless of the country package installed.
