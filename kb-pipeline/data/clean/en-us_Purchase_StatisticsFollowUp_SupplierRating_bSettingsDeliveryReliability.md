### Settings – Delivery reliability
The following settings are available for the list types for delivery reliability.

#### Delivery date
Here you select which delivery date that the delivery reliability should be measured against. The available alternatives are: planned, initial, desired, and requested (the last alternative is only available for the list types Delivery reliability of subcontract). The default option here is "Initial". (This applies to systems newer than version 24.1.)
Planned, initial, and desired delivery date all exist on the purchase order row. Requested delivery date exists in the manufacturing order log and is set when the subcontract is reported as shipped. If no requested date exists, the planned date (which always exists) will be used instead.
Example 1: Requested delivery date
You have shipped 10 pcs with a requested delivery date on 2014-12-15 (December 15, 2014). On 2014-12-16, you then arrival reported 10 pcs. The requested delivery date will then be compared with the actual delivery date. The result will show that the arrival was one day late.
Example 2: Requested delivery date
You have shipped 10 pcs with a requested delivery date on 2014-12-15 and 10 pcs with a requested delivery date on 2014-12-22. On 2014-12-19, you then arrival reported 15 pcs. If you measure on arrival rows, the detailed list will include two log records. The first 10 pcs are shown as four days late and the other 5 pcs are show as 2 days early (work days). If you then ship another 10 pcs and later on arrival report all the remaining 15 pcs, the arrival will be measured against the second and the third shipment. That is, the measuring will always be made based on a chronological and quantitative matching. The matching will always be made for all shipments and arrivals, even if you made a selection so that you only get the last delivery as result.

#### Calculate delivery reliability of
With this setting you determine what on what to calculate the delivery reliability:
- Arrival rows(default) – This alternative means that if you make a partial delivery of a purchase order row/operation e.g. three times, the actual delivery day of the three arrivals will be compared with the planned delivery day. If one of the arrivals is on time and two are late, the delivery reliability will be 33%.
- Purchase order rows – This alternative means that each order row/operation is included only once in the calculation and in the detailed list. If the purchase order row is delivered e.g. in three partial deliveries, of which one early, one on time, and one late, the order row is considered to be late. In other words, a negative interpretation of all the arrivals will be made, where the late arrivals carry the most weight.
This setting can be combined with the setting Include late, undelivered order rows below. If you have selected Arrival rows, a fictitious arrival record will be added for the rows that are late but not completely delivered. If you have selected Purchase order rows, the entire order row will be considered as late.

#### Calendar
The dates in the selected calendar will be included in the calculation. Using the National calendar, weekends and holidays are not included, but in the calendar All calendar days they are included. E.g. if you plan to arrival report on a Friday, but arrival report the following Monday instead, the delivery will be considered one day late using the National calendar, but it will be three days late if All calendar days are used.

#### Include stray supplier
Suppliers marked as “stray suppliers” in the supplier register are included in the calculations by default, but they can be deselected by unchecking this setting. You may not always be interested in measuring the delivery liability of stray suppliers.

#### Include late, undelivered order rows
With this checkbox you determine if undelivered order rows, where the delivery date has already passed, also should be included in the calculation. A passed date refers to when the delivery date of the order row is yesterday or earlier than that. Which delivery date that is concerned is determined by the setting Delivery date above.
The remaining quantity on the order row is displayed as a separate row in the list, in case it is undelivered and late. That row also does not show any actual delivery date or difference. It is possible that you have arrival reported some quantity of the order row already, and that this quantity is already included in the calculation. If you have an order row that is partially delivered and the rest of the order row is undelivered, this means you will see it as two rows in the list, and it will also be calculated as two rows in total lists.

#### Use allowances, if any, on supplier
If you have activated this setting, the values entered for the supplier in the supplier register will be used in the fields Allowance too early and Allowance too late (in work days). These are used as exceptions from Allowance before and Allowance after that can be configured here in the supplier rating. The setting is activated by default. If you uncheck the setting, the calculation will only be based on the values in the fields below.

#### Allowance before/Allowance after
Here you enter how many calendar days (not work days) you allow before and after, to still consider the delivery to be on time. Default values are loaded from two system settings Default allowance for delivery reliability – Too early and Default allowance for delivery reliability – Too late.
