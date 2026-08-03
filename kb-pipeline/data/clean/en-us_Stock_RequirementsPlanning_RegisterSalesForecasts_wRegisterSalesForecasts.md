## Register sales forecasts
In this procedure you can create forecasts to show expected future sales. These forecasts are then used in the requirements planning in order to see the requirement of quantities and delivery dates for parts.
- The purpose of sales forecasts is to extend the planning horizon, if the planning horizon spans a longer period than what contains registered orders.
- Sales forecasts can be an alternative to security stock, especially if requirements vary over time.
- Sales forecasts can give you manufacturing order suggestions which can be shown in the priority plan and the loading plan.
- Sales forecasts can give you a basis for delivery schedules for your suppliers.
Forecasts can be created in two different ways:
- Manually
- Via import of a text file Find out more about [importing via a text file](bImportSalesForecast.htm).
The data structure consists of forecast codes. Each code has forecast rows with parts where the configuration, quantity, and delivery date are registered. You can print the forecasts in the Sales forecast list procedure.
To be able to create, modify, and delete sales forecasts are determined by user rights.
Register sales forecasts from XML file
In cases where your customer also use Monitor ERP, the customer can send a delivery schedule to you as an XML file and PDF file in an e-mail message. This makes it possible to then import the XML file to this procedure from the desktop component Inbox for Monitor-to-Monitor. You can either drag and drop the entire e-mail message including the attached XML file and PDF file, or only the XML file. A new sales forecast is then automatically created based on the delivery schedule.
If you import a forecast where the unit does not match the unit of the part in Monitor ERP, a warning message is displayed and you get the chance to adjust the unit.
If the import has been interrupted earlier, you can open the sales forecast again from the Inbox Monitor-to-Monitor desktop component.
To register a new sales forecast from delivery schedule via XML file in an e-mail message is a function included in the [Monitor-to-Monitor](../../../UserGuide/GeneralFeatures/M2M.htm) feature.
If you have chosen to import using an already existing forecast code, then you can select among three alternatives:
- Add to existing records – Using this alternative the new values will be added to the existing values.
- Replace all rows in existing forecast – When using this alternative, all existing forecast rows will be removed and be replaced with the rows in the file. This means that only part B will have forecast rows when the import is completed.
- Only replace parts in the import file – If you for example have three parts A, B, and C in the existing forecast but only part B exists in the import file. Then existing forecast rows for part A and C will not be replaced, while the forecast rows for part B will be replaced with the rows imported in the file.

#### Keep deleted forecasts in database
Instead of the rows in the sales forecase being deleted in the database, you can use the system setting called Keep deleted forecasts in database to keep the rows in the database and have them marked as deleted instead. This makes it possible for you to follow up on how a sales forecast has developed over time.
