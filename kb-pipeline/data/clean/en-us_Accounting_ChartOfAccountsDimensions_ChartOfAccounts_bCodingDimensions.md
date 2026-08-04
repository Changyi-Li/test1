### Dimensions
Here you can select which dimensions should be possible to use for the account. Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. must first be created in the Dimensions procedure.

#### Applied
In this column you decide which dimensions which should be possible to apply on the account or if it should be mandatory to apply the dimension.

#### Cost/Income type
The dimension's cost/income type (for the project accounting). The types of costs and income are those which in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure has been configured to load result from the bookkeeping. This field is available if you in the field above have chosen to apply the dimension on the account and the dimension in its turn is linked to project in the Dimensions procedure.
If this field is active you are required to select a type of cost/income. This is determined with the system setting Mandatory to enter project cost type in chart of accounts. If that system setting is not activated you are not required to select type of cost/income here, but you will receive a warning letting you know the transactions will not be included in the project.
With the system setting called Cost/Income in project is retrieved from you decide from which accounting year the chart of accounts setting regarding link to C/I type should be loaded.

#### Cost/Income
If the selected type of cost/income can be both a cost and an income (configured in the Basic data – Project procedure) then you can in this column choose if the dimension is a cost or income in the project accounting. If this is not the case, the field will instead show if the type of cost/income refers to a cost or an income.

#### Warehouse
This applies if the Warehouse option is installed. This setting means the program will automatically post on the cost center linked to the warehouse, in connection with this account being used when posting order rows. Please note! Warehouse must be selected for the dimension code in the Dimensions procedure, otherwise you will not be able to select warehouse. This automation will takes place provided that cost center had not already been entered for the part's product group in the Posting matrix procedure.
