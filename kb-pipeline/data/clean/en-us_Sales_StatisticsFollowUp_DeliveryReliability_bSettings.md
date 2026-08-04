### Settings
Here you configure settings for calculating/measuring the delivery reliability.

#### Delivery date
In this field you select which delivery date to use when calculating/measuring delivery reliability: Planned, Initial, or Desired. The default option here is "Initial". (This applies to systems newer than version 24.1.)

#### Horizon
Applies to the Future delivery reliability list type. Here you enter how many days ahead (calendar days) of the order list should be analyzed for our expected future delivery reliability. The horizon also includes the lagging order rows (past time).

#### Calculate delivery reliability of
Applies to the Detailed and Total list types. With this setting you decide what will be used when calculating the delivery reliability; delivery rows or customer order rows.
- Delivery rows – This alternative means that each delivery is included in the calculation and in the detailed list. If a customer order row is partially delivered, e.g. in three deliveries, the system will compare the actual delivery date with the planned delivery date of all of these three deliveries. If one of the deliveries is in time and two are late, the delivery reliability will be 33%.
- Customer order rows – This alternative means that each customer order row is included only once in the calculation and in the detailed list. If the order row is delivered e.g. in three deliveries, of which one early, one in time, and one late, the order row is considered to be late. In other words, a negative interpretation will be made.
This setting can be combined with Include late, undelivered order rows (see below).

#### Calendar
Here you select National calendar or All calendar days. The dates in the selected calendar will be included in the calculation. In the national calendar, weekends and other holidays are not included. In the option All calendar days, weekends and holidays are included. If you plan, e.g., to deliver on Friday but deliver the following Monday instead, the delivery will be considered one day late using the National calendar. Using the option All calendar days, the delivery will instead be considered three days late.

#### Include stray customers
If you activate this setting, the delivery reliability will also be calculated in relation to customers registered as "Stray customers" in the customer register.

#### Include late, undelivered order rows
Applies to the Detailed and Total list types. With this setting you determine if undelivered or partially delivered rows with dates in past time, that are considered late, will be included in the list. If you have selected the option Delivery rows under the setting Calculate delivery reliability of, a fictitious delivery record for the rows that are late and not completely delivered will be added. If you have selected the Customer order rows option for that setting, the entire order row will be considered late.

#### Include late order rows
Applies to the Future delivery reliability list type. With this setting you decide order rows in past time should be included. These will then be considered late.

#### Use allowances, if any, on customer
With this setting you decide if allowances entered for the customer should be considered when calculating/measuring delivery reliability. For customers, you can enter exceptions from allowances. This applies both to deliveries made too early and made too late. If this setting is not activated, or if the customer does not have unique values for allowance, the delivery reliability will be calculated based on the values entered in the fields below.

#### Allowance before/Allowance after
Here you enter the number of days before and after the delivery date, which you allow the delivery to be sent and still consider it to be on time. Default values are loaded from the system settings Default allowance for own delivery reliability – Too early and Default allowance for own delivery reliability – Too late. Depending on what calendar you choose, this will be interpreted as work days or calendar days. For the Future delivery reliability list type you only enter days for allowance after the set delivery date.
