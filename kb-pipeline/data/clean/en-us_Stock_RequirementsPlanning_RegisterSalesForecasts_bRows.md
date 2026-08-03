### Rows
In this box you enter the forecast rows. The future expected sales is entered by part number with configuration (if any), quantity, and expected delivery date.
With the Apply default configuration on rows possible to configure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) on the toolbar, you are able to select the default configuration for all generated sales forecast rows for the selected forecast. The default configuration is selected and changed in the Part register under the General tab.

#### Part
Here you enter/see the part number to forecast. Only rows with part numbers can be saved.
If the part which will be forecast is a fictitious part, the net requirement calculation will explode it to forecasts for the incorporated parts and save it in the database. Thereby you will see the requirements for the incorporated/included parts which can then result in manufacturing order suggestions or purchase order suggestions. After the net requirement calculation you can see the underlying forecasts for the incorporated/included parts by clicking the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) button to the left in the box and expand the row.

#### Configuration
If the selected part is linked to a configuration group, the Configuration column will be shown. It contains a button for configuration of the part on the forecast row. If the button has this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) then the forecast row is possible to configure. By clicking this button you access a configuration window where you can configure the forecast row. When you save the configuration using OK in that window, the symbol on the button will change ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png), to illustrate that the forecast row is configured.

#### Original forecast
Here you see the forecast quantity. It is always saved in the standard unit. The default quantity on the first row is 1. After that, the quantity from the row above will be suggested when you create a new row.

#### Unit
Here you see the part's unit.

#### Delivery date
Here you see the forecast delivery date. The default date on the first row differs depending on how the part’s forecast deduction is configured in the Part register procedure. The date suggested on subsequent rows is the date on the row above plus the time interval (in work days) on that forecast. The date calculation will start again when you enter a new part number.
A calendar function is linked to the field. Dates in past time are shown in red, and dates within the part’s lead* are displayed in blue.
* For purchased parts, the referred lead time is primarily the one entered in the part register for the active supplier link, and secondarily the lead time which is entered in the planning information. For manufactured parts, the referred lead time is the throughput time entered in the part register in the planning information.

#### Net forecast quantity
Net forecast quantity = Original forecast – Ordered quantity. Only actual customer order rows are deducted from the forecast. If the order or the order row is deleted, this quantity will no longer be deducted from the forecast (but they remain in the database for the order inflow). If you have manually deleted a remaining quantity, the ordered quantity will still be deducted.
This field is used when the parts' deduction method has been set to Periodic intervals. Please note! This field is shown even though you might not be using Periodic intervals as deduction method for the parts.

#### Ordered quantity
Here you see the ordered quantity of the part. This field is used when the parts' deduction method has been set to Periodic intervals.

#### Error message from import
Error messages generated during the import, if any, will be displayed in this column.
