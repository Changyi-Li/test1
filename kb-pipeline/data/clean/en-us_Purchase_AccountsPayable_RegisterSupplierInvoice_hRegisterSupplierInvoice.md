### Header row
The header row in the procedure is the starting point when you wish to register a new supplier invoice. If you use the option Electronic invoice management (EIM) you will also find an inbox in the Navigation box that is used when registering a new invoice.

#### Consecutive number
Here you enter the consecutive number of the supplier invoice. You can here select a consecutive number if you wish to load an existing invoice. A new invoice will be given a consecutive number from the number series when the invoice is saved for the first time.
After you have saved, the procedure will be reset to the initial mode and be emptied from information. In the Last registered field you can see the consecutive number that was given to the invoice that was most recently registered.

#### Supplier
In this field you see/enter the supplier who has sent the invoice. If you do not use the Electronic invoice management option (EIM), you start by selecting a supplier for the new invoice. This is either done in this field or indirectly via the Order number field (provided that it is an order invoice with a purchase order).
By using the button Change supplier ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can change the supplier for an already registered invoice. This ca be done as long as the invoice is not final recorded. Under the Order link tab you can see all arrival reported purchase orders, if any, for the supplier. You can select which purchase order(s) to be included in the link to the invoice.
The previous supplier can be suggested after you have saved the invoice and want to register a new invoice. This is activated by the system setting Suggest previous supplier at registration.
If a messages has been set for the supplier, this will open automatically when you enter the supplier. You can also see the this message by using the Show message button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Order number
Here you see/select the purchase order number to which the supplier invoice should be linked. The supplier is loaded from the purchase order. If you have activated the system setting called Load invoice information from purchase order, some information will be loaded from the purchase order. This applies to, for example, Payment term, Currency, VAT group, and Supplier group (import of Monitor-to-Monitor invoices is an exception where the information is mainly loaded from the XML file). If you select a purchase order that is not arrival reported, you will see a warning. If you have already selected a supplier in the field Supplier and then select a purchase order that is registered for another supplier, information about this will be displayed. You will also be asked if you wish to change the supplier on the invoice basis to the supplier in question on the selected purchase order.
Under the Order link tab you can then see all the fully or partially arrival reported purchase orders, both for the selected supplier and also for the supplier of the selected purchase order, if they are not the same. The selected purchase order is by default included in the link to the supplier invoice.

#### Invoice's status
In this field you see the current status of the invoice, it can be:
- New registration – The invoice is new and has not yet been saved (does not have a consecutive number).
- Registered – The invoice is saved and registered (has a consecutive number). The invoice will be given this status if preliminary entry of invoices is not applied.
- Preliminary recorded – The invoice is saved and preliminary recorded (has a consecutive number). The invoice is given this status, instead of the Registered status, if preliminary recording of invoices is applied. This is activated with the system setting Preliminary entry of supplier invoices.
- Final recorded – The invoice is final recorded.
- Ordered – The payment has been ordered but is not yet executed.
- Partially paid – The invoice is partially paid.
- Fully paid – The invoice is paid in full.
- Canceled – The invoice has been canceled.

#### Last registered
Here you see the consecutive number for the most recently registered invoice.

#### Status EIM
The field Status EIM is shown if the option Electronic invoice management (EIM) is installed. The following status options exist with EIM:
- Pending – The invoice was set to pending at the registration, that is, it is waiting for further action. For example, this can be necessary if you when registering, find that the invoice needs to be complemented with additional information or that you want to wait for a purchase order to be arrival reported before going ahead with the handling of the invoice.
- Sent for authorization – The invoice has been sent for authorization, that is, it has been sent to a group of people who has to authorize it in a specific sequence. The name within parenthesis shows at whom in the sequence it is located at present.
- Authorization completed – Everybody has authorized the invoice and it is now available for final coding in the navigation panel.
- Rejected – The invoice has been rejected during the authorization round, and is therefore sent back to the financial department.
- For final recording – The invoice is available for final coding.
- Final recorded – The invoice has gone through the authorization round/sequence and has also been final recorded.
- Filed – The invoice has been filed.

#### Save without image
This setting is available if EIM is installed in your system. To be able to save an invoice without an invoice image (PDF), you must select the Yes option for this setting.
