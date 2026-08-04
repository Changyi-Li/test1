### Delivery schedules
In G5 there is EDIEDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. support for import and handling of delivery schedules as well as export of simplified dispatch advice or complex dispatch advice (with package structure). In a simplified way, this means that there is support for the following EDI transactions:
- Import of delivery schedules to the Sales module. This includes import of delivery schedules for a so-called batch flow (where parts in a new delivery schedule completely replaces the corresponding parts in the preceding delivery schedule), Kanban flow, and Call-off flow. Please note! Synchro delivery is not handled.
- Export of simplified dispatch advice from the Sales module. When referring to "simplified dispatch advice" we mean that the dispatch advice does not contain any information about packages and packaging structures. With different settings, the export of a simplified dispatch advice can either take place via the Delivery planning procedure or via the Report delivery procedure.
- Export of complex dispatch advice from the Sales module. The complex dispatch advice contain information about packages and packaging structures. The export of a complex dispatch advice can either take place via the Pack for delivery procedure or via the Report delivery procedure.
Import files for delivery schedules support a so-called flat file format. The format of export files for dispatch advice is XML.
It is also possible to manually register delivery schedules in a separate procedure. This method can be applied if the customer for example sends you delivery schedules as Excel files or on paper.
In G5, each imported or manually registered delivery schedule is assigned an individual consecutive number before it is saved in a delivery schedule register. This means that importing a delivery schedule via EDI or manually registering the delivery schedule, are two different methods to achieve the same thing. You then check the delivery schedule – no matter if it is created via EDI or manually – and then you transfer it to customer order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule1.png)](../../../../../Resources/Images/News/DeliverySchedule1.png)
Unlike in G4, the EDI portion is separated from the actual business process handling for delivery schedules in G5. In short, this means:
- Just like for all EDI import in G5, you handle the corrections/adjustments of customers and parts which don't match in the procedure Manage EDI transactions in the General registers module. When the EDI portion finds a match for customer and parts, there is a delivery schedule registered in G5.
- You handle (check/match and transfer to customer order) all registered delivery schedules by using the procedure Handle delivery schedules in the Sales module.
In the Sales module in G5 there are four new procedures having to do with delivery schedules. These procedures are used both when you import delivery schedules via EDI and when you register them manually.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule2.png)

#### Delivery schedule types
Here you register delivery schedule types which for example contain settings for how the delivery schedule should be checked/matched and which order type should be used for the transfer to customer order. Furthermore, there is a setting determining whether or not the delivery schedule should automatically be transferred to customer order when using EDI import. The corresponding settings in G4 are configured per customer (button Extra Info).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule3.png)](../../../../../Resources/Images/News/DeliverySchedule3.png)

#### Register delivery schedule
Here you can manually register delivery schedules and you can modify and delete delivery schedules. The corresponding functionality in G4 was found in the Import EDI Delivery Schedules procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule4.png)](../../../../../Resources/Images/News/DeliverySchedule4.png)

#### Handle delivery schedules
Here you handle the delivery schedules in the business process, that is, you activate, check/match, and transfer to customer order. You can choose to either handle the entire delivery schedule or a certain part in the delivery schedule.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule.png)](../../../../../Resources/Images/News/DeliverySchedule.png)

#### Analyze delivery schedules
Here you can get an overview of the delivery schedules which have been transferred to customer order and how the relation was between the delivery schedule's calls and the order rows, at the moment when the delivery schedule was transferred. You also a find a simplified chart function which you can activate. The corresponding functionality in G4 was found in the Delivery Schedule Log / Diff procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/DeliverySchedule5.png)](../../../../../Resources/Images/News/DeliverySchedule5.png)
