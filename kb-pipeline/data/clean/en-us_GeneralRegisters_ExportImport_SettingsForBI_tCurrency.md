### Currency
Under this tab you enter the company currency for each company as well as the exchange rate in relation to the main company's* currency. Amounts in different currencies from different companies must be converted into a common company currency regarding BI data.
> * The main company is the company where you create a scheduled data mining. Normally, this is the company with database number 001.1.
In the upper table you see all companies in the system as well as the external companies registered under the External companies tab.
In the bottom table you add the exchange rates to be used for each marked company in the upper table. You enter from and to which date the exchange rate will apply and you also enter the exchange rate in relation to the main company's company currency. On each row you enter from which date the exchange rate should start to apply. The exchange rate with the latest date applies until further notice.

#### Currency
In the Currency column you enter a code for each company's currency, for example, t.ex. SEK, EUR, USD.

#### From
In the From column you select from which date the exchange rate should apply.

#### Exchange rate in relation to company currency
In this column you enter which exchange rate that applies (conversion factor) in relation to the the main company's currency. Please see the example below. The exchange rate can have a maximum of 6 decimals.
Examples
- The main company uses the company currency SEK and the selected company uses the company currency GBP. The GBP currency was 0.084 at the start date in relation to 1 SEK. You should then enter the conversion factor 1/0.084 in the field. When you leave the field, the factor becomes calculated and is displayed with a maximum of 6 decimals. In the example this results in 11.904762.
- The main company uses the company currency EUR and the selected company uses the company currency USD. The USD currency was 1.162 at the start date in relation to 1 EUR. You should then enter the conversion factor 1/1.162 in the field. When you leave the field, the factor becomes calculated and is displayed with a maximum of 6 decimals. In the example this results in 0.860585.
