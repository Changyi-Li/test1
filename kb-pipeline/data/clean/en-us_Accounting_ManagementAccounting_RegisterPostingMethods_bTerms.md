### Terms

#### Transaction type
The following transaction types can be selected, depending on for which log the posting method applies:
| Stock transaction log | Manufacturing order log | Calculation difference | Price change log | Invoicing log |
|---|---|---|---|---|
| Arrival – Purchase order | Processing | Calculation difference | Stock balance | Income |
| Material withdrawal – Manufacturing order | Subcontract |   | WIP balance | COGS |
| Transfer to stock to finished stock | Rejection * |   |   |   |
| Delivery – Customer order |   |   |   |   |
| Stock count |   |   |   |   |
| Direct stock reporting
(incl. withdrawal/returning of tools) |   |   |   |   |
| Move between warehouses |   |   |   |   |
| Cases |   |   |   |   |
| Arrival – Stock order |   |   |   |   |
| Delivery – Stock order |   |   |   |   |

#### Part type
Here you select which part types should be included in the posting method:
- Purchased
- Manufactured
- Fictitious
- Service (only for Invoicing log with transaction type Income.)

#### Control method M-part
With this term you decide if the posting method applies for Order oriented and/or Stock driven manufactured parts. This is used if you require different posting methods for Order oriented and Stock driven parts. Manufactured parts with "Physical" planning method are handled as Stock driven when posting of logs.

#### Part's basic type
Here you select which basic types should be included in the posting method:
- Part
- Consumption
- Reusable
- Tool list

#### Include packaging
With this setting you determine if packaging should be included in the posting method. This term is only available for purchased and manufactured parts.

#### Event type
With this setting you determine if the posting method results in a Stock increase or a Stock decrease.

#### Reverse posting on reversed event type
If you activate this setting it is sufficient to register one posting method for the transaction, regardless if it results in a stock increase or a stock decrease. The system then automatically reverses the posting depending on the positive/negative sign in the log.
However, if you want different posting depending on whether it is an increase or decrease, you should register these with separate posting methods and uncheck the setting Reverse posting on reversed event type.

#### Allow duplicates
Here you decide if duplicates should be allowed. In some cases you might need several posting methods with identical terms. This applies if the same transaction generates duplicate postings or even more. An example of this is if you want to post both standard price and SO mark-up upon arrival, but you want a separate posting for the SO mark-up.
