### Status
In this box you select the status for the serial number/batch number. Depending the status, the function Block/Notify will also be activated.

#### Status
In this field you can choose a status for the serial number/batch number. For serial numbers there are eight different statuses which can be used as shown in the table. For batch numbers, only the status items marked with an asterisk (*) in the table are available.
| Symbol | Name | Block/Notify |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) | Approved for use * | – |
|   | Does not need approval for use | – |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) | Service overdue | Message |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeService.png) | Service/Calibration in progress * | Message |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) | Not approved * | Block |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) | Service/calibrate before use | Block |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/question_mark.png) | Missing | Block |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDeleted.png) | Scrapped | Block |

#### Block/Notify
You can configure a block or a notification on a serial number/batch number for the following events:
- Withdrawal to manufacturing
- Clearance to manufacturing
- Withdrawal to customer order
- Clearance to customer order
- Exclude from disposable balance.
The status of a serial number/batch number determines if it possible to configure a notification or a block. In the table above you see which status items you can setup a block for and for which you can configure a notification.
> If a serial number is rejected in manufacturing, the serial number cannot be used in any kind of order, and it is excluded from the stock balance. When a serial number has been rejected in the manufacturing, the status is set to Scrapped.

#### Notified by
Here you see who configured the block/notification.
