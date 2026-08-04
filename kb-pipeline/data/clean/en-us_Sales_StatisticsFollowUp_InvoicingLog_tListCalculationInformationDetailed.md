### Calculation information – Detailed
This list shows detailed information about calculation costs and a comparison of these against the invoiced value and CM The contribution margin (CM) is the difference between the standard price and the sales price.. Below, you can read about how the invoiced value, calculation costs, and CM are calculated. All values are always shown in the company currency.
The following applies for manufactured parts if the FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price alternative is used:
If the invoiced row originates from multiple different manufacturing orders (multiple post-calculations), the rows will be divided by unique manufacturing order. Meaning, if 10 parts originates from 3 different orders you will see 3 rows with the calculation information according to its unique saved calculations.
If there is a saved FIFO calculation, the calculation registered for the part's standard price will be used. This means that even if there is a standard price used when good are sold, it will be presented in Material, SO, Subcontract, and SC, etc.

#### Sales
Here you see the invoiced value, that is, price each × quantity (taking discounts and setup prices into consideration, if any).

#### Material
The material cost is partly loaded based on which row type is concerned and also based on which calculation alternative was selected under the Selection tab. The calculation alternatives affect the material cost in the following way:
- Current standard price calculation – With this option, the material cost will primarily be loaded from the current standard price calculation. Secondarily, if there is no standard price calculation, the part's current standard price will be loaded (e.g. for services or parts without calculations). For invoice rows of row type 2 there is always a zero in this column since they neither have calculations nor standard prices.
- Standard price calculation at delivery or Standard price calculation at invoicing – If one of these alternatives is selected, the material cost will primarily be loaded from the calculation at the delivery date or invoice date. Secondarily, if there is no calculation at that date, the part's or service's standard price at the same date will be loaded. For invoice rows of row type 2 there is always a zero in this column.
- Post-calculated mean price – With this alternative the material cost will be loaded from the standard price calculations for M-parts and F-parts. If there is no calculation, you will see a zero (0). For P-parts and services, the current standard price is always loaded.
- Future standard price – Using this alternative, the material cost will primarily be loaded from the standard price calculations. If there is no calculation, the part's or service's future standard price is loaded. For invoice rows of row type 2 there is always a zero in this column.

#### SO
The SO (storage overhead mark-up) is always loaded from the selected calculation. If there is no calculation, you will see a zero. For P-parts you will see SO in this column if you have chosen to include SO for P-parts under the Selection tab.

#### Subcontract/SC/Processing
The subcontracting cost, the subcontract cost mark-up, and the processing cost, are loaded from the calculation that you have selected. If there is no calculation, you will see a zero.

#### Manufacturing cost
In this column you can see the manufacturing cost which is the total of Material, SO, Subcontract, SC, and Processing.

#### CM
Here you see the contribution margin. It is the sales minus manufacturing cost.
The standard price at the time of invoicing is the price that will be used in the invoicing log when calculating CM/CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. and the price alternative called FIFO price is used as well as the part not being stock updated.

#### Cost factor 1-3
These columns display a breakdown of the processing cost per cost factor. Which cost factors should be included in the processing cost is selected under the Settings heading under the Selection tab.
