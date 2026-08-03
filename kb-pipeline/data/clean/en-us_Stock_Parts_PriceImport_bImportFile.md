### Import file

#### Type
Here you select which type of record you wish to import: standard price, supplier price, customer price, or price list.

#### Price list
If you have selected Price list under Type, here you select which price list you want to import.

#### Supplier/Customer
If you have selected Supplier price or Customer price under Type, you here select to which supplier or customer you want to import price by using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature.

#### Match part number with
This is available if you have selected Supplier price or Customer price under Type. Here you configure with what the part number in the import file should be matched in Monitor ERP. The options are:
- Our part number – This option means that our part number is matched with the part number in the file. If the part number does not exist in the part register in Monitor ERP, the price cannot be loaded.
- Supplier's part number – This option means the part number in the file is matched with the Supplier's part number field in the supplier link under the Purchase tab in the Part register procedure. If the part number does not exist in any supplier link, the price cannot be loaded. If the part number exists in multiple supplier links, then all supplier links will be updated.
- Customer's part number – This option means the part number in the file is matched with the Customer's part number field on the customer link under the Sales tab in the Part register procedure. If the part number exists in multiple customer links, then all customer links will be updated.
- Primarily the supplier's part number – This option means that the price will be loaded to the part (the supplier's part number in the supplier link) which is matched by the part number found in the file. If there is no matching with the supplier's part number, the matching is instead made with our part number number.
- Primarily the customer's part number – This option is the same as the option above but for the customer.
> To update future prices for staggered prices for customer linked prices, you should leave the Limit value, qty and Price columns empty. The order of the staggered prices in the columns will match the order of the current staggered prices.

#### File
By using the Path button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png) you can enter a path to the file. You will then see the file path in the field.

#### Format template
Here you can select a format among the formats created in the backstage of the procedure. When the system is new, only a standard template is available. If you have made any temporary settings for the format, which have not been saved as a separate template, this will be shown as Current settings (not saved template).
If you select the format template called Monitor-to-Monitor – Import you can import a CSV file generated in the Price list – Sales procedure, list type Order simulated price – External during import of supplier price. (If your supplier uses Monitor ERP and can then generate such a file.)
