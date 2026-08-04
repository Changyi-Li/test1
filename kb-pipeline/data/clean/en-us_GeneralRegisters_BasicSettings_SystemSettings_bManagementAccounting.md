### Management accounting

#### Posting of direct stock reporting via
Here you determine if posting of direct stock reporting should be made via posting method or via the posting that was entered at the time of the reporting in the Direct stock reporting procedure.
If you select Posting matrix, the posting entered at the time of the reporting will be loaded. For this to take place, it is required that the Use cause/posting in the Direct stock reporting procedure system setting, found under the Stock tab, has been set to Cause and posting. When the setting above has been configured, you enter the default posting for these in the Posting matrix procedure, under the Direct stock reporting tab. Posting made via posting method is entered in the Register posting method procedure. Regardless of how the system setting has been configured, the posting will always be transferred to the stock transaction journal in the accounting.

#### Post records without values
This system setting determines if also records with zero in value should be posted and be displayed in the journals. This can for example occur if you report a part with zero in standard price.

#### Calculation for stock transaction
If calculation parts of standard price are set to be posted in the field called Price alternative for manufactured part (for example material cost, processing cost) in the Register posting method procedure, the value that is being posted is loaded from the calculation register for the part. In this system setting you can choose if the value should be loaded from current calculation or current calculation at time of reporting.
This system setting also applies to purchased parts when you save standard prices from a calculation.

#### Handle product group as numeric field during posting of logs
Here you determine how the field product group should be handled under Other terms in the Register posting method procedure. Product group is by default handled as an alphanumerical field, but here you can determine that is should be handled as a numerical field instead. This system setting is significant if for example the term is product group 1 up to 9. When the field is alphanumerical, the posting method finds all product groups that stat with 1, 2, 3, etc. up to 9. In other words, also 10 or 100. When the field is numerical, the posting method only finds product groups within the digit interval 1 to 9 (not 10 or 100 for example).
