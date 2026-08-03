### Settings – Internal operations
Under this heading you configure settings for valuation of own work and costs for work centers in the calculation of the WIP value.

#### Value of processing
With this setting you determine if reported time or planned time should be used for the valuation of work. By selecting one of the alternatives Reported time or Planned time for reported quantity, you can choose to value work either according to the operation’s actual reported time or according to the operation’s planned time for the quantity that has been reported. If you select Planned time for reported quantity, the setup time will be distributed based on reported quantity.

#### Don't value higher than planned time
If you have selected the option Reported time for the setting above, you can here select to not give a higher value than the value of the planned time. The orders that have a reported time longer than the planned time will be displayed with a warning symbol, and you can also see them under the Warnings tab along with information about the cause.

#### Operation cost
There are two alternatives for type of cost for operations:
- Planned/Reported (default) – The cost for the reported time will be valued at the cost factors that applied at the time of the reporting. By using this alternative, you will get the same operation cost regardless of when the calculation is made (as long as the reported time has not been changed).
- Current – The cost for the reported time is valued at the current cost factors of the work centers. When this alternative is selected you can also choose between the price alternatives Current and Future.

#### Cost factors
Here you select the costs for operations that should be included in the calculation. The costs that are selected in the system setting Default cost factors will here be shown as default.

#### Price alternative
With this setting you decide if current or future prices should be loaded from the cost factors.

#### Calculate with planned setup time (for operations with only reported unit time)
With this setting you include the cost for planned setup time for operations that do not have any setup time reported. This can be used if the operator has included the setup time in the unit time for operations that are reported as finished. The purpose of this setting is to avoid cost differences in cases where the setup time has not been reported. The costs of setup time and unit time can differ, partly due to staffing factors linked to the cost factors, and partly if you have created different cost factors for the work center, one for setup time and another for unit time.
If the operator has reported setup time, the calculation is based on the reported setup time, regardless of this setting.
Example: There is 1 hour of planned setup time and 2 hours of planned unit time registered for an operation. The operator does not report any setup time, but 3,5 hours of actual unit time. If this setting is activated when performing the calculation, the system will calculate 1 hour setup time and 2,5 hours of unit time.
