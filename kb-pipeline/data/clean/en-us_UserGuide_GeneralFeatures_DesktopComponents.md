### Desktop components
In this topic you find descriptions of the desktop components included in Monitor ERP. These are used to create desktop configurations.You can create your own desktop configuration under Desktop in the backstage of the desktop. An administrator can create templates for desktop configurations (which multiple users can then use directly). You create these templates in the Desktop templates procedure.
> Even though you can add any component in a desktop configuration you need to have the right to show/see the specific data which the component displays. Otherwise, the component will not be shown on the desktop. Read more under each component to find out if it requires a certain user right to be used.

#### Component list
Open procedures
This component shows your open procedures as thumbnails.
By clicking on a thumbnail in the component, that procedure window will be shown.
Favorites
This component shows the procedures which you have saved as favorites. You can save a procedure as a favorite by using the Favorites button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_favorites.png) on the toolbar in the procedure you wish to add as favorite.
By clicking on a procedure name in the component that procedure will open.
When you add your favorite procedures in the Favorites component you can also link the procedures to default values, if needed. A tip is to add some information about the default value in the Name/Path column in the settings for the component. This way you can easily see which default values the procedure is opened with. You can add the same procedure several times in Favorites but with different default values.
Bulletin board
This component shows the bulletin board which you select in the settings of the component.
In the Edit bulletin board procedure you update the contents that should be shown to users on the bulletin board.
Inbox Monitor-to-Monitor
This component shows the e-mail inbox used for incoming e-mails of the type Monitor-to-Monitor. You can drag e-mails of this type directly from your e-mail program and drop it on the inbox. Then the attached XML file will be loaded and the order registration procedure is automatically opened. In the procedure Settings for incoming e-mail and in the procedure Users, it is possible for the administrator to configure that incoming e-mail of this type automatically will be sent to this inbox for different users.
In the component there are buttons with which you can import XML files to orders and invoices in Monitor ERP, update the inbox, delete e-mails from the inbox, as well as see the text in e-mails received. Read more about [Monitor-to-Monitor](M2M.htm).
Inbox e-invoice/XML
The component called Inbox e-invoice/XML displays the e-invoices/XML files which have been received. The component shown the XML inboxes which are registered under Paths for inboxes in the Scan supplier invoices procedure.
If you have received invoices, you can start the import by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) or double-clicking on the row. You can start downloading from the operator’s server manually by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png). Click ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) in order to preview the PDF invoice.
Status of outgoing e-invoices
The Status of outgoing e-invoices component shows the invoices which have been sent to CrossState. This component's settings determine for example how often the information should be updated and what status level of the invoices should be shown.
Order inflow – Blanket order
This component is a gauge showing the order inflow for blanket order in relation to the order inflow for the same period of the previous year. The order inflow is shown in percent and is based on data from the database in Monitor ERP. The settings of the component will for example determine which type of gauge to show and for which selected data, and also which period to measure.
The settings are the same as in the Order inflow – Blanket order procedure except the Group by setting. Grouping Acc. to system settings is based on the settings under Order inflow under the Sales tab in the System settings procedure.

#### Group by
- Log date – if the presentation Grouped by log date is selected, the order inflow will be displayed by log date.
- Order date – if the presentation Grouped by order date is selected, the order inflow will be displayed by the order date of the order rows.
- Date as per system settings (default) – dates are loaded as per the New order inflow, New order inflow at delivery, and Changed order inflow system settings.
Budget deviation analysis – Customer
The Budget deviation analysis – Customer component compares the customer budget with the result. It corresponds with the list type called Budget deviation analysis – Customer in the Invoicing log procedure.
Order inflow – Chart
This component displays the order inflow’s amount as a chart. The settings of this component determine, for example, which type of chart that will be displayed. You can choose to also display the amount of previous years as a comparison. The component can be grouped by Log date or Order date. You can choose warehouses from which data should be displayed. The order inflow is based on data in the company database in question. You can choose to include orders from the customer orders, deliveries, and invoices. You can also include preliminary customer orders, show order inflow for deleted customer orders, and show called order rows.
Grouping Acc. to system settings is based on the settings under Order inflow under the Sales tab in the System settings procedure.
If you double-click the chart, the total list in the Order inflow procedure will open and use the same settings as in the component.
The Show order inflow user right is required to be able to use the component.
Order inflow
This component is a gauge showing the order inflow in relation to the order inflow for the same period of the previous year. The order inflow is shown in percent and is based on data from the database in Monitor ERP. The settings of the component will for example determine which type of gauge to show and for which selected data, and also which period to measure.
The settings are the same as in the Order inflow procedure except the Group by setting. Grouping Acc. to system settings is based on the settings under Order inflow under the Sales tab in the System settings procedure.

#### Group by
- Log date – if the presentation “grouped by log date” is selected, the order inflow will be displayed by log date.
- Order date – if the presentation “grouped by order date” is selected, the order inflow will be displayed by the order rows’ order date.
- Date as per system settings (default) – dates are loaded as per the New order inflow, New order inflow at delivery, and Changed order inflow system settings.
Order inflow – Old BI
This component is a gauge showing the order inflow in relation to the order inflow for the same period of the previous year. The order inflow is shown in percent and is based on data from the business intelligence database. The settings of the component will for example determine which type of gauge to show and for which selected data, and also which period to measure.
In order for this component to show current information, data mining must regularly be performed in the Settings for BI procedure.
If you double-click the component on the desktop the procedure BI – Sales will open with the data source Order inflow selected and with the same settings as in the component.
The user right Show Business intelligence – Sales is required to be able to use the component.
Budget deviation analysis – Part
The Budget deviation analysis – Part component compares the part's budget with the result. It corresponds with the list type called Budget deviation analysis – Part in the Invoicing log procedure.
Planned deliveries
The Planned deliveries component shows delayed and future deliveries for customer orders depending on the settings you configure. The default setting is to display customer order with a delivery date in the interval from yesterday and 5 days ahead. You can change the settings to have the component show only delayed deliveries or only future deliveries, if this suits you better. The component can be added to your desktop with different names and settings, so you can follow up on the deliveries that you are interested in.
Budget deviation analysis – Seller
The Budget deviation analysis – Seller component compares the seller’s budget with the result. It corresponds with the list type called Budget deviation analysis – Seller in the Invoicing log procedure.
Budget deviation analysis table – Seller
This desktop component displays the budget for and result of the current year for the selected seller. The table is grouped by month.
Delivery reliability
This component is a gauge showing our delivery actual reliability to customer in relation to all deliveries made on time during the same period of time. The delivery reliability is shown in percent. The settings of the component will for example determine which type of gauge to show for which selected data. You also decide the interval of delivery dates for which to measure the delivery reliability, and if the delivery reliability should be measured on delivery rows or customer order rows.
If you double-click the component on the desktop the total list in the procedure Delivery reliability will open, with the same settings as in the component.
The Show delivery reliability user right is required to be able to use this component.
Future delivery reliability (index)
This component is a gauge displaying the company's expected delivery reliability to customer. This is calculated using the difference between order confirmed delivery date and New finish on order row for the yet not delivered customer order rows. New finish (Earliest delivery date) is calculated via the procedure Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts.. The settings of the component will for example determine which type of gauge to show and which selected data. You also decide the horizon for which to calculated for the delivery reliability. This horizon also includes the undelivered order rows where the order confirmed delivery date is already in the past. The delivery reliability is shown in percent.
If you double-click the component on the desktop the list Future delivery reliability – Total in the Delivery reliability will open, with the same settings as in the component.
The Show delivery reliability user right is required to be able to use this component.
Invoicing log
This component displays the invoicing log as a chart. You can group the invoicing log by invoice date or by customer. When grouping by invoice date, the component corresponds to the list type Total with presentation Total by invoice date in the procedure Invoicing log. You can choose for only main rows to be shown, and if you want a comparison with the previous year.
If you double-click on the chart the total list in the procedure Invoicing log will open, with the same settings as in the component.
The user right Show sales statistics is required to be able to use the component.
Future delivery reliability
This component shows the company's expected delivery reliability to customer in chart form. The component corresponds to the component called Future delivery reliability (index).
The Show delivery reliability user right is required to be able to use this component.
Tasks – Activities
This component shows tasks as different activities where you are registered as responsible for the activities. The settings of the components determine which types of activities will be shown.
With the Show future activities ready to start setting you decide if only activities that are planned within your planned Time horizon will be displayed. Activities planned for a time further in the future will not be shown.
When you activate Show future activities ready to start, you will also see project activities outside the time horizon, but only those that are actually ready to start now.
In order for a future project activity to be displayed, all of the following conditions must be met:
- The activity is a project activity (other activity types are not affected by this setting).
- The activity has dependencies to other project activities.
- All preceding activities have been finished or meet the requirements of being started, which means that nothing is blocking the activity.
- The activity is assigned to the logged in user and is not finished.
Project activities without dependencies are never shown, regardless if the setting is activated.
Preceding activity finished determine if only activities ready to start will be shown. This helps make sure that the work is performed in the correct order and makes it clear for you what is next to be done in the process.
If you double-click on an activity the activity will be shown in Tasks in the Message center.
Tasks – EIM
This component is designed for the option Electronic invoice management (EIM) and shows tasks to carry out regarding supplier invoices in the EIM flow. You can see if you have invoices to authorize or final record. The invoices are the ones where you are signer or where you have the user rights to final record supplier invoices. If you would like to see which invoices you have to authorize or final record in the desktop component, you need to check the Supplier invoice to authorize and Supplier invoice to final record checkbox under Reminders in the Authorization settings – EIM procedure. You can also configure the component to link to the Tasks window. The component also has a setting where you can select if the task Authorize, Final record, or both, should be shown.
If the checkbox "Link to the Tasks window" is activated, you can double-click a task and it will open under the EIM tab in the Message center. There you can then choose to preview the invoice and open it in the concerned procedure.
Tasks – Absences
This component is intended for signers and shows which employees have planned absence that still has not been approved. You are able to select Update interval and a Time horizon in days. You can also choose to show employees For which I am main signer­ or Show all I can adjust.
Invoice overview – EIM
This component displays EIM statistics. It also shows some additional statistics for those who use EIM Workflow. The component is divided into the following sections: Current EIM status, Import overview, Company statistics, and a chart.
In this component you do not do any selections. Only configure regular component settings such as update interval and period setting where you choose among the options 30, 90, 180, and 365 days.
Approve purchase order
This component is used so to give the signer/approver a quick overview of the purchase orders he/she should approve. The order number is displayed as well as which position needs to be approved. Part number and name are also shown.
Cash flow forecast – Table
This component is based on the data presented in the Cash flow forecast procedure and provides a table overview of future cash inflows, outflows, and balance. If Bank integration is being used, the bank balance is automatically loaded into the forecast. The settings in the component are for the most part the same as the settings in the Cash flow forecast procedure.
Cash flow forecast – Chart
This component is based on the data presented in the Cash flow forecast procedure and provides a quick visual overview of future cash inflows, outflows, and balance. If Bank integration is being used, the bank balance is automatically loaded into the forecast. The settings in the component are for the most part the same as the settings in the Cash flow forecast procedure.
Control of basic data for parts
This component checks basic data for parts to find data with problems or where data is missing. Such problem might for example be when all purchased part should have at least one supplier link. This component will then show the number of purchased parts which are missing a supplier link. Parts with missing data or problems are shown as result rows total by type of control. The settings of the component determine which parts should be controlled and which controls to perform on them.
If you double-click a result row in the list, a selection/Clipboard becomes created for these parts and it is loaded in the Part list procedure. There you can then update the basic data for the parts if you have the user right Modify part. The selection of parts that have been created can also be used in single-record procedures (as e.g. BOM and routing or Part register), via Filtering ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search_form.png) on the procedure's toolbar.
The Show part user right is required to be able to use this component.
Loading plan
This component shows the chart of the loading plan with loading and capacity. You also see total lag and total horizon. The settings of the component determine for example which work centers and manufacturing orders to include. The other settings are the same as those existing in the procedure mentioned below.
If you double-click in the component on the desktop the procedure Loading plan will open, with the same settings as in the component.
The Show manufacturing order user right is required to be able to use the component.
Overloaded work centers
This component shows the work centers which are overloaded within a certain time ahead, starting now. There are two types of overload, they are shown as a yellow and a red symbol. The yellow symbol means the work center has a load of more than 100% for one or several weeks or days within the selected time. This overload is temporary and can be solved by doing the work at another time. The red symbol means the work center has a negative accumulated difference for one or several weeks or days within the selected time. This is more serious since it means the hours in total will not suffice.
If you double-click a work center the procedure Loading plan will open with the work center loaded and with the same settings as in the component.
The Show work center user right is required to be able to use the component.
New customers
This component shows the customers which most recently have become actual customers (status 1). The date when a customer became an actual customer is saved and that date is shown in the component. The settings of the component for example determine if a maximum number of actual customers should be shown or if you want to display the customers which have become actual in a specific number of recent days. If you double-click a customer the procedure Customer register will open with that customer loaded.
New parts
This component shows the most recently registered parts and have received status 3 (New part). The date when a part received status 3 (New part) is saved and that date is shown in the component. The settings of the component for example determine if a maximum number of new parts should be shown or if you want to display the parts which have status 3 in a specific number of days back in time. You can e.g. Sort by a certain part type or a certain administrator. If you double-click a part the part register procedure will open with that part loaded.
Website
This component is a web browser. You can in the component navigate on the web page configured as start page in the component. In the component there is also a Home button you can use to go back to the start page, and a button used to open the website in your standard browser. There are also settings regarding the X and Y position (entered in number of pixels), meaning where the component will be positioned on the website.
Ledger summary
This component provides a summary of how the company is doing based on invoices in both accounts receivable and accounts payable. In the component you see the number of invoices and remaining amount. This is shown in total as accounts receivable and accounts payable, and how large share there is of overdue accounts receivable and overdue accounts payable. The settings of the component determine the selection of customers and suppliers as well as which overdue invoices to include. Regarding the overdue invoices you can select among overdue credit invoices (customer or supplier), overdue interest invoices, and blocked invoices.
If you double-click on a row of overdue customer invoices the procedure Accounts receivable list will open. If you double-click on a row of overdue supplier invoices the procedure Accounts payable list will open.
Overdue customer invoices
This component displays a list of overdue customer invoices. It shows customer number, customer name, overdue amount, and the number of overdue invoices. At the bottom of the component you also see the total overdue amount. You can make selections and configure if debit invoices, credit invoices, or both, should be included in the list.
Overdue supplier invoices
This component displays a list of overdue supplier invoices. It shows supplier number, supplier name, overdue amount, and the number of overdue invoices. At the bottom of the component you also see the total overdue amount. You can make selections and configure which invoices to include in the list. You can choose to include registered invoices, preliminary recorded, and/or final record invoices.
Bank account info
This desktop component can be used when the Bank integration option is active. The first time you add the desktop component, you will need to restart Monitor ERP for the information to be visible. Under Settings you can select which banks the information should be shown for.
> It may also be necessary to restart Monitor ERP for the bank to load and to be able to configure the desktop component’s settings.
The component shows the balance of the bank accounts, the balance in the general ledger, and the balance of not confirmed payments. The bank account balance is loaded from the bank every night, but you can also load your current balance via the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png).
> Please note that certain banks have limits on how many times balances can be loaded per day.
In the To confirm column, you can see the balance of payments which have not yet been confirmed. By double-clicking on the bank account, you can be redirected to the Manage bank transactions procedure to confirm the payments.
In the desktop component you can also monitor ordered payments. The Payment status button shows information about the payments which have been sent to the bank.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) OK – no problems reported with the payments that have been ordered for payment (waiting to be paid).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) Warning – there are ordered payments which are partially signed and are waiting to be countersigned via online banking.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) Error – there are ordered payments that have failed to be sent to the bank.
By clicking the button, you will be redirected to Status of ordered payments in the Accounts payable list where you are able to see more information.
Crediflow invoice status
Sweden and Norway. This component provides the user with an overall view of the e-invoices sent via Crediflow. The component can be configured to show invoices with different statuses. You can also configure for how many days back in time you want to show invoices.
Explanation of statuses with Crediflow:
- In queue – Means that the document is sent to Crediflow's API. It has been placed in a queue to be processed by Crediflow.
- Imported – Means that Crediflow has matched the correct issuer and mapped the document and loaded it in the system (Crediflow).
- Exported – Means the document is exported from Crediflow to the receiver.
- Printed – Means exported from Crediflow to the print partner.
- Sent to post – Means sent from the print partner to the post distributor.
- Rejected – Means that either Crediflow has rejected the invoice due to a validation error, or the receiver's operator/system for some reason has rejected the invoice.
- Acknowledged – Means that the invoice has been acknowledged by the receiver.
Delivery schedule deviations
This component shows deviations occurring in the delivery schedules. The details of the deviations are not displayed in this list (it is intended as an early warning and overview). However, by double-clicking a record, it will open in the Analyze delivery schedules procedure, in the list type called Deviations – Detailed. In the setting you can choose if you want to show warnings and/or alerts, and also if you want to show Part issues and/or Call issues.
Depending on the type of issue, you can double-click to go to:
- When there is a deviation in requirements, the Analyze delivery schedules procedure will open with the list type called Deviations – Detailed.
- When there is an issue with part transfer, the Analyze delivery schedules procedure will open with the list type called Delivery scheduleSilf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. parts, using the Transfer warnings and errors presentation.
- When there is an issue with call-off transfer, the Analyze delivery schedules procedure opens with the list type called Requirements – Detailed, using the Standard presentation.
Lagging purchase orders
This component displays a list of late purchase orders. The component shows the delivery date, part number, the part’s name, order number, status of the purchase order, position number, ordered quantity, supplier number, supplier name, and a column that shows whether the purchase order is a stock order. The list is filtered by delivery dates that are earlier than today’s date.
Shortcut keys
This component has a table where you can see the shortcut keys you can use in Monitor. At the top of the component there is a filter where you can filter by Type of shortcut.
Supplier rating – Chart
This component displays the supplier rating. Data in this component is grouped by actual delivery date which is compared to:
- Planned date
- Initial date
- Desired date

#### Component settings
In all components you can change the heading shown on the title bar of the component. The heading is also determined by the language of the user. In many of the components it is possible for you to enter an updating interval. This is by default set to 24,00 hours. You can also update data manually in components by using the Refresh button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) in the component. Other settings in the components correspond to the settings available in the procedure to which you can go to by double-clicking in the component in question. You access all settings using the Settings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_settings.png) in the component.
> If you are using a finished desktop configuration According to template you will not be able to access the settings. For these finished desktop configurations, setting for the components are instead configured in the Desktop templates procedure.
