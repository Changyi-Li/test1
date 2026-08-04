### The Write-up of costs list
This list type is used to write up the material cost for projects. The price is calculated as per the settings under the Selection tab.
Example of when a write-up of material costs can be useful: 
A purchase order contains 100 pcs of Part A which has been purchased on Project P1.

The standard price is 10 SEK for part A.

As per the manufacturing order that is linked to the project, only 80 pcs of part A are used. The remaining 20 pcs can be used in another order/project.

The remaining 20 pcs are used as per the manufacturing order on project P2. As the purchase is not recorded on project P2, no material cost is loaded in the project.

To get the correct material cost in project P2, the price is written up to move 20 pcs of part A to P2. By using the Write-up of costs list type, material cost is calculated with the price alternative Standard price. When the calculation is saved, a voucher is created in the journal with project P2 on the debit side and no project on the credit side. When the journal is approved in the Print material cost calculation journal procedure, the voucher becomes visible in the project and the material cost for part A increases from 0 SEK to 200 SEK (quantity x standard price).
