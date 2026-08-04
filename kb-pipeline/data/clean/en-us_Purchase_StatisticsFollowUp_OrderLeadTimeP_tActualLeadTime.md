### Actual lead time list
The list is loaded and displayed based on the selection and settings you have chosen. As in all lists in Monitor ERP, you can drag and drop in order to change the column to group by.
This list shows how the order row has been planned in relation to desired delivery date and the part’s lead time. The actual lead time, from print date to arrival date, is shown. The list shows how the supplier has delivered in relation to desired delivery date and the part’s lead time.

#### Desired lead time
The Desired lead time column is a calculated column that shows the difference between Desired delivery date and Print date.
Desired lead time = Desired delivery date – Print date

#### Actual lead time
The formula for calculating actual lead time is:
Actual lead time = Actual delivery date – Print date

#### Difference
The Difference column is a calculated column. It shows the difference between what we desired and the actual result. If the value is positive, delivery is later than desired. If the value is positive, delivery is earlier than desired.
Difference = Actual delivery date – Desired delivery date

#### Comparison
If the setting Part’s lead time is checked, the calculated column Comparison is shown. This column shows the comparison between the part's lead time and the actual lead time.
If the value is positive, the supplier has delivered later than the part’s lead time, meaning the supplier could have delivered earlier based on the part’s lead time.
If the value is negative, the supplier has delivered earlier than the part’s lead time, meaning the supplier was able to shorten the lead time and deliver really fast.
The formula for this column is:
Comparison = Actual lead time – Part’s lead time
