### Settings (procedure)
Here you configure settings for the Agent task of the procedure.

#### Default values
Here you can select among default values in the procedure selected in the box Selected procedures.
A copy of the default value Is saved. This copy is only used in the agent task. The purpose of this copy is to make sure that a user does not change the default values in the procedure which would affect the agent task

#### Filter
Here you can select a filter from the procedure selected in the box Selected procedures. A filter has to have been saved in the list in the procedure. If the filter is saved in a list which has been loaded using a default value, you must first select the default value in the above mentioned field before you can choose the filter.
Filters can be applied in many of the procedures in an Agent task. This field is not available if a filter cannot be applied.

#### Warehouses
If you have installed the option Warehouse, you can here select in which warehouse/warehouses the agent task should be run for each procedure. To be able to choose another warehouse than the one which the user is logged in to, the user must have sufficient user rights in that warehouse.

#### Printing method
If you have selected the Print delivery documents procedure, you must select the printing method E-mail, Printer, or both, for the documents that can be printed from the procedure in question. Depending on which printing method you select, you must enter an E-mail address for sender or a Server printer.
If you have selected any of the Handle delivery schedules – Purchase, Order confirmation reminder, Delivery reminder, Print invoice, Print payment reminder, or Print statement – Sales procedures, the printing method is always set to both E-mail and Printer. The field is then unavailable. You must in such cases enter both E-mail address for sender and Server printer.
If the selected procedure is Export annual volume the printing method will always be E-mail. The field is then unavailable. You must in that case enter a E-mail address for sender.

#### E-mail address for sender
Here you enter the e-mail address which will be shown as sender of delivery documents and invoices which are sent via e-mail when an agent task runs the procedures in question.
If the E-mail method system setting is set to Server based, via Microsoft Exchange, the field is always deactivated. In that case, the e-mail address entered as E-mail sender for result e-mail, will be used (and shown).

#### Server printers
Here you select the server printer you want to use when printing delivery documents and invoices when an agent task runs the procedures in question. The server printer must first be registered in the Server printers procedure.

#### Path for factoring export
Here you select a file path if you need to export factoring files in connection with invoicing. This means that this setting only applies for the Print invoice procedure. The path must first be registered in the Paths procedure.
