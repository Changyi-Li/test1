### Register purchase order
This is a description of how a purchase order with a payment plan is registered in Register purchase order.

#### The Header tab
Here you can specify if the purchase order should be paid as part of a payment plan. This is done in the Payment plan field.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanTerms.png)
The payment plan can also be set up automatically via a setting for the supplier. This is configured in the [Supplier register](../../../Purchase/Supplier/SupplierRegister/wSupplierRegister.htm) or [Supplier list](../../../Purchase/Suppliers/SupplierList/wSupplierList.htm).
If you want to follow-up on the order via the project accounting, you can enter a project number in the order header. The project number will then be automatically inserted on order rows which can be posted on projects, and on the partial invoices which handle project posting in the Payment plan tab. Please note! If you change the project on the order rows, then the advance and in arrears rows' posting will not become automatically updated. These must be changed manually.

#### The Rows tab
You register the purchase order rows as normal. That is, you don't add any rows for advances and in arrears here. However, there is an important checkbox on each row. You use this to determine which rows should be included in the payment plan. This is done via the Included in payment plan column.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanRegisterPOrder.png)](../../../../Resources/Images/TrainingMaterial/PaymentPlanRegisterPOrder.png)
Rows which are not included in the payment plan can be reported for arrival and paid in the usual way, separately from the payment plan – for example, an additional product to be delivered, or a freight charge.

#### The Payment plan tab
The order’s payment plan is shown in this tab.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanTab.png)](../../../../Resources/Images/TrainingMaterial/PaymentPlanTab.png)
In the upper box, you can see the different partial invoice rows, which are loaded from the payment plan template registered in the Invoicing/Payment plans procedure. It is possible to edit/delete/add rows. It is also possible to change name on advance invoice and in arrears invoice. For each partial invoice, you should enter a planned invoicing date. This is called the Invoicing period. This is used if you later want to be able to make a selection on what is to be released in the Payment plan list procedure.
In the lower box you see information about the order rows which are included in the invoicing plan.
At the very bottom of the tab you see different types of totals, according to the image above.

#### The Documents tab
When printing an order, you can see information about the payment plan. This information is displayed below the order rows. In the procedure [Document settings](../../../GeneralRegisters/DocumentManagement/DocumentSettings/wDocumentSettings.htm) you can choose if the information should be displayed or not.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanPOrder.png)
