### Export/Import
In this box you, for example, enter information for Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reports used for import and export between two EU countries.

#### Net weight
The part's net weight can be entered by using two to five decimals. The unit is always kg. This field does not exist for parts of the Service type.
The net weight is also used for calculation of emissions from transports. If the part's standard unit is kg, it is important you set the net weight to 1 in order to get a correct emission calculation.
If no net weight has been entered for the subcontract part in the Subcontract parts procedure, the net weight you enter here will be used as fallback when calculating emissions for transports to and from the subcontract.

#### Fixed weight
By activating this setting you decide that the part's net weight should be fixed and the recalculation will not automatically be saved in the Calculate weight procedure. Fixed weight is used, for example, for parts processed from a raw material where the finished product's weight is lower than the weight of the total material. For these parts you manually enter the net weight and it will not be overwritten during the next calculation.
However, for a part where Fixed weight is activated it is possible to calculate the weight and save it in the Calculate weight procedure.

#### CN code
Here you can choose a CN code (goods code) for the part. These codes are handled in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part. This filed is shown depending on the warehouse in which the logged in user is working. Since CN code is only used for trading between two EU countries, the logged in warehouse must be an EU country in order for the field to appear. It also determines if the CN code should be included in different environmental/sustainability report, for example, CBAM.

#### Country of origin
In this field you can choose a country of origin for the part, that is, the country in which the part was made The name of the country is shown to the right of the field. Country of origin can then be selected to be displayed on the following documents: delivery note, invoice, and pro forma invoice (if the document setting in the Customer register procedure has been set to show country of origin).
The country of origin entered for a part can also be used when reporting Intrastat export. In this case, the country of origin for parts will override the country entered in the Company information procedure.

#### Use country of origin fr. serial no./batch, if available
You can activate this setting if the part has traceability set to batch or serial number under the Stock tab.
With this setting you decode which country of origin should be reported in the Intrastat export procedure and should be displayed on the following documents: delivery note, invoice, and pro forma invoice (if the document setting in the Customer register procedure has been set to show country of origin). If one and the same part number is purchased from different countries, and you handle the part for both sales and purchase, the system can use traceability to determine from where a certain part was purchased (the country of origin), in connection with invoicing. In this case, the country comes from the country for the supplier which is linked to the serial number/batch. This country overrides the country entered as the country of origin on the part, or which is specified in the Company information procedure.
