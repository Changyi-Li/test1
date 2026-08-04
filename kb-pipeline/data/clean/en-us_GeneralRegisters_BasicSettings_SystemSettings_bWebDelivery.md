### Report pick list – Sales
Here you configure settings that are specific for the mobile client.

#### Show pick lists
Here you determine which pick lists the users should be able to see in the Report delivery in the mobile client. All alternatives below are activated by default.
- Not delegated – This alternative displays pick lists that are not delegated to a person, that is, no person has been selected to perform the picking.
- Delegated to other – This alternative displays pick lists that have been delegated to another person than the person who are linked to the logged in user in the mobile client.
- In progress – This alternative displays pick lists for which picking has been started by another person.

#### Sort order on order rows
Here you determine if order rows should be sorted by Main location Earlier called "Current location". Main location means the stock location for a part that has the most recent arrival date for the part. If you apply priority for the locations, then the main location is the location which has the highest priority (that is, the lowest number). or Location.

#### Default part number when adding an order row
(Optional). Here you determine which part number should be used by default when adding new order rows to the pick list.

#### Default quantity when reporting
This system setting determines if the quantity to deliver from location should be Zero (0) or Quantity in pick list. If you select Zero (0), then both the loaded location and the picked quantity must be entered. If you select Quantity in pick list, then both the loaded location and the picked quantity are suggested according to the pick list.

#### Print document after delivery
If you want to print delivery documents after delivery then you select Yes, with question or Automatic, without question.

#### Default documents when printing
This setting is activated if you have selected to print delivery documents in the system setting above. Here you determine which delivery documents you want to print. The available documents are Transport label and Delivery note. Both documents are printed by default.
> For the user who is performing the picking in the mobile client, a Server printer must be selected in the Users procedure for the documents Transport label, sales and Delivery note, delivered. The server printers must first be registered in the Server printer procedure.

#### Allow change of location
With this setting you decide if it should be allowed to change location in Monitor Mobile. The following options are available:
- Yes – the user can select another location to pick from instead of picking from the suggested location.
- No­ – picking

#### Use scanner
This setting determines whether the scanner should be used when reporting pick lists in Monitor Mobile. The following options are available:
- Mandatory – scanning is mandatory and the scanning field cannot be hidden.
- Yes, default – the scanning field is active and is visible by default but can by hidden.
- No, default – the scanning field is active but is hidden by default. It can be made visible and be used.

#### Scan location
This setting determines whether locations should be scanned in Monitor Mobile. The following options are available:
- Yes – the user should scan a location before the part identity.
- No – location is not scanned.

#### Count by scanning
This setting determines how parts are counted when scanning The following options are available:
- Yes – all part identities must be scanned to count the quantity.
- No – the first part identity must be scanned and then you may decide whether you want to scan the remaining part identities or enter the quantity manually.

#### Allow manual input
This setting determines whether you can manually enter Location, Identity, and/or Quantity.

#### Show pick instructions
Here you decide if the pick instruction should be displayed for Manufacturing order, Operation, and/or Material.

#### Pick list row is expanded by default when having pick instruction
This setting determines whether the pick list row expands by default when there is a pick instruction.
> "Identity" or "part identity" refers to part number, serial number, or batch. This depends on if the part is traceable or not.

#### Show pick instructions
This setting determines whether pick instructions are shown for Part, Customer link, Delivery row, Customer order, Linked text row on order, and/or Customer.

#### Pick list row is expanded by default when having pick instruction
This setting determines whether the pick list row expands by default when there is a pick instruction.
