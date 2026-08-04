### Part

#### Log WIP balance during price change
This system setting checks and logs the balance of the parts that are WIP during price change. A check will also be made to see which manufacturing orders will be affected by the price change. This is made to prevent differences between the accounting and the WIP value when standard prices are changed for parts in ongoing manufacturing orders.

#### Purchase on project for new parts
Here you determine if the setting Purchase on project in the Part register procedure should be activated by default for new parts.

#### Show annual budget, annual volume, and order quantity with current pace
This system setting determines if fields for annual budget, annual volume, and order quantity should be activated in thePart register procedure. Current pace is mostly applied during seasonal fluctuation in the consumption and when the planning is made according to stock refill. These fields define which annual budget, annual volume, and order quantity the part has with the current month's consumption pace.

#### Manage future sales prices
This system setting activates the fields Future price, Future valid through, and Future setup price on customer links in the Part register procedure. This is used when you apply future sales price for parts in the currency of the price list and in the parts' default unit.

#### Keep order quantity and calculated quantity in sync
With this setting you decide if Order quantity under the Planning tab in the Part register should be synchronized with the Calculated quantity under the Manufacturing tab in the Part register.
This system setting is only available in systems where the Warehouse option is not installed.

#### Exposure time
With this setting you decide if Exposure time should be applied for parts with traceability of the type Batch A batch is the set of components/products manufactured at the same time and made from the same original material.. When this setting is activated, new fields and list types becomes available in the following procedures: Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part, Part register, Location list, Serial number A serial number is a number that is used for traceability for parts on entity level. list, and Monitoring tasks.
When you use exposure time, a batch should always be seen as a unit with quantity X. This should be done for the Remaining exposure time to be calculated for the batch.
If you wish to move a part of a batch, you should always Split batch in order to obtain a unique batch number for each quantity.
Countdown of exposure time is only started/stopped via stock transaction/move in or out of a location of the type called Controlled environment. If you want a location to be a controlled environment, you configure this in the Location list procedure, in the Locations list type.

#### Allow up to 60 characters in part name
Here you decide if it should be possible to enter up to 60 characters in part names.
> However, part names containing more than 50 characters may cause the name text to be cut off when printing certain documents.
