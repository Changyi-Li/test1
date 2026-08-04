### Direct stock reporting
The Direct stock reporting tab will be activated if the system setting Use cause/posting in the procedure Direct stock reporting has been set to Cause and posting.
In the matrix you register posting settings for direct (unplanned) stock withdrawals. To each product group and cause coordinate in the matrix there is an account string containing cost account and posting dimensions, to which you select accounts.
When posting direct arrival, the cost and stock will be recorded automatically on the opposite side of the arrival/withdrawal in question.

#### Product group
Here you see all registered product groups on separate rows in the table. There are several account types for each product group according to the below, for which you configure posting against each cause:
- Cost – on this row you configure the account string for cost of direct stock withdrawal.
- Stock – On this row you configure the account string for stock.

#### Cause
Here you see all registered causes on separate columns in the table. Causes for direct stock reporting are registered in the Cause codes procedure. You will see Account for each cause and the dimensions in the account string registered in the Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure. When you start up the system for the first time, the following dimensions are available: CC (cost center), CU (cost unit), and Project. If an account does not manage postings of a certain dimension, the field is grayed out. If a dimension is mandatory, you will see information about this in the field. However, under this tab you can leave the field empty.
For certain dimensions you cannot enter a code, because it can be a dimension that is linked to a register which is posted automatically, for example, part, product group, etc. This link is created in the Dimensions procedure.
