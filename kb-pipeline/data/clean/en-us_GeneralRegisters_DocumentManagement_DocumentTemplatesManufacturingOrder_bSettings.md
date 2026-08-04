### Settings
In this box you can see and modify all settings for the selected document variant of the manufacturing order document.
In the tables below you find a description of all settings. They are sorted by sections.
Header
| Setting | Description |
|---|---|
| Default no. of copies | The default number of copies that you want to print of the document. |
| Decimals on quantity | The value in the quantity column on the rows will be shown in decimals on the document. If not, rounding is made to the nearest whole number. |
| Show configuration | Shows product configurations on the document. |
| Show maintenance plan | Shows the form belonging to the planned maintenance. This applies to systems with the Tools & Maintenance option. |
| Show control plan | Shows the form with calibration points/measuring data belonging to the planned maintenance. This applies to systems with the Tools & Maintenance option. |
Text
| Setting | Description |
|---|---|
| Show order's manufacturing comment | The manufacturing order's manufacturing comment will be shown in the text section on the document. You can choose to show None, Only comment, Only linked files, or Both comment and files. |
| Show part's manufacturing comment | The part's manufacturing comment will be shown in the text section on the document. You can choose to show None, Only comment, Only linked files, or Both comment and files. |
| Show part revision | The part's active revision will be shown in the text section on the document. |
| Show part revision comment | The part's revision comment will be shown in the text section on the document. You can choose to show None, Only comment, Only linked files, or Both comment and files. |
| Show drawing number and drawing revision | The part’s drawing number on the first row and active drawing revision will be shown in the text section on the document. The available alternatives mean: None will be shown. Only comment (drawing number and drawing revision) will be shown. Only linked files to drawing revision will be printed with the document. Both comment and files (drawing number and drawing revision) will be shown and files will be printed. |
| Show part's additional name | The part's additional name, if any, will be shown in the text section on the document. |
| Show customer's part number | The customer's part number from the customer link on the part will be shown in the text section on the document. |
| Show internal comment from customer order | The internal comment on the customer order will be shown in the text section on the document. |
| Show order's part status | The manufacturing order's part status will be shown in the text section on the document, but only if it deviates from status 4 (Normal). |
| Show revision comment for part status 5 | The part's revision comment for the active revision will only be shown if the part has status 5 (New revision). This setting applies provided that the setting Show part revision comment has not been set to None. |
| Show the part's location | The part's location will be shown in the text section on the document. |
| Show serial number | The serial number will be shown on the document. |
| Show customer order row's goods label | Here you determine if the customer order row's goods label should be shown on the document. |
| Show cust. order row comment | With this setting you decide whether the first linked row type 4 to the part found on the customer order row should be displayed on the manufacturing order. |
| Show variant code | With this setting you decide if the variant code will be shown on the document. It can contain a maximum of 20 characters. If more characters are required, you can change the document layout. |
Operations
| Setting | Description |
|---|---|
| Show operations | For travelers you can determine if None or All operations should be shown. For operation documents you can determine if Active operation or Active including previous and next operation should be shown in the operation section on the document. |
| Show instruction | For travelers and operation documents you can choose to show None, Only comment, Only linked files, or Both comment and files. |
| Show times | The operation's setup time, unit time, and total time will be shown on the operation row in the document. The setting Show times affects the settings regarding unit on setup time, unit time, and total time as well as the setting called Show cost for subcontract. |
| Unit for unit time | Unit times can be shown in Minutes, Hours, Quantity/minute, or Quantity/hour. |
| Unit for setup time | Setup times can be displayed in Minutes or Hours. |
| Unit for cycle time | Cycle times can be displayed in Minutes or Hours. |
| Unit for total time | Total times can be displayed in Minutes or Hours. |
| Show cost for subcontract | The cost for subcontract will be shown on the operation row on the document. |
| Show goods location from previous operation | For operation documents you can determine that the operation's goods location from previous operation will be shown on the row for previous operation on the document. |
| Show quantity | The operation's quantity will be shown under each operation on the document. If Extra % or Setup quantity has been entered on the operation in the BOM and routing, the quantity on the operation can differ (be greater) from the quantity on the order. |
| Show report number | The operation's report number will be shown on the operation row on the document. |
| Show bar code (for report number) | The operation's report number will also be shown as bas code below each operation on the document. |
| Show start time | The operation's start date and time will be shown below each operation on the document. |
| Show finish time | The operation's finish date and finish time will be shown below each operation on the document. |
| Show control plan | On travelers you see all measuring points in a Measuring plan as a separate page. On operation documents you see the operation's measuring points below the material list. |
Material
| Setting | Description |
|---|---|
| Show material | This setting determines if information about the materials' "For operation" should be shown in the material section on the document. The available alternatives are None or To active operation. The latter alternative activates the settings below. |
| Show instruction | The material's instruction in the BOM and routing will be shown under each respective material row on the document. |
| Show standard unit | This setting determines if the material should be shown with the unit used during Material withdrawal for manufacturing order in the part register, if the material has several units, |
| Show report number | The material's report number will be shown on the material row on the document. |
| Show bar code (for report number) | The material's report number will also be shown as bas code below each material on the document. |
| Show location and balance | You can choose to show None, All, or Suggested location and its stock balance on the material row on the document. The location that will be suggested follows the rules for material withdrawal. That is, first the cleared location is suggested, then the pick location, then by priority on location, and finally via age analysis. |
| Only show material with remaining quantity | Only material with remaining quantity will be shown in the material section on the document. |
| Show weight calculation | Here you decide if weight calculation data should be displayed on manufacturing order documents. |
Tools
| Setting | Description |
|---|---|
| Show tools | This setting determines if information about the tool's "For operation" should be shown in the tool section on the document. The available alternatives are None or To active operation. The latter alternative activates the settings below. |
| Show instruction | The tool's instruction in the BOM and routing will be shown under each respective tool row on the document. |
| Show location and balance | You can choose to show None, All, or Suggested location and its balance on the each tool row on the document. The location that will be suggested follows the rules for material withdrawal. First the location that has cleared material for the order will be suggested. Then the suggestion will be determined by pick location, priority on stock location, and finally age analysis. |
| Show standard unit | This setting determines if the tool should be shown with the unit used during Material withdrawal for manufacturing order in the part register, if the tool has several units, |
| Show report number | The tool's report number will be shown on the tool row on the document. |
| Show bar code (for report number) | The tool's report number will also be shown as bas code below each tool on the document. |
| Only material with remaining quantity | Only material (tools) with remaining quantity will be shown in the tool section on the document. |
Footer
| Setting | Description |
|---|---|
| Show footer | The footer will be shown on the document. |
| Show | With this setting you decide if Production engineer info or Info from next level, should be displayed. |
General
| Setting | Description |
|---|---|
| Quantity | Here you can choose to show the order's Planned or Remaining quantity on the document. |
