## Report manufacturing order
In this procedure you can report operations and linked material for manufacturing orders. You can also add operations and material to an order.
After saving the reporting, it is possible to print a transport label for the manufacturing in progress, or a transport label for transfer to stock, if you have reported the final/last operation.
You can report in an operation list based on the order number or you can perform a detailed operation reporting based on the report number. You can also switch between operation list and the detailed operation reporting by selecting a main part or an operation in the structure map.
Subcontracts are not reported here. Instead you go to the Report arrival procedure via a link, from a selected subcontract in the structure map.
Traceable material
A check is made to find out if there is remaining quantity on included traceable material. When performing partial reporting, a warning is shown if remaining quantity exists for traceable material. When reporting operations as finished, a block is created if remaining quantity exists for traceable material. Traceable material is never automatically deducted when the operation is reported.
If you have a serial number for the part that is being manufactured, and traceability for the included material, then a dialog is opened when you save the quantity that you are reporting. There you can enter the manufactured serial number and link it to a serial number/batch number that exists for the traceable material. It is possible to report traceable material which is linked to subcontract.
In the dialog it is also possible to rename the serial number, that is, to enter a new.
System settings
There are some system settings that affect the reporting of manufacturing orders. The settings that will be selected by default in this procedure are determined by:
- Suggest remaining quantity when reporting
- Suggest planned time for reported quantity
- Automatic withdrawal of material
- Automatic reporting of tools – Only available in systems with the Tools & Maintenance option. Please note! If you report on operations which have active recording items, no automatic return of tools will be made. Regardless if the remaining quantity on the operation is 0.
These system settings determine if checks in the procedure should do nothing, warn, or block:
- Check if reported quantity is greater than previous operation's reported quantity
- Check against remaining quantity of material when reporting final operation as finished
- Check if balance is negative during reporting.
This system setting determine the increase of the remaining quantity for a following operation:
- Increase remaining qty for following operations when excess reporting – If the remaining quantity is instead decreased for an operation, the remaining quantity always decreases for the following operations.
This system setting determines how the remaining quantity should be handled at rejection for operation:
- Deduct remaining qty on operation and material at rejection.
