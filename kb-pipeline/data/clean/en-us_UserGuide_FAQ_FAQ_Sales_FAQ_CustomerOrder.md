### FAQ– Customer order and deliveries
How do I delete a customer order that is connected to a manufacturing order/purchase order?
Unfortunately you are not able to delete the order from the system, but you can delete remaining quantity on the order in Report delivery.
Search the order number in Report delivery. Click Load­ ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) to load the order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_CustOrder2.png)](../../../../Resources/Images/FAQ/FAQ_CustOrder2.png)
Enter 0.00 in Quantity to deliver, check the Delete remaining box, and save.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_CustOrder3.png)](../../../../Resources/Images/FAQ/FAQ_CustOrder3.png)
The status of the order then becomes 9) Final delivery made, however no quantity has been delivered on the order. (See the image below.)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_CustOrder4.png)](../../../../Resources/Images/FAQ/FAQ_CustOrder4.png)
How do I create a customer order from a quote?
Under the Order header, the Customer order box in the Register quote procedure, click the Create customer order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_new.png) to create a customer order based on a quote. In the box you can then see the customer order that you have created.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_CustOrder1.png)
Can I change delivery date on a customer order that has the status final delivery made?
Yes, if you want to adjust/correct an actual delivery date, you can do so in the Delivery log procedure. To be able to make adjustments, you need to make the list updatable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png).
Why does it say there is no disposable balance when I want to report delivery?
Even though the info in the Part register says there is a balance for the part, this balance might be cleared to be used in an order and then it is not available. Another scenario is that you have a linked manufacturing/purchase order which has not yet been reported as finished (status 4).
Which procedure should I use to see registered/on hand customer orders in the system?
Use the Order list – Sales procedure. There you are able to customer orders with status 1, 2, 3, 4 and 5.
How do I determine which language is shown on the documentation that gets sent to the customer?
It is the document group that is set on Mailing address and Delivery address under the Settings for address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_settings_15x15.png) (the Contact information tab) in the Customer register which determines which language the documentation will be in. The same document group must be set on Mailing address and Delivery address for this to apply to the documents.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_CustOrder5.png)](../../../../Resources/Images/FAQ/FAQ_CustOrder5.png)
How do I delete a pick list?
Go to the Delivery planning procedure and choose the list type called Picking in progress. Select by e.g., pick list number or order number and click Load ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png). You then mark Include in the pick list and delete it by clicking Delete row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) and then click save ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png).
Am I able to link a blanket order after creating a customer order?
Yes, you can. In the Register customer order procedure, under the Rows tab, there is a column named Blanket orders where you can manually link the customer order with a blanket order. Please note that the Blanket order button is only active when there is a blanket order registered for the customer.
Can I exempt (“pause”) a customer order so it won't have any requirements?
You can delete the delivery date of the order row/s. This way, there will be no net requirement calculation. You can also set the customer order as Preliminary­ under Miscellaneous under the Header tab in Register customer order and deselect preliminary customer orders in the net requirement calculation.
How do I get the Delivery reliability on the desktop to show the delivery reliability for a rolling 12-month period?
Use the “t” command to select up to today and the command “t-365” to see 365 back in time.
You can read more about [the date parser](../../GeneralFeatures/GeneralFeatures.htm#Inbyggd_datumtolk_i_datumfält_med_kalender) here.
What does it mean if a customer order is Preliminary?
If you check the Preliminary checkbox, it means that the order will be marked with the text "Preliminary" across the order confirmation. A preliminary order exists in the order register and can be listed in the Order list – Sales procedure. It can be displayed in the planning window if you choose to show preliminary orders, but it is by default not included in the net requirement calculation. Also, a preliminary order cannot be delivered. Preliminary orders can be useful if you e.g. aim to continue working with an order later on and cannot finish it completely at the time of registration. In the procedure Order types you can decide if Preliminary customer order should be default for the order type.
Why is list type Picking plan empty?
The Picking plan list type in the Delivery planning procedure may be empty if the Impose a time limit on delivery horizon setting is activate.
How do I edit a Total row (row type 3) on a customer order?
Mark the total row you want to edit and then click the Edit total button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_total.png) in the function menu to the left.
Why does the prise on the order row become 0 when I use staggered price?
You must always enter a price in the Price each field on the customer link in the Part register in order for the staggered price from the customer link to show on the order row. Otherwise the price will be shown as 0.00 on the order row.
How do I register a customer order for a customer without having to register the customer in the Customer register?
There must always be a customer registered for a customer order. One way of solving this is to register a so-called “stray customer”. "Stray customerA customer which only makes an occasional purchase. "Stray customer" is a customer number that is used for different customers for one-time sales (non-recurring). Therefor these customers do not have to be registered in the customer register." is a customer number that is used for different customers for one-time sales (non-recurring). Therefore, these customers do not have to be registered in the customer register. Under the Settings tab under the Miscellaneous heading in the Customer register procedure, you mark the checkbox called Stray customer for the customer you will use for "occasional sales" or "one-off customers".
If the setting Stray customer has been checked it means that printouts of reminders, if any, for that customer number will be divided per invoice and will not be gathered to a single reminder. That way, you can separate the reminder printouts for the different physical customers.
For stray customers (occasional customers), the e-mail address entered in the invoice header will always be used when sending invoices via e-mail. The e-mail address from the Customer register is never used, regardless of how the setting Recipient of invoice via e-mail is loaded from is configured.
