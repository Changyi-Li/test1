### Header row

#### Pick list number
Here you select or enter the pick list that should be packed. The pick list is created from the list type Picking plan in the Delivery planning procedure.

#### Clear/Undo clearance
Using the buttons Clear ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png) and Undo clearance ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) you can perform clearance or undo a clearance of all the parts in the pick list.
All parts are not cleared by default on a preliminary pick list, and the pick list status in the Header box will then be "Preliminary".
All parts are cleared by default on a regular pick list, and the pick list status in the Header box will then be "Ready for delivery". If you undo a clearance of a pick list ready for delivery, the pick list status will be reset to "Preliminary".

#### Pkg ready (Package structure ready for delivery)
Here you select Yes when all packages have been completely packed and are ready for delivery. This will then set Complete on all rows in the package structure, if this has not manually been entered on the rows.
> When the setting Package ready for delivery is set to Yes, you can no longer change data in the Package structure box. But it is possible to make changes to a pick list, even when it has been delivered. You should then set this field to No and this makes it possible to make changes in the package structure after you have unchecked the box Complete on the row that should be changed in that box. For example, you can change gross weight, add/delete package rows or part rows, change quantities.

#### EDI
By clicking the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the EDI information in question.
In the EDI connected field it says Yes if the customer on the pick list is connected to EDI, otherwise it will read No. The default value is loaded from the customer. When the customer is connected to EDI, it is possible to use the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button next to the field to see which EDI transaction types and directions that apply for the customer in question.
If the customer is connected to EDI it is possible to send EDI advice. This is done by using the Send via EDI button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_send_edi.png) which is then available on the procedure toolbar. A dispatch advice can by default be sent via EDI when printout of delivery note is approved in the Report delivery or Print delivery documents procedures. When the dispatch advice is sent, it is done according to the EDI behavior to which the customer is linked. This can be monitored in the procedure called Manage EDI transactions.
If the customer is connected to EDI, you can with the setting Exclude from EDI decide if the dispatch advice for the pick list in question should be excluded from the EDI flow. This means the dispatch advice cannot be sent via EDI from the above mentioned procedures. The Send via EDI button will then also be deactivated.
You can also see the EDI Export status for the dispatch advice showing date and time for the export.

#### Packing progress
Here you see the packing progress for the pick list. This is an icon consisting of arrows, representing how far the packing has come based on the status of the phases. A phase can have the following statuses: Not started, Started, and Finished. The packing progress shows one arrow per phase and one colors for each status. That way, it is easy to see what the situation is like for the pick list.
The four phases represents:
Preliminary quantities packed
- Indicated as started if the total preliminary quantity + cleared quantity is greater than 0.
- Indicated as finished if the total preliminary quantity + cleared quantity equals or is greater than the total quantity to pack, for all rows.
Cleared quantities packed
- Indicated as started if the total preliminary quantity is greater than 0.
- Indicated as finished if the total cleared quantity equals or is greater than the total quantity to pack, for all rows.
Packages completed
- Indicated as started if the total packed quantity is greater than 0.
- Indicated as finished if the total packed quantity equals or is greater than the total quantity to pack, for all rows, and all levels in the package structure have been marked as Finished.
Packed and ready for delivery
- Indicated as not started.
- Indicated as finished if the field called Pkge ready is set to Yes.
Each phase can have three modes:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_1.png) – the phase is not started.
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_2.png) – the phase is started.
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_3.png) – the phase is finished/completed.
