### Traceability
> All settings in this box can be made for several parts at a time in the [Traceability settings](../PartList/tTraceabilitySettings.htm) list in the Part list procedure.

#### Traceability
With this setting you decide if the part should be traceable. By clicking the button next to the field ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you select the level of traceability; by batch or serial number. You cannot use traceability for parts of the Fictitious and Service type. Explanation of the different traceability alternatives as follows.
- None – No traceability in the manufacturing of the part.
- BatchA batch is the set of components/products manufactured at the same time and made from the same original material. – A batch can contain one or several units of the same part. Batch must be entered for all stock transactions.
- Serial numberA serial number is a number that is used for traceability for parts on entity level. – TraceabilityTraceability in Monitor ERP is all about being able to trace a specific serial number or a batch in each step it is being processed, as of when a part or a material arrives with you from a supplier. Traceability is also about stating what is withdrawn from and what is added to stock, so it is then possible to trace from customer order, via manufacturing order to purchase order. But it is also about being able to trace the other way around; from purchase order via manufacturing order to customer order. on entity level in the manufacturing. Serial number must be entered for all stock transactions. Read under Traceability only for delivery below if you want to assign serial numbers for a part you sell, but which you do not have to apply traceability for in the manufacturing.
- Serial number (only withdrawal) – This alternative is available for the Purchased part type. In this case, no serial number is assigned to the part during arrival. The serial number is instead entered when you link the part as material when an operation is reported on a manufactured part with traceability on serial number.
> It is not possible to change traceability from Batch to None if there are reservations for the part.
Display in location windows
When a part has traceability activated and a batch number or serial number has been registered on a location, there are sub-rows on the location that you can expand by using the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the left in the location table. On the sub-rows you see which serial number/batch number and charge number have been registered on the location.
Change traceability for existing part
If you activate Batch or Serial number traceability for the part and there is a balance on the location, a warning will be shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that batch or serial number is missing. You then have to adjust this by adding batch numbers or serial numbers for the balance in the Stock count procedure.
If you activate traceability and the part has a negative balance in a location, a block is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) since a negative balance for traceable part is not allowed.
If Serial number traceability is activated for a part with a planned or started manufacturing order, you must either assign serial numbers from Number series or manually add serial numbers with the Serial number button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) for the quantity on the manufacturing order where the part is included.
If you change traceability for a part that has a material clearance, a warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that the clearance on the part will be deleted.
It is possible to change traceability for a part that has a material clearance as long as the reporting of the material has not taken place for the specific material row. For partially reported material rows on a manufacturing order that does not have status 9 (Historical), a warning or a block is shown according to the table below.
| Change from | Change to | Result |
|---|---|---|
| None | Batch | Warning or OK |
| None | Serial number | Block |
| Batch | Serial number | Block |
| Serial number | Batch | Block |
| Serial number | None | OK |
| Batch | None | OK |
You cannot change traceability for a part from Batch to Serial number if the part has batches with a balance greater than 1.
Traceability only for delivery
If you should assign serial numbers to parts you sell but you do not require to apply traceability in the manufacturing, then you should not activate Serial number traceability here. You should in that case leave the traceability as None and instead select the Create serial no. at customer order setting below on the part. Via the options in that setting, the serial number is added on customer order rows, either during registration of customer order or during delivery reporting of customer order. This way you can assign serial number without activating traceability in the manufacturing.

#### Apply best-before date
If you have configured the traceability to Batch or Serial number, this setting becomes available. When you activate this setting, you must also enter a best-before date when you arrival report the part. This field is empty by default. The date is saved for the batch/serial number and is shown in the Serial number/Batch procedure. In that procedure you can also edit the best-before date.

#### Suggest best-before date
Configure this setting if you want the system to suggest best-before date when transfer to stock takes place for a manufacturing order.
If the part is a purchased part, you will receive a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) if you select any of the options to suggest a best-before date. This is because the best-before date for purchased parts are entered at arrival reporting. Also, manufacturing orders are normally not created for purchased parts.
The following options are available:
- No – no date will be suggested. Then you must manually enter the best-before date.
- Yes, add days – a fixed number of days will be added when best-before date is set. The fixed number of days are entered in the setting below called Add days.
- Yes, shortest date on reported material – checks the shortest best-before date of material withdrawn for the order, and suggest it as best-before date.

#### Add days
Here you enter the number of days that should be added to the best-before date when you have selected one of the Yes alternatives in the setting Suggest best-before date.

#### Allow automatic withdrawal
Here you can allow automatic stock withdrawals during different reporting items. This is made at part level. This can be configured for the alternatives Pick location, Cleared, Location, and Project. Automatic withdrawals are allowed by default for a part without traceability, but not when the part has traceability. To obtain an easy reporting process for traceable material without compromising the accuracy/security, you can choose to only activate one option for automatic withdrawal. Below you will find more information about the different alternatives.
- Pick location – Allows automatic withdrawal from locations configured as pick location and pick location for work center.
- Cleared – Allows automatic withdrawal of balance that are cleared for the requirement. This is useful when using linked requirement since the balance will then be automatically cleared.
- Location – Allows automatic withdrawal from other locations (not pick locations). This is mainly used if you always want to allow automatic withdrawal. In that case, it is combined with the alternative Pick location.
- Project – This alternative only applies to parts with traceability. It allows automatic withdrawals from batches and serial numbers which have the same project number as the order to which the withdrawal is made. In order for this to work, the project number is saved on batch/serial number during arrival to stock.
This setting can be configured for several parts at a time in the Allow automatic withdrawal list in the Part list procedure.
> Please note! The system setting called Automatic withdrawal of material will override this setting. When this system setting has been set to Yes, you can make exceptions per work center by using the setting Exclude from automatic reporting of material for the work center.

#### Create serial number at customer order
If you should always assign serial numbers to a part that you sell, you should here configure that serial number should be created at customer order. You should then select one of the options At registration of order or When reporting delivery. It will then be mandatory to enter a serial number on the customer order row, either during registration of the order or at the delivery reporting.
If it should not be mandatory to enter a serial number on the customer order row, you should keep the setting set to No. It is then optional to enter a serial number.
It the part has traceability set to Serial number and you also should create/assign serial number at customer order, the part's control method must be set to Order oriented (with lot sizing rule Lot-for-lot or Linked requirement) which is configured under the Planning tab.
A number of checks are made if serial number is entered at customer order. A check is made to see if the serial number already exists. If so, a warning appears. When a manufacturing order is created from a customer order row, a check is made to make sure that the serial number does not already exist on a location or on another manufacturing order.
If a manufacturing order already has been created and changes are made regarding the serial number on the customer order row, then the serial numbers for which reporting has been made will be blocked. This means that it is not possible to make any changes on these serial numbers. If no reporting has been made for the serial numbers, the changes of serial numbers will be transferred from customer order to manufacturing order.
Please note! If the part is Stock driven and has traceability set to Serial number and you here select At registration of customer order or When reporting delivery, then an error message is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png). For such a part you cannot create serial number at customer order. If the part has serial number traceability, a serial number will be created for each entity of a part during arrival reporting to location, either from purchase or from manufacturing. These serial numbers will be used on the customer order row and at the deliveries reporting. In that case, the serial numbers will be used to trace entities of the part back to the manufacturing and purchase. This means that traceability throughout the entire chain is required, meaning that all parts where the part is included must also have traceability at serial number level.

#### Assign number
If you have configured to create serial number at registration of order, you here determine if the serial number should be set Manually or From number series.
The option Manually means the number of serial numbers must match the quantity. For example, if there are 10 parts on a customer order row, you must enter 10 serial numbers. Please note! If serial number is created when reporting delivery, there is an exception. You then enter a start value for the serial number and the quantity to deliver, and the end number is calculated automatically.
The option From number series means that the serial numbers are loaded from a number series for serial numbers. Then 10 serial numbers will be loaded automatically from the number series to the customer order row. Which number series you want to use and how it should be created is configured in the Number series procedure.
If you have not configured to create serial number at registration of customer order (the setting above Create serial no. at customer order set to No), you can still enter an optional serial number on the customer order row, but it is not mandatory.

#### Linking of serial number
For manufactured parts with Serial number traceability where the material is also traceable, the material has to be linked to each individual serial number. Here you choose when in the manufacturing reporting this linking should be made.
The following options are available:
- At actual operation – A dialog is shown when reporting the operation where the traceable material is included according to the BOM. In that dialog you can link the traceable material to serial numbers.
- At actual op. or subsequent op. – With this option you can link the material to the serial number when reporting the operation where the traceable material is included according to the BOM, or at a subsequent operation. You link the material by clicking the Change traceability button when you report the operation. However, if you have not performed the linking when you report the final operation, the dialog will appear automatically for you to link the traceable material to serial number.

#### Exposure time
On parts with traceability at Batch level, you can select the exposure time. Codes and exposure times must first be registered under the Exposure time tab in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure. The Exposure time system setting under the Stock tab in the System settings procedure is used to activate the exposure time function.
When a batch is created, the code you have selected for the part is automatically assigned to the new batch.
