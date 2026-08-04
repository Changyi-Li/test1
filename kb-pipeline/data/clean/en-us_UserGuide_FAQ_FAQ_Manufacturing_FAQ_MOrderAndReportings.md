### FAQ – Manufacturing order and reporting
How do I delete a manufacturing order if I cannot use Delete (the eraser icon)?
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder5.png)
Deleting a manufacturing order does not work.
If you cannot delete an order via Delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) in the Register manufacturing order procedure, you can instead delete the order in the Quick reportingQuick reporting means that the entire manufacturing order becomes reported as finished in one single step, including deletion of remaining quantity, if any. procedure. Choose the Delete remaining list type and enter the order number under the Selection tab.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder6.png)
The settings to delete an order in the Quick reporting procedure.
Mark Include and then click Save. See the image below.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder7.png)](../../../../Resources/Images/FAQ/FAQ_ManufOrder7.png)
Delete an order in the Quick reporting procedure.
This sets the Remaining quantity to zero and the order is assigned status Finished. This does not affect transport to stock or material withdrawal.
Why do I get a validation that an Account needs to be entered when I create a manufacturing order?
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder1.png)](../../../../Resources/Images/FAQ/FAQ_ManufOrder1.png)
Validation that an account must be entered.
This is due to the part containing subcontracts that do not have the correct posting.
Check that the correct product group is set under Subcontract information in Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register or in the Subcontract parts procedure. The system setting Posting of subcontract purchase according to product group on determines in which procedure product group should be entered.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder3.png)](../../../../Resources/Images/FAQ/FAQ_ManufOrder3.png)
Product group in Work center register.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder2.png)
Product group in Subcontract parts.
If the product group is correct, you need to check that an account has been entered for the product group. You do this in the Posting matrix procedure under the Purchase account tab.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_ManufOrder4.png)](../../../../Resources/Images/FAQ/FAQ_ManufOrder4.png)
Posting matrix, account settings for product group.
How do I report subcontracts? It can’t be done in the Report manufacturing order/Report operation or in the Recording terminal.
On the subcontracts row, there is a purchase order which is created in the Subcontract documents/Shipped procedure. After you have reported arrival of this purchase order, the subcontracting is reported with the quantity you have selected to report.
> You can go to Register purchase order via the link and from there you can go to Reporter delivery and select quantity to deliver.
I have changed the quantity on a manufacturing order but the linked purchase order for the subcontract doesn’t change, why?
If the Quantity column does not change on a purchase order, it is because the purchase order no longer has status 1 Registered. You need to change the status on the purchase order to status 1 Registered before you are able to change the quantity on the manufacturing order. The quantity then changes both on the manufacturing order and on the purchase order.
Is there a list where I can see which manufacturing orders will be started today?
Use Order list – Manufacturing and sort by Start date order or Operation.
Is there a setting that deducts the remaining quantity for operation and material when we report rejections?
Yes, this is done via the Deduct remaining qty for operation and material at rejection system setting.
Why don’t I get a result on the number of reported hours in Manufacturing order log and Operation follow-up when I search a date interval?
That’s because these procedures are intended to be used differently.
The Manufacturing order log shows everything that has been reported on a certain day. Time is displayed regardless of the operation’s status. It is the report date that is searched.
The Operation follow-up procedure shows all reported hours for the operation if the operation’s finish date is within the given interval, which is good if you want to compare planned time and reported time for the operations. This is the why time is only shown for finished operations and the finish date is searched.
