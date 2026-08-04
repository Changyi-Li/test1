### Machine
The Machine tab is available if the option Machine integration is installed. This tab is intended for machines in the production that are included in the machine integration. Machines that are registered here will become selectable in MI Admin, the administration tool used in Machine integration.

#### Using Machine integration
With this setting you determine whether or not the employee number should be linked to the machine integration. The following options are available:
- No
- Machine – this option will take up one machine license.
- Machine – Member in line – this option will take up one machine license. The same fields will be inactivated as for the option Line – Member described below.
- Line – this option will take up one line license.
- Line – Member – this option will not take up a line license, but it gives you the same alternatives as for the option Machine.
> Please note! Employee numbers that are linked to machine integration cannot use the Recording terminal procedure.

#### Linked to work center
Here you choose to which work center the Machine or Line should be linked.

#### Report arrival
With this checkbox you decide if the operator's arrival to the terminal to acknowledge stops, should be reported for this machine. The purpose is to measure the time from stop to action, that is, the time it takes for the operator to get to the machine to resolve the stop.

#### Time interval for loading to order
Here you enter a default interval for loading to order for Machine or Line. This interval determines how often the order in the company database in Monitor ERP (for example 001) should be synchronized with the machine's reporting on the order in the company's machine database (for example MM_001). The default interval is 30 minutes. If you enter 0 minutes, no automatic synchronization will be made.

#### Report quantity when full pallet is manufactured
With this checkbox you decide if an automatic reporting should be made when Machine or Line has manufactured a full pallet. You should activate this setting when the above setting has been set to 0 minutes as time interval. This means automatic synchronization will not take place.

#### Machine unique time for short stops
Here you enter the excepted stop in number of minutes. Two decimals will be displayed but it is possible to enter up to six decimals. If you enter a value here, this value will override the value entered in the system setting Time limit for short stops (minutes).

#### Machine-unique indirect code for short stops
Here you select the indirect code that you want to use during short stops for this machine. If you select an indirect code here, this will override the indirect code entered in the system setting Indirect code for short stops.

#### Machine-unique indirect code when operating without order
Here you enter a machine unique indirect code when running/operating without an order. This setting is used during Line.

#### Machine-unique limit for yellow area on availability gauge
Here you enter a machine-unique start value (in percent) for the yellow area on the availability gauge if OEE gauge is used.

#### Machine-unique limit for green area on availability gauge
Here you enter a machine-unique start value (in percent) for the green area on the availability gauge if OEE gauge is used.

#### Machine-unique limit for yellow area on performance gauge
Here you enter a machine-unique start value (in percent) for the yellow area on the gauge used to show performance if OEE gauge is used.

#### Machine-unique limit for green area on performance gauge
Here you enter a machine-unique start value (in percent) for the green area on the gauge used to show performance if OEE gauge is used.

#### Machine-unique limit for yellow area on quality gauge
Here you enter a machine-unique start value (in percent) for the yellow area on the quality gauge if OEE gauge is used.

#### Machine-unique limit for green area on quality gauge
Here you enter a machine-unique start value (in percent) for the green area on the quality gauge if OEE gauge is used.

#### Automatically start setup time when new order is loaded
With this setting you decide if the setup time should automatically start when you load a new work item in the machine.

#### Check setup when a new order is loaded
With this setting you decide if a check should be made to see if the loaded order has previously reported setup time. If the order doesn't have setup time reported, the warning text "Setup has not been performed on order" will be shown.

#### Report pieces at "End setup"
With this setting you decide if the machine operator should have the ability to manually report finished pieces (parts) when ending setup. This applies to Machine and Line. This setting also activates the four settings below.

#### Mandatory to report all manufactured parts
With this setting you decide if the machine operator should be forced to report all finished pieces when ending setup.

#### Suggest remaining quantity as rejection
With this setting you decide if remaining quantity should be suggested as the rejected quantity.

#### Lock possibility to manually change rejection
With this setting you decide that it will not be possible to manually change the rejected quantity.

#### Default rejection code
Here you can enter a default rejection code. This rejection code will become the default if you report pieces when ending setup. The rejection codes available to select here are the ones marked with Only rejection in the Rejection codes/Cause codes procedure. When you end setup and there is a default rejection code, but the setting Suggest remaining quantity as rejection is not activated, then this code will automatically be filled in when a rejected quantity is entered. If there is no default rejection code, you can instead select one of these rejection codes.
