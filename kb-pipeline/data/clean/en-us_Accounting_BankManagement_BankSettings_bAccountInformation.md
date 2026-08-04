### Account information

#### Type
Here you select bank account type. You can make the following selections:
- IBAN (International Bank Account Number) – is an international standard for account numbers that is used during payments to and from foreign countries. IBAN consists of country code, control digits, bank code, and complete account number.
- BBAN (Basic Bank Account Number) – is a national account number. The length of this account number varies depending on which country it is. There is no common international standard unifying the BBAN. Instead every country has its own specific number.
- UPIC (Universal Payment Identification Code) – is a universal account identifier issued by financial institutions. It is used by companies and organizations that need to receive electronic payments without having to reveal confidential bank information, for example account number.
- Other – accounts that do not correspond to any of the account types above.
The lead text for the bank account type (IBAN/BBAN, etc.) is shown in a dynamic field in the footer of all external documents depending of the bank account type.
> E-invoice export (the PEPPOL format): This applies generally when exporting e-invoice. If the bank account information is missing SWIFT/BIC at the company issuing the e-invoice, an "empty" tag for this will no longer be exported in the file.

#### Currency
Here you select currency for the bank account. You can select among the currencies registered in the Currencies procedure.

#### Account number/IBAN
Here you enter bank account number or IBAN number. A check is made in the field to ensure that the entered IBAN number is valid.

#### SWIFT/BIC
The bank's SWIFT or BIC (Business Identifier Code) is the bank's identification code used during international payments. 8 or 11 characters are used in the code, and the first 6 characters are always letters.

#### Sender account BBAN
This field is available if you have installed the plugin for Swedbank ISO payments. Here you enter a sender account (BBAN), using a maximum of 15 characters.
> You must make sure that correct information is entered since no validation is made of the entered sender account BBAN.
