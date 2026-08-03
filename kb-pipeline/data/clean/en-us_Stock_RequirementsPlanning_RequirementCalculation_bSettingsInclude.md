### Include – Settings

#### Existing suggestions/orders
With this setting you determine if forecasts, suggestions, different types of orders, material requirement, quotes, should be included in the requirement calculation.

#### Type of shortage
Here you select which type of shortage the part should have in order to be included in the list. Explanation of the options:
- Include parts without shortage – When using this option, all selected parts will be included in the list regardless of the disposable balance.
- Below safety stock – With this option, the part will be included when there is a shortage in stock since the part's balance falls below the safety stock.
- Below reorder point – With this option, the part will be included when there is a shortage because the disposable balance falls below the reorder point.
- Definite shortage (<0) – With this option, all selected parts where the disposable balance is negative in the planning window within the selected date interval (regardless of safety stock or reorder point) will be included.

#### Include parts without reservations
With this setting you determine if parts with no requirement should also be included in the list. If this setting is not activated, a part with for example 0 (zero) as stock balance will not be included even if the safety stock is 5. If there is no reservation for the part, there is by definition no shortage.

#### Shortage without suggestion
With this setting you determine if parts that have a shortage but no registered suggestions, should be included in the list. You can also choose to only show these parts.

#### Include parts without suggestions
Here you determine if parts without suggestions or shortages also should be included.

#### Order suggestion
This setting determines the types of order suggestions that will be included in the list. Parts with shortages according to the definition for Type of shortage will be included in the list even though you have selected not to show order suggestions.
