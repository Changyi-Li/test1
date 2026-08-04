### Header

#### Customer's delivery schedule no.
Here you see/enter the number which the customer has on their delivery schedule.

#### Customer's delivery schedule type
If the customer has a delivery schedule type on their delivery schedule, you should enter this here.

#### Customer's delivery schedule date
Here you enter the customer's date on their delivery schedule. Today's date is entered by default, but it can be changed.

#### Organization assigned code
This is a code which is normally entered as information on the delivery schedule in the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. flow, in order to relate to a certain usage of the message.

#### Start date
Here you see/enter the start date of the delivery schedule. The start date must be earlier than the end date, if an end date is also selected.
By clicking the button Calculated start date ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you get to see the calculated start date. The calculated start date is based on the earliest call's delivery date among the parts in the delivery schedule, in combination with the date you selected in the Start date field. You also see what the calculated start date has been calculated for.

#### End date
Here you see/enter the end date of the delivery schedule.
By clicking the button Calculated end date ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you get to see the calculated start end date. The calculated end date is based on the last call's delivery date among the parts in the delivery schedule, in combination with the date you selected in the End date field. You also see what the calculated end date has been calculated for.

#### Customer number, buyer
Here you can enter the customer who in the delivery schedule is set as buyer.

#### Customer's number as buyer
Here you can enter the number which the customer enters for themselves as buyer in the delivery schedule.

#### Transport time
Here you see/enter the transport time of the delivery schedule. By default, the value is loaded from the customer selected for the delivery schedule. It is possible to change transport time for a separate delivery schedule as long as it is open for editing, that is, as long as the delivery schedule has status New or Activated.
The date At customer on call rows means the Delivery date + Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver..
With each transfer of calls to customer order, the transport time in the customer order header will be updated with the delivery schedule's transport time, if it has been modified. If the transport time on delivery schedule and customer differs, a warning regarding the calls will be shown in the procedures Handle delivery schedules and Analyze delivery schedules.

#### Our reference
Here you can select among the persons in the company who are registered as references in the personnel records. If you start typing in the field, the system will suggest the reference that matches what you have typed. The More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) becomes visible after you have selected/entered a reference. Using it you can access information about the reference in question. The Our reference field will by default show the name linked to the logged-in user. If no such link exists, the user’s most recently selected Our reference, will be suggested.
Our reference on delivery schedule can also be decided via EDI behaviors.
