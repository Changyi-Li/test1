### Location

#### Create new location at arrival
This system setting determines if a new location should be created when parts arrive. The alternative Yes, only traceable material means that a new location is created only during arrival of traceable parts.

#### Name new locations at arrival
With this setting you determine if a location name should be suggested for a new location created at arrival or if the location name should be empty by default. The suggested names location names can be ******** or a consecutive number shown as *1001*, *1002*, up to and including 9999.
Validation rules for location names
If No name was set for the system setting, only generated location names are valid. Location names are generated in the Generate locations procedure.
If ******** was set for the system setting, it means generated location names and location names with ******** are valid.
If Consecutive number: *1001*, *1002* etc. was set for the system setting, it means generated location names and location names with consecutive number *1001*, *1002*, up to and including *9999*, are valid.

#### Apply arrival location
This system setting determines if it should be possible to apply arrival location. Arrival location is then entered for the part in the Part register, under the Stock tab.

#### Apply pick location
This system setting determines if it should be possible to activate pick location and pick location for work center on locations.

#### Check location name
Here you determine if validation of location names should be made of transactions that result in transfer to stock. The validation is made when the user enters a location name. The following options are available:
- Inactive – No validation of location name takes place at transfer to stock.
- Warn – A message appears if the selected location does not match any valid location name. However, the transaction will be executed.
- Block – If the entered location does not match any valid location name or consecutive number, the transaction will not be executed. You must then select a valid location. However, you can also register the requested location name first and then select it at transfer to stock.
Under the Stock tab in the Part register procedure, the Stock location system box will be activated when this setting is configured to Warn or Block. In this box you can select a location selection for the part in question. This can also be made for several parts at the same in the list Location selection – Part in the Location list procedure. Selection criteria must first be registered in the Location selection procedure.

#### Apply the setting on existing locations as well
With this setting you decide if the setting called Check location name above will also check the existing locations for the part and verifies if the location name is valid. The available options for the setting are Yes and No.
