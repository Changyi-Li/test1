### Release advance invoice basis and link supplier invoice
You can release an advance invoice basis in the following ways:
1. Via the Payment plan tab in the Register purchase order procedure.
2. Via the Detailed list type in the Payment plan list procedure.
To release an advance invoice via the Payment plan tab in the Register purchase order procedure, do as follows:
1.    
Place the cursor on the row to be released and click the Release supplier invoice basis button. You can also access this command via the context menu (right-clicking).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanRelaseAdvance.png)](../../../../Resources/Images/TrainingMaterial/PaymentPlanRelaseAdvance.png)
2.   
An invoice basis is then created (compare with arrival reporting an order row). You can also undo this command (if the basis has not yet been registered). This is done by clicking the button Undo release.
1.    
If the order has been partially delivered, you need to undo the release of the advance/arrears payment by using the Undo Arrival reporting procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentPlanRegSupplierInv.png)
1.   
Linking a supplier invoice relating to an advance is done in the same way as linking a regular order. In the Header tab, in the Register supplier invoice procedure, however, the partial invoice type Advance is displayed, as shown below, after the order is linked to the invoice.
If suspended VAT is to be handled on advance invoices, the system will automatically post the invoice on the account/VAT code for suspended VAT. However, this is provided the VAT code on the advance invoice row in the payment row is specified with a VAT code for suspended VAT. This can be configured automatically by setting an exception on the VAT code via the product group for advances in the VAT settings procedure.
1. To release an advance invoice via the Detailed list type in the Payment plan list, do as follows:
2. Select Include for the advance and in arrears invoice rows in the list that you want to invoice, and click the button Release Supplier invoice basis ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png). After that you are linked to the Register supplier invoice procedure to register the supplier invoice.
3. After that you are linked to the Register supplier invoice procedure to register the supplier invoice.
