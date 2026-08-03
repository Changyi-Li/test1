### Locations
Here you can add information which by default should be included for new parts with this template selected. If you select this template for an existing part, this information will also be copied by default to the part, but then it is optional.

#### Location
In this column you see the name of the location. For a new location, ******** will be entered by default as name, but you can change it as you please. However, you can only use 35 characters.
> It is not possible to rename a location which already has a balance.

#### Pick location
The system setting Apply pick location has to be activated in order for you to be able to check this setting. This setting determines if the location should be a pick location for withdrawal of a part to manufacturing order or customer order. Only one location can be pick location for the part.
If pick location is activated for the location, it is also possible to enter the reorder point in the next field and refill quantity in the following field.

#### Pick location for work center
The system setting Apply pick location has to be activated in order for you to be able to check this setting. This setting determines if the location should be a pick location for work center for withdrawal of a part to manufacturing order. Several locations can be pick location for work center for the part.
If pick location for work center is activated for the location, it is also possible to enter a reorder point and a suggested refill quantity in the following fields.
Pick location for work center is primarily intended to supply the manufacturing order/work center. Therefore, these will be placed last in the list over locations from which withdrawal should take place when needing quantity for e.g. customer order rows. Settings and search criteria for Default location in the work center register determine if the pick location for work center should be suggested when it fulfills your search criteria.

#### Reorder point
Here you can enter a reorder for the pick location.

#### Refill quantity
Here you can enter a default refill quantity for the pick location.

#### Exclude balance
Here you determine if the balance should be excluded during net requirement calculation, requirement calculation, and check delivery times. This is useful if for example the location contains overflow or wastage material that can be used but should not be considered as supply during requirements planning.
> Please note! Excluded balance does not apply to clearance, picking, stock count, and stock valuation. If, for example, a user registers a manufacturing order, the quantity on the order will be reserved against the balance even though this setting has been configured.
