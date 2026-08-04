### Settings
In the Settings box, you decide how the code should be built up with various fields. For the Default template, it’s not possible to change the order of the fields. The Default template works well for Monitor-to-Monitor and is default for all configured suppliers. The Default template is determined by a prefix. When a string is determined by a prefix, the order of the fields is not relevant.
The order of a sequential string’s fields is relevant and a prefix is not required.
The following fields match with the 2D code on the supplier document.
| Field | Prefix | Additional text field | Is matched against |
|---|---|---|---|
| Part number | P |   |   |
| Supplier's part number | S |   |   |
| Order number | C |   | Is matched against your order number on the customer order. |
| Delivery note number | N |   |   |
| Quantity | Q |   |   |
| Position | R |   |   |
| Customized |   |   |   |
Customized is used with a sequential string to identify a part of a string which should be excluded when loading.
