### Linked requirement and supply planning
For parts with the control method Order oriented it is possible to link the customer order's requirement to its manufacturing order or purchase order. This is done by using the lot sizing rule Linked requirement for the part instead of the lot sizing rule Lot-for-lot.

#### The difference between Linked requirement and Lot-for-lot
A big difference between linked requirement and lot-for-lot is how the requirement is linked to different supplies:
- When working with linked requirement, each requirement will be linked to a unique supply/asset. For example, this means that net requirement calculations will create one manufacturing order for each customer order row (the same will apply to stock order "out"). This means that there might be multiple manufacturing orders per day.
- When using the lot sizing rule "lot-for-lot", a maximum of one manufacturing order can be created per day. This means that several requirements can be covered by the same manufacturing order. That means that the manufacturing order can not be marked for a specific customer.

#### Automatic updates and managing changes
When linked requirement is activated for a part, the system will make sure that all changes made on the customer order (for example changed quantity or date) will also be made on the linked manufacturing order or linked purchase order.
If you instead try to make manual changes to the manufacturing order or purchase order, the system will warn you of this way of working. You should modify the requirement, not the supply, otherwise you risk damaging your planning.

#### Requirement and supply in the system
What creates a requirement in the system is either a customer order or a manufacturing order. As supply, the system can create a manufacturing order, a purchase order, or a stock order (stock order is included in the option called Warehouse).

#### Requirement calculation when there is a linked requirement
For a part with a linked requirement, the requirement calculation will not take the following into consideration:
- Existing stock balance.
- Manufacturing orders or purchase orders that do not have linked requirements.
The system will still suggest that more parts should be acquired. This behavior also affects:
- Pick lists
- Clearance lists
- Material rows in Manufacturing order info
Instead of checking the disposable balance, the system will only search for linked supplies to all requirements. This means that if you purchase extra for an order row or if you add a manual purchase order, these will not be included in the requirement calculation.

#### Manufactured parts
It is possible to have a link between customer order and manufacturing order also when Linked requirement has not been activated for parts. However, you then need to create the manufacturing order directly from the customer order in order to be sure that a manufacturing order is created linked to customer order row.

#### Purchased parts
When Linked requirement is activated for purchased parts, all material requirements will be linked to a unique purchase order row. All changes made on the customer order or the manufacturing order, will automatically affect the purchase order as well.
If a warehouse has been selected for a purchased part, by using the setting Refill from warehouse (included in the option called Warehouse), no linked purchase order will be created from a customer order row for the part in question.
