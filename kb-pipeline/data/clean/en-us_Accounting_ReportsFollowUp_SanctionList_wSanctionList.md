## Sanctions list
> The only users which by default have access to this procedure are the ones with any of the following roles: Financial manager, Financial assistant, or ERP manager.
The procedure is an option for companies which handle classified information, defense secrets, etc. These companies can here check information regarding customers, suppliers, and employees, against sanctions lists regarding financial crime and terrorism. The purpose is to make sure the companies are not in business with anyone on these lists, or has employees that are on these sanctions lists.
There is support for sanctions lists created by the EU, the UN, the United Kingdom, Switzerland, and the US. These lists can be activated, loaded, and updated by using a plugin called Sanctions lists under the Export tab in the Settings for export/import procedure. In this plugin you select which of the sanctions lists to activate as well as configure path and file name for where to save the sanctions lists when they are downloaded. There you also configure a Levenshtein distance. This refers to how much the tolerance should be (in number of characters) in order to get a match, for example for misspelled words.
Each activated sanctions list is displayed on a separate tab in this procedure. There are three different list types in the procedure to check data for customers, suppliers, and personnel, against the sanctions lists. See below.
In this procedure there is also a tab where you can create and save a whitelist consisting of different names and words which are considered OK, even if they might occur in any of the sanctions lists. This means that if a whitelisted word or name is found for example in a note/remark on a customer reference, then that record will be exempted from matching.
The matches found in the lists in the procedure can be exported to Excel, PDF, CSV, Word, or Clipboard in Windows, for further processing or reporting to the concerned authorities. You perform the export via the button Export ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_export.png) on the procedure's toolbar.
List types

#### Customers
With this list type you check the selected customers against the list. The information checked is: The customer's name on the header row and in the mailing address. Customer name when searching. Name and remark/note in all of the customer's references.

#### Suppliers
With this list type you check the selected suppliers against the list. The information checked is: The supplier's name on the header row and in the mailing address. Supplier name when searching. Name and remark/note in all of the supplier's references.

#### Employees
With this list type you check the selected employees against the list. The information checked is: Name in home address.
