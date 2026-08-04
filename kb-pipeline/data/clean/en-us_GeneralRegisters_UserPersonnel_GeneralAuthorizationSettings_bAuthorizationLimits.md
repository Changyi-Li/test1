### Authorization limits
In this box you can enter an authorization limit which applies to the order type for the user selected in the Users/Signers box. The order types are loaded from the Order types procedure.

#### Amount from and including
This field is empty by default. This means that no authorization limit is set for the user in question. The user can then save purchase orders with unlimited order amounts and the orders don't have to be approved. The amount entered here (in the company currency) will be the user's authorization limit. When you have entered an amount (from zero and up), you must also select a head signer in the next field.

#### Head signer
This field is activated when you have entered an amount in the field Amount from and including. Here you select a signer or signer group that should be allowed to approve the user's purchase orders if they exceed the entered amount. The selectable signers are users for which Signer of Purchase order has been activated, authorization lists, and also the created signer groups.
The actual approval is done in the Approve purchase order procedure.
