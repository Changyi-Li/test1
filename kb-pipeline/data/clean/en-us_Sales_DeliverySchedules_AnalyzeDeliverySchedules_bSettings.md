### Settings – List type Requirements – Detailed
These settings are available for the list type Requirements – Detailed.

#### Show delivery horizon
Here you can choose a time horizon for changes.

#### Only calls before transfer date
This setting limits the result to only show changes where the delivery date is before the delivery schedule’s transfer date.

#### Show calls with no changes
By default only posts where the quantity has been changed are shown. If you activate this setting, also posts with no changes are included in the list.

#### Show only blocked parts with current requirement
If you activate this setting only blocked parts with demands are shown in the list. By activating this setting, you also activate the settings Block status and Only include if blocked activity is Register customer order.

#### Block status
This setting determines whether parts where block status is set to Block, Notify, or both will be included.

#### Only include if blocked activity is Register customer order
The blocked part will only be included in the list if the part is specifically blocked for register customer order.

#### Show only delivery schedules not replaced within the set time
With this setting checked you can list all parts in the delivery schedule that have not been replaced with a new delivery schedule within the time limit that has been entered in the delivery schedule type.
If the setting is activated, the list will only show parts in the delivery schedule which meet the following requirements:
- The status cannot be Replaced.
- Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. with Usage set to Delivery schedule.
- Date of creation is older than the amount of days entered in the delivery schedule type.
The setting Warn if schedule (or section) is not replaced within set time must also be activated for the delivery schedule type.

#### Show only calls with deviation alerts or warnings
With this setting you can choose to only include call-offs that have alerts for deviation or warnings, in the list. This box is deactivated by default.
