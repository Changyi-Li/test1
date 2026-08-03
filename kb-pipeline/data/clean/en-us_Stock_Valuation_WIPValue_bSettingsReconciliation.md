### Settings – Reconciliation

#### Account
Here you select which account to reconcile.

#### Reconciliation period
Here you enter the start date and end date of the reconciliation period.

#### Only show orders with a difference
With this setting you determine if only orders with difference should be shown in the list. The difference refers to the difference between changes in the WIP value and changes in the booked WIP value.

#### Include not approved journals
With this setting you determine if journals which are not yet approved should be shown in the list. This is used when you want to reconcile the WIP value before the journals are transferred to the accounting.

#### Show configured parts
With this setting you determine if configured parts should be shown in the list. The Product configurator is an option you can add to the system. Please note! The system does not support reconciliation of configured manufacturing orders.

#### Storage overhead mark-up
Here you see storage overhead mark-ups. You can also adjust these mark-ups.

#### Value of processing
With this setting you determine if reported time or planned time should be used for the valuation of work. By selecting one of the alternatives Reported time or Planned time for reported quantity, you can choose to value work either according to the operation’s actual reported time or according to the operation’s planned time for the quantity that has been reported. If you select Planned time for reported quantity, the setup time will be distributed based on reported quantity.

#### Operation cost
There are two alternatives for type of cost for operations:
- Reported (default) – The cost for the reported time is valued at the cost factors that applied at the time of the reporting. By using this alternative, you will get the same operation cost regardless of when the calculation is made (as long as the reported time has not been changed).
- Current – The cost for the reported time is valued at the current cost factors of the work centers.

#### Cost factors
Here you select the costs for operations that should be included in the calculation. The costs that are selected in the system setting Default cost factors will here be shown as default.

#### Value of subcontract
With this setting you determine if reported cost or planned cost should be used for the valuation of subcontract. By selecting one of the alternatives Reported cost or Planned cost for reported quantity, you can choose to value subcontract work either according to the operation’s actual reported cost or according to the operation’s planned cost for the quantity that has been reported. The actual cost is loaded from the supplier invoice that is linked to the purchase order.

#### Planned cost before invoice has been linked
If you have selected the option Reported cost for the setting above, you can here determine that reported subcontracts will be valued using the planned cost according to the purchase order for the reported quantity, until the supplier invoice for the subcontract has been linked. When the invoice has been linked, the subcontracts will be valued to the reported cost according to the invoice. If this setting is not activated, the cost of subcontracts that have no invoice linked to them will be reported as zero.
