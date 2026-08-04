### List type Initial lead time
The list is loaded and displayed based on the selection and settings you have chosen. As in all lists in Monitor ERP, you can drag and drop in order to change the column to group by.
This list shows the initial lead time, from print date to initial delivery date. The list also shows the initial lead time in relation to the lead times of the parts. If the supplier promised to deliver within the part’s lead time, this can be a reason for poor delivery reliability. If the supplier promises to deliver after the part’s lead time, the part’s lead time may need to be adjusted. This list lets you analyze the supplier’s performance.

#### Desired lead time
The Desired lead time column is a calculated column that shows the difference between Desired delivery date and Print date.
Desired lead time = Desired delivery date – Print date

#### Initial lead time
The Initial lead time column is a calculated column that shows the difference between Initial delivery date and Print date.
Initial lead time = Initial delivery date – Print date

#### Difference
The Difference column shows the difference between what you want and what the supplier wants. If the value is positive, the supplier needs more days than you desire. If the value is negative, the supplier needs fewer days than you desire.
Difference = Initial delivery date – Desired delivery date

#### Comparison
If the setting Part’s lead time is checked, the calculated column Comparison is shown. This column shows the comparison between the part's lead time and the initial lead time. If the value is positive, the supplier has confirmed an initial date that is further away in time than the part’s lead time allows. If the value is negative, the supplier has confirmed an initial date that is within the part’s lead time.
Comparison = Initial lead time – Part’s lead time
