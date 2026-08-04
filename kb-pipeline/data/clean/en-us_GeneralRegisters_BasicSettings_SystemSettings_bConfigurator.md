### Configurator

#### Total of price on order row
This system setting determines if the price on an order that contains a configured part should be totaled as Net or Gross + discount.
If you select Net, the part's net price from the configuration will be displayed in the Price each field on the order row. Any discount entered in the configuration will not be displayed on the order row. 0,00% will then be displayed in the Discount field.
If you select Gross + discount, the part's gross price from the configuration will be displayed in the Price each field on the order row. Any discount entered in the configuration will be displayed in the Discount filed on the order row.

#### Show on sales document
Here you determine which configuration information should be displayed (in a section) below quote rows, customer order rows, and invoice rows that contain a configured part. It is possible to make exceptions from these settings directly on options (parts) in option lists. The following alternatives exist and can be combined:
- Heading – The name of the option lists to which the options (parts) in the configuration belong.
- Part number – The part number and variant code, if any.
- Text – The part name (the selected part).
- Quantity – The part quantity in the configuration.
- Price each – The price each for the part.
- Discount – The discount that applies to the part.
- Net price – The part's price after discount.
- Amount – The quantity × net price.
- Image – The part image (the image file is linked in the part register).

#### Show on purchase documents
Here you determine which configuration information should be displayed (in a section) below inquiry rows and purchase order rows that contain a configured part. It is possible to make exceptions from these settings directly on options (parts) in option lists.

#### Show on manufacturing order documents
Here you determine which configuration information should be displayed on manufacturing order documents. It is possible to make exceptions from these settings directly on options (parts) in option lists.

#### Show the linked text row for configuration info on the following documents
Here you determine on which documents (text type) a text row that describes the configuration should be displayed. No text types are selected by default. The text shown on the text row is the name of the option list and option (part). The text row is primarily used to display information in different lists.
> On documents, the information will instead be displayed in a document component. If you change this system setting, you should also deactivate the document setting Show configuration for the affected documents.

#### Show excluded options in option list
(This system setting is currently not in use).

#### Price alternative for calculation of CM in the configuration window
Here you determine which price alternative you want to use when calculating CM The contribution margin (CM) is the difference between the standard price and the sales price. in the configuration window. The available alternatives are: Standard price, Future standard price, Price list, and Future price list. Standard price is selected by default. If you choose one of the alternatives for price list, you should also select a price list in the field below.

#### Price list
Here you select the price list that should apply if the price alternative used to calculate CM is: Price list or Future price list.

#### Include order row qty for staggered sales prices on options
If you select Yes, the staggered sales price will be calculated based on the option's (included part's) quantity in the configuration multiplied by the configuration's (main part's) quantity on the order row.
If you select No (default), the staggered sales price will be calculated based only on the option's quantity.

#### Merge options with the same part number
With this system setting you decide if the quantity of the selected parts in option lists should be added together to/merged into a single material row on manufacturing orders, if they have the same order number. A total will always be made per main part.
The following options are available:
-   
No – With this option, no merge into one material row will take place.
-   
Yes, options with same For operation – If the selected parts have the same Part number and the same For operation, the parts will be merged into one material row on manufacturing orders.
-   
Yes, options with same For operation and Position – If the selected parts have the same Part number, the same For operation, and the same Position in the option lists, the parts will be merged into one material row on manufacturing orders.
> The selected parts in configurations are also added together with the material rows from the BOM and routing. This means that a row in the BOM and routing can be "removed" on a manufacturing order by in the configurator selecting the same part with a negative quantity. For example, you select -1.00 in the configuration and the same material has a quantity of 1.00 in the BOM and routing (-1+1=0). Rows in which the quantity after total is 0 are not included in the manufacturing order. Please note! Material rows in the BOM and routing whose quantity is zero will still be included in the manufacturing order. It is only when the quantities are totaled via the configurator that rows whose quantity is zero are not created. If the same part is found on multiple rows in a regular BOM and routing, not total will takes place. Information in instructions from the rows included in a total row will be managed in accordance with the system setting called Manage instruction from included fictitious part's material row, where you can choose to add, keep, or replace the information. Please note! Text from rows with a negative quantity will not be included in the resulting text, if you have chosen one of the merging alternatives. If you only total/merge per operation and not per operation and position number, the position number (if any) will be merged until the Position field is full. The same applies here, that position number will not be included for incorporated/include rows with a negative quantity.

#### Copy extended description to option comment
If this system setting is set to Yes, an extended description (entered under Configuration for the Miscellaneous button in the Part register) should be copied to the option comment in the configuration if the part is selected. This option comment is shown and can also be edited by clicking the OC button under the Result tab in the configuration window.
To avoid having the text shown twice on documents, this setting will also result in documents not displaying the extended description, but only the option comment.
If the setting is set to No, the extended description will not be copied to the option comment. This way, both option comments and extended descriptions will be shown on documents.

#### Option is inherited if beginning of part number is identical (enter 8-20 characters)
This system setting can be used if you apply the Inherit options setting in option lists. Here you can configure that options not included in the option list on the next order row, will anyway be inherited to the next order row. The condition for this is that the option lists have the same Identifiers as well as having the same first 8-20 characters of the part numbers. The default value is 0. This means the setting is deactivated. Allowed values are 0 and 8-20.

#### Calculate CO2e value for configured parts
With this setting you decide if a CO2e value for the configuration should be calculated or not The default alternative is No. The purpose of this setting is to avoid the warnings you will receive if there are values missing in order to perform a complete calculation. Activate this function when you have sufficient values in the system.
