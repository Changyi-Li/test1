### Printouts

#### Printouts at Stop work
- Print transport label – Here you decide which transport labels should be printed by default when the operator stops a work item. There is ons transport label for rejections, one for transfer to stock (final operation), and one for in progress (all operations where there is no transfer to stock).

#### Printouts at Start
- Automatic printing of shop packet – With this setting you determine if the number of manufacturing order documents which you have entered and linked files you have selected in the table, should automatically be printed when the operator starts the work item or starts picking in Monitor Mobile.
Traveler and material document will be printed when the first operation of a part (order node) is started. Operation document will be printed once per started operation. However, the operator can manually print the documents at any time.
If the first operation is subcontract or a work center with automatic reporting of quantity, then the following operation is considered to be a start operation and when it is started the automatic printing will take place. If several operations in a row are subcontract or work centers with automatic reporting of quantity, then the automatic printing of documents will take place when the operator starts the first regular operation.
- Print transport label – With this setting you decide if transport labels should be printed. You can choose if transport label should be printed when a work item is started, or when picking in Monitor Mobile is started (Mobile picking).

#### Stop work
- Return tool when operation is interrupted – With this setting you decide if tools linked to an operation should be returned when you finish an operation in the Recording terminal even though then entire quantity is not reported.
