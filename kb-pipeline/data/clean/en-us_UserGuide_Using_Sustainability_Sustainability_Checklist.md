### Emissions – CO2e – Checklist
This is a summary checklist which can be used to help you get started and using the sustainability functionality for CO2e in Monitor ERP.
Data in the following registers is used in the CO2e calculation.

#### Basic data – Sustainability
In the Material types box under the Emission factors tab you can enter general emission factors for different materials. These factors are then used to enter emission factors for purchased parts in the Part register procedure.
- In the Other emissions box you register other emissions with a descriptive name and a link to rows in the company's sustainability report according to the GHG protocol. These can then be used in the Company emission register procedure to create a more detailed specification specification of the different emission categories. You select the emission type among the different rows/categories available in the sustainability report. The selected emission type determines the Scope category and Scope.
- In the Energy sources box under the Emission factors tab, you enter the electricity mix that your company uses (this can be found on your electricity bill), as well as how big each part of the mix is. This is used to calculate emissions in production via electricity usage per work center.
- Company emission register
- The company emission register is used to register your company’s emissions on a yearly basis. These values are used when reporting the company's emissions according to the GHG protocol (Green House Gas Protocol Corporate Standard). This information is also the basis of calculations in the sustainability calculation made for parts.
- In the Year field you enter the budget year for the emissions with a Start date and an End date.

#### With the Allocation key for OH you decide how the emissions handled as overhead should be distributed/allocated. You can choose among the following allocation keys: Quantity, Total production time, and Weight. Also enter an annual value for the allocation key you have selected. For example, 120.000 sold units if you selected to allocate by quantity.
- In the box containing the different scopes and the sub-categories, you enter the company’s Total emissions for each sub-category. You also enter the share of these that should be distributed as OH in the Distribute as OH column. The overhead (OH) is everything that is not included in any other way in the calculation. You can add several sub-categories if you have registered Other emissions in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Sustainability procedure.
- Terms
- Add Emissions CO2e using the unit gCO2e/tkm under the Delivery method tab. This information is used when calculating transport emissions. Please note! The unit gram CO2e is used here and not "kg CO2e" which is used in most parts of the system. It is entered per tkm which is ton x kilometer.
- Check the Payer under the Delivery terms tab. Only the emissions that are to be paid for by the purchaser as per the delivery terms are included in the sustainability calculations.

#### Part register
- Update the Material type and the Emissions for purchased parts under the Sustainability tab. Manufactured parts get their values from the sustainability calculations.
- Make sure that the Net weight is entered under the General tab. The net weight is used for both IntrastatIntrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reporting and calculating transport emissions.

#### Add/check the Supplier link under the Purchase tab. Information from the active supplier is used to determine the emissions in the calculation. The Material type and Emissions entered under the supplier link are used as information in the purchase order suggestion.
- Subcontract parts
- Update the Net weight of the subcontract parts in the Subcontract parts procedure. The net weight is used to calculate transport emissions to and from the supplier. If the net weight isn’t entered in the Subcontract parts procedure, the net weight entered in the Part register is used in these calculations. The net weight is also used if you have selected weight as the basis for calculating emissions from the contract manufacturing.
- Supplier register

#### Make sure that the Transport distance is entered under the Settings tab. The transport distance is used when calculating transport emissions.
-   
Check the Delivery method and Delivery terms, see the Terms procedure above.

#### Work center register
- Here you can enter the emission values for work centers and subcontract work centers. These values are used for calculating production emissions and contract purchases in the sustainability calculations.
- Own work centers

#### Enter Power in kW for the machine (work center). The values you enter here are first multiplied with the emission factor for the electricity mix you have entered in Basic data – Sustainability and then with the production time entered in BOM and routing to calculate the CO2e emissions from electricity usage when producing the part.
Enter Other emissions using the unit kg CO2e/h. The values entered here are then multiplied with the production time entered in BOM and routing to work out other CO2e emissions from the production of the part.
Subcontract work centers
- Enter a factor in Other emissions using the unit kg CO2e and select a calculation basis that matches the subcontract work center. The following calculation bases can be chosen:
- Net weight – If you use net weight as calculation basis, you have to enter a net weight for the subcontract part in the Subcontract parts procedure. If net weight is missing for the subcontract part, the net weight entered in the Part register procedure will be used instead. The calculation will be performed as follows: Net weight x Other emissions.
- Operation price incl. setup – This is calculated according to: (Unit price + (Setup price/Calculated qty)) / Other emissions. This calculation means that you can get an emission factor based on the price for the purchased service, which is often the only information available.
- Operation price excl. setup – This is calculated as follows: Unit price x Other emissions.
- Each – The value for Other emissions will be used per item (each) without any conversion/recalculation.
-   
Sustainability list
Use the Sustainability list procedure to update multiple parts with the correct emission factor and CO2e value. The list also displays the annual volume for parts and calculates the annual CO2e emissions for each part. You can also use the list to find the parts that produce the most emissions yearly, so you know which parts to focus on reducing the emissions of as part of your sustainability work. The Calculated emissions column gives you information on which parts cause the most emissions.
- Sustainability calculation

#### Once you have entered all the above information, you can start the emissions calculation.
Select the desired parts and start the calculation. If any warnings are displayed, you need to enter the information that is missing. The warning will let you know which information is missing.
Save the calculation for the manufactured parts. Under the Sustainability tab in the Part register the manufactured parts are updated with the CO2e values and the calculations. Please note! When you click Save, it means the CO2e value for the part is saved. When you click Save calculation, the entire calculation will be saved instead.

#### Please note! For the emission calculation to be credible, it is important that the company’s total yearly emissions have been analyzed and are included in some part of the calculation.
Document settings
- In the Document settings procedure you are able to decide whether emission information should be shown on the documentation for quotes, order confirmations, invoices, and comprehensive invoices. By default, transport labels do not show sustainability information but you can choose to add emission information to your own transport labels.
- Save the calculation for the manufactured parts. Under the Sustainability tab in the Part register the manufactured parts are updated with the CO2e values and the calculations. Please note! When you click Save, it means the CO2e value for the part is saved. When you click Save calculation, the entire calculation will be saved instead.
> Please note! For the emission calculation to be credible, it is important that the company’s total yearly emissions have been analyzed and are included in some part of the calculation.

#### Document settings
In the Document settings procedure you are able to decide whether emission information should be shown on the documentation for quotes, order confirmations, invoices, and comprehensive invoices. By default, transport labels do not show sustainability information but you can choose to add emission information to your own transport labels.
