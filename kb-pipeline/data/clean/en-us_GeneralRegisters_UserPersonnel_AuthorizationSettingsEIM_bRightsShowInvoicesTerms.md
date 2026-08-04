### Terms (user rights group)
In this box you add terms that determine which invoices should be viewed or not for signers included in the user rights group in question.
The terms for user rights groups can be created in two ways. The invoices can be viewed or they cannot not be viewed. Below you find two examples of how to use user rights groups.
Example 1
You want to hide certain supplier invoices from the user. You then create a term with the viewing rule Invoices that cannot be viewed. Under Based on you select for example Supplier category and enter from which category it applies.
- This means that the user can view all invoices besides the invoices from the suppliers within the created term. However, the user can always view invoices that they have handled in the flow.
Example 2
You want to view certain supplier invoices to the user. You then create a term with the viewing ruleInvoices that can be viewed and select on which it should be based.
- This means that the user only can view invoices from suppliers within the created term. However, the user can always view invoices that they have handled in the flow.
- This can also be useful if you have a [signer group](bSignerGroups.htm) where the other members of the group who do not authorize invoices should be allowed to view all invoices from these suppliers.
For one and the same user rights group, you can create terms including both viewing terms. If you enter that the user can view invoices from supplier group 4 but not from supplier group 3, then the user can view invoices from supplier group 4 (plus the invoices they have handled themselves). According to the term, it is not possible for the user to view invoices from supplier group 1 and 2. If you enter that the user cannot view invoices from supplier group 3, then the user can view invoices from all other groups.

#### Based on
Here you determine on which the term should be based. You can choose supplier category, supplier, supplier role, supplier priority, or purchasing agent.

#### From
Here you enter or choose the selection on which the invoices should be based. For supplier group, supplier, supplier priority, and purchasing agent you can enter an interval in this field and in the field that is activated to the right. For supplier category you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to make a category selection if such is registered in the Categories procedure.

#### Viewing rule
Here you determine if the invoices within the selection can be viewed or not.
