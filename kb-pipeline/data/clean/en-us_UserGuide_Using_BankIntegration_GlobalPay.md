### Global Pay
The Global Pay function is used to make international payments. You connect your account (in your local currency) to a function that makes payments in foreign currency via our partner Open Payments. When you make a payment it is converted to a foreign currency, just as with your regular bank, but with the help of a function that can make it a little cheaper. There are several benefits of this:
- Often lower conversion rates and transaction fees than your regular bank.
- Quicker payments, payment either the same day or the next day at the latest.
- Full control over which exchange rate and transaction fee in real time before you make any payment.
- You can transfer both domestically and internationally via the same payment flow (excluding payments from currency accounts).
- Payments to most countries/currencies.
- The service is free.
> You can schedule an invoice payment for up to 30 days in advance. You can read more [here](BankIntegration.htm#Utlandsbetalningar).

#### Payment flow
They payment is done in two stages when you pay via Global Pay:
1.   
The payment first goes into a client account with Open Payments. Therefore you cannot see the recipient’s (the supplier’s) bank account and payment reference in your bank’s payment information. It is Open Payment which is shown as the receiving account with the payment reference “OPESEXXXX” As you’re paying in the local currency and Open Payments manages all currency exchange, the payment will show in the local currency with your bank.
2.   
Open Payments exchanges the currency and sends the payment to the recipient’s (your supplier’s) bank account. The recipient receives the correct currency amount and the correct payment reference (invoice number) will show up on their bank statement.
Example of a company in Finland using Global Pay:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/BankIntegration_GlobalPay_Flow2.png)](../../../../Resources/Images/TrainingMaterial/BankIntegration_GlobalPay_Flow2.png)
> When confirming payments made via Global Pay, an accounting record is automatically attached when the records are loaded from the bank. This accounting record shows more information about the payment (Proof of payment information). This document is automatically saved as a PDF to the voucher which is created during the confirmation reporting. This is a record of Open Payments paying your supplier and can be provided as proof of payment should you need to provide proof that the payment has been made. Read more about payment confirmation [here](BankIntegration.htm#Återrapportering).

#### Supplier settings when paying via Global Pay
> International payments via Global Pay require certain details from the recipient such as address and bank account information. This is especially the case outside of the Single Euro Payments Area (SEPA).
-   
Within the SEPA, only IBAN and BIC are required.
-     
Outside of the SEPA there are different requirements depending on the recipient’s country:
| Country | Country code | IBAN/BBAN | Length | Bank code/Routing no. | Length | Clearing | Length | Street | City | Zip code | State |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Argentina | AR | BBAN | 22 | * |   |   |   | * | * | * |   |
| Australia | AU | BBAN | 20 | Bank code | 6 |   |   | Required | Required | Required | Required |
| Bangladesh | BD | BBAN | 13 | * |   |   |   | * | * | * |   |
| Brazil | BR | IBAN | 29 |   |   | Branch code | 7 | * | * | * |   |
| Canada | CA | BBAN | 12 | Bank code | 3 | Branch code | 5 | Required | Required | Required | Required |
| China (CNY) | CN | BBAN |   | Bank code |   | Cnaps |   | Required | Required | Required | * |
| China (USD) | CN | BBAN |   | Cnaps |   |   |   | Required | Required | Required | * |
| Egypt | EG | IBAN | 29 |   |   |   |   | * | * | * |   |
| Ethiopia | ET | BBAN | 5–35 |   |   |   |   | Required | Required | Required |   |
| Ghana | GH | BBAN | 8–20 | Bank code | 6 |   |   | Required | Required | Required |   |
| Hong Kong | HK | BBAN | 9 | Bank code | 3 | Clearing no. |   | * | * | * |   |
| India | IN | BBAN | 11 | Bank code | 11 |   |   | * | * | * |   |
| Indonesia | ID | BBAN | 35 | Bank code | 3 | Branch code | 4 | Required | Required |   |   |
| Israel | IL | IBAN | 23 | Bank code | 5 |   |   | * | * | * |   |
| Kenya | KE | BBAN |   | * |   |   |   | Required | Required | Required |   |
| Korea | KR | BBAN | 11–16 | * |   |   |   | * | * | * |   |
| Malaysia | MY | BBAN | 20 | * |   |   |   | * | * | * |   |
| Mexico | MX | BBAN | 18 | * |   |   |   | * | * | * |   |
| Morocco | MA | BBAN | 24 | * |   |   |   | * | * | * |   |
| Nigeria | NG | BBAN |   | * |   |   |   | Required | Required | Required |   |
| Philippines | PH | BBAN | 13 | * |   |   |   | * | * | * |   |
| Qatar | QA | BBAN | 35 | * | 9 |   |   | Required | Required | Required |   |
| Taiwan | TW | BBAN | 34 | * | 7 |   |   | Required | Required | Required |   |
| Tanzania | TZ | BBAN | 5–35 | * |   |   |   | Required | Required | Required |   |
| Türkiye | TR | IBAN | 26 | * |   |   |   | * | * | * |   |
| Ukraine | UA | BBAN |   | * |   |   |   | * | * | * |   |
| USA | US | BBAN |   | Routing no. | 9 |   |   | Required | Required | Required | Required |
| Vietnam | VN | BBAN | 30 | * |   |   |   | Required | * | * |   |
*Requirement not confirmed
> Read more about international payments via Global Pay [here](BankIntegration.htm#Utlandsbetalningar).
