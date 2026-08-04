## Currencies
You use this procedure to:
- Register currencies.
- Update exchange rates (current and historic) per rate type.
- Manage rate types.
You select a currency for the company (called "company currency"), customers, suppliers, price lists, etc. in order to use it on orders and invoices as the currency that applies to the price of the parts and the currency that you use in the accounting.
The company currency is completely blocked for modifications regarding exchange rate, code, and factor, but you can modify the currency name.
You can also delete currencies. To delete a currency, it cannot be used in the system (that is, it cannot be selected for the company or entered in basic data, price lists, orders, invoices, etc.).
There is also a term in the system called Rate type. Rate types are registered under the Rate types tab. Rate types make it possible to link different exchange rates to one and the same currency.
When you install the system the following rate types are available from the start Current exchange rate and AFS rate. The first-mentioned is used for exchange rates that are updated continuously. The AFS rate is used for exchange rates that are set in connection with the year-end closing. This rate type is for example used if you want to load lists with orders and then use the same rate that applied during the latest year-end closing.
You set an exchange rate for each rate type. The exchange rates are updated manually or loaded electronically via Internet. The information is saved in a changelog when you update the exchange rate of a rate type. When you start up the program for the first time, all rate types have exchange rate 1,00.
> Exchange rates that are changed on a specific day will apply as of the beginning of the following day, that is, from midnight. That is why we recommend that you update tomorrow's exchange rates at the end of the day. Each day, the banks publish information about which rates will apply the following day. BUT this does not apply to day-to-day transactions such as registering purchase orders and reporting arrivals. If you modify an exchange rate NOW and create a purchase order straight away, it will be the new exchange rate that applies.
Day-to-day transactions
The transactions made in a foreign currency are recalculated into the company currency according to the current rate entered in the currency table in this procedure. The current rate is loaded from each rate type. You can, for example, have your purchase flow and your sales flow linked to different rate types.
If you work with updated exchange rates every day it is important that you go here to modify the rate before you register the transactions of the day. If you modify the exchange rate in the middle of the day you will get transactions valued at different rates within the same day. This is something you want to avoid.
Historical rates
Every time an exchange rate is modified, this is logged. The exchange rate change is logged in the general changelog in Monitor ERP, and it contains a time stamp for the rate change, who modified it, as well as the exchange rate before and after the change.
For invoicing and ledgers there are functions where you can load the exchange rate for a given day in the past (historical rate). When the system should load a historical rate for a specific date (a day already passed), the information is loaded from the changelog of the currency. The log record loaded by the system is the rate which applied at the start of the day for which you are loading the exchange rate.
Automatic loading of exchange rates
The Scheduling tab is available if the selected Currency for the company in the Company information procedure has support for automatic loading of exchange rates. Via a scheduling item you can automatically update the company's exchange rates by loading the exchange rates from the central bank in question. At present, the following are supported:
- Sveriges Riksbank
- Norges Bank
- Danmarks Nationalbank
- European Central Bank (if the company currency is Euro)
- Narodowy Bank Polski (the Central Bank of Poland)
- Central Bank of Malaysia
- Monetary Authority of Singapore.
> Please note! Your Monitor ERP server must have internet access via TCP port 443 and 80, in order for the automatic loading of exchange rates to work.
