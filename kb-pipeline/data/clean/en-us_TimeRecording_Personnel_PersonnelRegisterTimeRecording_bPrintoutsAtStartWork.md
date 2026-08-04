### Printouts at Start work
In this box you find settings for the person in question regarding printouts which should be made when starting work in the recording terminal.

#### Print according to
The default option here is Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations.. This means that printing of transport labels and shop packets will take place according to the settings of the work center. If you select the option Employee you can override the work center's settings for the person in question.

#### Print transport label
With this checkbox you can select that a transport label for work in progress should be printed when the person starts a work item.

#### Print shop packet
By clicking the button Print shop packet you access a table where you can select the Number of copies which by default will be printed for each manufacturing order document. In the Files column you can decide if linked files also should be printed together with the shop packet (for example instructions, drawings). It is possible to link files to the main part, the part's revision, the operations in the BOM and routing, and the material in the BOM and routing.

#### Automatic printing of shop packet
With this setting you determine that the number of manufacturing order documents which you have entered, will be printed when the operator starts the work item. Traveler and material document will be printed when the first operation for a part is started. Operation document will be printed once per started operation. However, the operator can manually print the documents at any time.
If the first operation is subcontract or a work center with automatic reporting of quantity, then the following operation is considered to be a start operation and when it is started the automatic printing will take place. If several operations in a row are subcontract or work centers with automatic reporting of quantity, then the automatic printing of documents will take place when the operator starts the first regular operation.
