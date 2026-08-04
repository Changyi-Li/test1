### Settings
In this box you configure settings for each delivery schedule type. The settings concern the different steps in the handling process: Activation, Reconciliation, Transfer, and are shown grouped by these steps in the box.

#### Processing mode
With this setting you decide if the steps in the handling process of delivery schedules of this type should be processed manually in full or partially, or automatically. Steps which should be done manually, you take care of in the Handle delivery schedules procedure. The available options are:
- Manual – (default) All steps are manually handled.
- Automatic activation – The activation will run automatically. Reconciliation and transfer are manually handled.
- Automatic reconciliation – The activation and the reconciliation will run automatically. Transfer is manually handled.
- Automatic transfer – All steps are automatically handled.

#### Transfer to
Here you decide if the delivery schedule should be transferred to Customer order or Sales forecast.
Activation

#### Matching of dock and storage
Receiver and part always have to be matched on the delivery schedules. But with this setting you can increase the matching to also include dock and storage. The available options are:
- Dock and storage must match – With this option both the dock and the storage must be the same for a match to take place.
- Dock must match – (default) With this option the dock on the part must be the same for a match to take place.
- Do not take dock and storage into consideration – With this option, neither dock nor storage must be the same.

#### Matching of customer's order number
With this setting you decide if the customer's order number should be matched at part level in the delivery schedules. The setting is relevant when the same part occurs multiple times in one or several delivery schedules.
- Do not match on customer’s order number – (default) With this option no match will be made of the customer's order number on the part rows. Earlier calls will be replaced when the part occurs multiple times in the delivery schedule or earlier delivery schedules, regardless if the customer’s order number is matched.
- Customer's order number must match – With this option a match is made of the customer's order number on the part rows. If different "customer's order number" are used on the rows with the part, the previous calls in the delivery schedule or earlier delivery schedules will not be replaced. Only if different "customer's order number" are used on the rows with the part, the previous calls in the delivery schedule or earlier delivery schedules will not be replaced.

#### Activation principle for the part
With this setting you determine how replacing of the part level should be handled in relation to an earlier delivery schedule. The available options are:
- Replace all calls – (default) With this option, all calls on order rows for the part in an earlier delivery schedule, will be replaced.
- Replace calls to and including end date – With this option, all calls on order rows up to and including the end date of the new delivery schedule, will be replaced. When you select this option, it also means that the next setting Show order rows beyond end date becomes available.

#### Show order rows beyond end date
If the above mentioned setting has been set to Replace calls to and including end date, you can here choose if existing order rows in Monitor ERP (with delivery date after the end date of the delivery schedule) should be displayed or not in the Handle delivery schedules procedure. By default, these order rows are shown together with the calls on order rows that should be replaced.

#### Warn if schedule (or section) is not replaced within set time
With this setting you decide if a warning should be shown when an entire delivery schedule or a section of a delivery schedule has not been replaced before the "best-before date" of the delivery schedule. It is the number of days you enter in the Number of days field. The default option here is 30 days.

#### Deviation model
Here you select a deviation model that will be linked to this delivery schedule type. By using this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can see how the selected model is defined.

#### Check deviations automatically
The default value here is No. If you configure this to Yes, the deviation check will run when the delivery schedule is activated. In this first version (25.5) there is no way to manually run a deviation check. In order to use the function, you need to select Yes.
Reconciliation

#### Reconciliation method
Here you decide which reconciliation method should be used for calls in delivery schedule. The available options are:
- No reconciliation – (default) With this option, no reconciliation will be made. That is, calls sent earlier to the customer will not be taken into consideration.
- Frozen period – With this option, reconciliation is made for calls with delivery dates outside the frozen period. That is, we do not reconcile the calls within the frozen period. The number of days is applied in relation to today's date. In the field Number of days below you enter how long the frozen period should be, in number of days. Number of days can either refer to work days (default) or calendar days. This is determined with the setting Consider work days in calendar which you find below.
- Delivery note reconciliation – With this option, reconciliation is made for calls on delivery notes which the customer has received earlier and which is returned to us for reconciliation with the new delivery schedule.
- Cumulative reconciliation – With this option, cumulative reconciliation of calls will be made. That is, we add to the calls already sent to the customer, and assume that the customer provides the accumulated quantity already received in their delivery schedule, as of the cumulative start date you have agreed upon together.

#### Received quantity must be greater than 0
If the reconciliation method is set to Delivery note reconciliation it is possible to choose if delivery notes for which the received quantity is zero, should not be included in the reconciliation.
-   
No – All delivery notes from the delivery schedule will be included in the reconciliation.
-   
Yes – Only delivery notes with a received quantity greater than zero will be included in reconciliation of delivery notes.

#### Consider work days in calendar
With this setting you decide if work days in the calendar should be taken into consideration. This setting applies when Reconciliation method above has been set to Frozen period. By default, the frozen period is given in work days. If you change the setting to No, the frozen period is given in calendar days, that is, including weekends and holidays.

#### Date principle for lagging order, if any
With this setting you decide which delivery date is entered on order rows created from calls that are considered lagging order, that is, order rows that we are unable to delivery on time. The available options are:
- Today's date – (default) Calls with delivery dates earlier or same as today's date, will become lagging orders.
- Fixed date – Calls with delivery dates earlier or same as the selected date in the Date field (below), will become lagging orders.
- Relative date – Calls with delivery date corresponding to the entered (negative or positive) number of days in the field Number of days (below) in relation to today's date will become lagging orders.

#### Date principle for urgent requirements
With this setting you decide which delivery date is entered on order rows created from calls which the customer has stated are urgent requirements, that is, order rows which must promptly be delivered. The available options are:
- Today's date – (default) Calls with delivery dates earlier or same as today's date, will become urgent requirements.
- Fixed date – Calls with delivery dates earlier or same as the selected date in the Date field (below) will become urgent requirement.
- Relative date – Calls with delivery date corresponding to the entered (negative or positive) number of days in the field Number of days (below) in relation to today's date, will become urgent requirements.

#### Replace previous call offs, if dates overlap
Determines if more recent calls will replace earlier calls if dates overlap. If dates overlap more recent calls, new order rows will be added with the further requirements that have the same date. This means that there is no risk of losing the demand that has been created by earlier calls and delivering a quantity lower than the customer expects.
- Yes – This option is selected by default. With this option, the overlapping requirements will always be replaced by the most recent call.
- No – Requirements from earlier calls will not be replaced. Overlapping requirements from the most recent call will be added as separate rows on the order.
Transfer

#### Use horizon limit
With this setting you decide if the length of the date horizon should be limited when transferring calls in the delivery schedule to customer order. In the field Number of days you should then enter the number of days ahead in time, for which you want to transfer calls to customer order. The default option here is 180 days. Calls which have a delivery date beyond the date horizon will not be marked for transfer. The purpose of this is if you for example receive a plan with a very distant forecast horizon, you might want to limit for how far ahead in time you want forecast order rows to be created.

#### Time interval in which calls are considered fixed (from today)
It is possible to decide within which time interval calls should be considered fixed, counted from today's date, when transferring from delivery schedule to customer order. Here you configure if this should apply For calls according to agreement or For all calls, that is, also for forecast calls.
In the field Number of days below you enter how long the time interval should be, in number of days. The default option here is 7 days. Number of days can either refer to work days (default) or calendar days. This is determined with the setting Consider work days in calendar which you find below.

#### Consider work days in calendar
With this setting you decide if work days in the calendar should be taken into consideration. The setting applies for Time interval in which calls are considered fixed (from today) above. By default, the time interval is in work days. If you change the setting to No, the interval is given in calendar days, that is, including weekends and holidays.

#### Warehouse on customer order/sales forecast
Here you select the warehouse that should be used when transferring to customer order or sales forecast.

#### Order type
Here you select the order type which should be used on the customer orders that will be created when transferring delivery schedule.

#### Use of commitment level
This setting determines if the Commitment level in calls should be transferred to Type of requirement on the order row. The default option here is to not transfer the commitment level to order row.

#### Handling of customer's order number
With this setting you determine how the customer's order number should be handled when transferring from the delivery schedule's part level to customer order if it differs The available options are:
- Customer's order no. is transferred to rows – With this option the customer’s order number will be updated on order rows.
- Customer's order no. is transferred to header rows – (default). With this option the customer’s order number will be updated both on order rows and in the order header.

#### Type of requirements to transfer
Here you decide which type of requirements should be transferred from the delivery schedule to the sales forecast. Choose between Forecast (default), Fixed order, or both of these requirement types.

#### Replacement method
With this setting you decide if all parts or only matched parts from the delivery schedule should be replaced in an existing sales forecast. The available options are:
Replace all – All parts in the existing sales forecast will be replaced.
Replace matching parts – Only matched parts in the existing sales forecast will be replaced. This setting is checked by default.

#### Prefix for forecast code
In this field you can enter a prefix to be used for the code the sales forecast is assigned when it is created.

#### Shift to new order when order position limit is reached
With this setting you can have the transfer of delivery schedules to customer order change/shift to a new customer order when the order row's position number exceeds the number specified in the delivery schedule type.
Important to keep in mind: This setting should only be used in cases where you do not use so-called linked requirements, since the links will not be included in the new order.

#### Order position number limit
If you configure the Shift to new order when order position limit is reached setting to Yes, you should enter a value in this field. The standard limit here is set to 10,000 (which means 1,000 rows if each position is set to an interval of 10).
With the setting above set to Yes, the following applies if the transfer of a delivery schedule to customer order leads to the order position limit of the "old" order is exceeded:
- A new order is created.
- All open rows from the "old" order are transferred to the new order.
- Order rows with the status Picking in progress will not be transferred/shifted to the new order but will instead remain open in the "old" order.
- On the "old" order, all open rows (except for those with status Picking in progress) will become closed, that is, the remaining quantity is set to 0 (zero) and the row status is set to Final delivery made.
Instances where no new order is created even though the position number limit is exceeded:
- If Usage of the transferred delivery schedule is set to Call-off (JIT/JIS), no new order will be created even though the position number limit has been exceeded.
- If the resulting number of rows to be created on the target order* is greater than the entered position number limit**, no new order will be created. The old order will in that case continue to be used and be updated.
* This is the total number of rows that should be moved from the old order to the new order plus new rows to create from the delivery schedule for the new order.
** That is, the total number of rows on the new order will result in the position number limit is exceeded.
