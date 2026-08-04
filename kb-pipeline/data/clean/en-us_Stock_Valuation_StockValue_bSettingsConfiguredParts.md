### Settings – Configured parts

#### Balance alternative
Here you select the balance, at different times, on the parts' locations, on which the stock value will be based. Explanation of the different alternatives:
- Current balanceCurrent balance is the part balance at this moment on the locations. – If you select this option, the balance at this very time will be loaded.
- Last stock count date – With this option, the balance at the time of the last stock count date will be loaded. The parts might have been stock counted on different dates, so the date from which the balance origins may differ from part to part.
- Optional stock count date – With this option, the balance used for valuation is the balance at the selected stock count date. Only the parts and locations which were stock counted on the selected date will be included in the list. A date must be selected in the date field.
- Historical balance (log date) – With this alternative the balance from the selected log date will be loaded. The log date in the stock transaction log is the date on which a log record is created. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.
- Historical balance (actual date) – With this option the balance from the selected date will be loaded. The actual date in the stock transaction log is the date entered during reporting. E.g. at arrival reporting, the date on which the delivery arrived is entered as delivery date and not the date at which the arrival reporting is made. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.

#### Show
With this setting you determine which dates to be displayed for the parts in the list. The following options are available: price date, last consumption date, last arrival date, and last stock count date. Price date is shown for the selected price alternative in the list.

#### Minimum value
Here you enter an amount limit of a part's minimum stock value in the company currency for the selected balance alternative. If the field is empty, the list will include individual rows for all parts that have been selected, regardless of how low a stock value each of the parts has. If you e.g. enter 100 as minimum value, all the minor positive amounts up to and including 99 and all the minor negative amounts down to and including -99 will be shown as a total under the headings "Total of small positive amounts" and "Total of small negative amounts". The small amounts are added to/subtracted from the total stock value. The purpose of the minimum value is to create a shorter list that does not display small amounts.

#### Also include parts without balance
With this checkbox you determine if parts with a zero balance for the selected balance alternative will be also included in the list.

#### Show calculation information
With this setting you determine if calculation information for the configured parts should be shown in the list. If you activate this setting, you will see cost of Material, SO, Subcontract, and Processing. This is loaded from the pre-calculation.
