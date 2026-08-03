### Settings
Include

#### Show maintenance to
With this date you decide for how long time ahead you want to show planned maintenance. Today's date is shown by default.

#### Trigger type
With this setting you decide for which trigger types planned maintenance should be calculated. The list will present planned maintenance based on the selected trigger types. The alternatives are:
- Calendar – Number of days since the most recent maintenance item.
- Distance – Number of kilometers since the most recent maintenance item.
- Operation time – Number of hours which the tool/machine has been used since the most recent maintenance item.
- Number of cycles – The number of cycles the tool/machine has been used since the most recent maintenance item.
All different trigger types are displayed by default. If you choose to not include any of the alternatives, you will get a list of all planned maintenance items, regardless of if the trigger limits have been exceeded or not.

#### Include all maintenance plans
If you activate this setting you will also show logs from previously linked maintenance plans for the serial number/tool.

#### Reporting status
With this setting you decide which reporting status (for service numbers) should be included for planned maintenance. Next time of maintenance is also based on the selected reporting status. By default, all reporting statuses are checked (Not started, Started, Finished).

#### Planned maintenance order
This is used to calculate the most recent reporting of maintenance order based on calendar. You can select among the same statuses as for manufacturing orders. By default, all order statuses are included except for Delivered and Historical.

#### Rows not triggered
With this checkbox you decide to also include maintenance items where the trigger type's limit has not been exceeded.

#### Suggest create maintenance order
If you mark this setting, each maintenance requirement in the list is suggested to create a maintenance order.
Show

#### Planned maintenance order
The list only shows maintenance orders with the status selected here. None of the statuses are include by default.

#### Reporting status
The list only shows maintenance orders with the reporting status selected here. All reporting statuses are selected by default.

#### To date
With this setting you can select a date horizon, meaning for how far in the future you wish to see planned maintenance orders in the list. If no date is selected here, all planned maintenance orders will be displayed.

#### Next reservation
With this setting you decide if the tool’s next reservation should be displayed in the list. In this list you will then see the date of the next reservation of the tool and the order number or order suggestion that has reserved the tool. The available options are:
- No
- Actual orders
- Actual orders and suggestions
