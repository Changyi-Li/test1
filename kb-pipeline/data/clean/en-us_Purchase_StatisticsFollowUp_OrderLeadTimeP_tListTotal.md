### The Total list
The list is loaded and displayed based on the selection and settings you have chosen. As in all lists in Monitor ERP, you can drag and drop in order to change the column to group by.
Grouped by supplier
If the list is grouped by supplier, it will show the amount of order rows that have been desired, confirmed (initial) and delivered (actual) before or after the part’s lead time. This is shown summarized per supplier.
In this list you can see:
- How many order rows the company has ordered to be delivered in fewer days than the part’s lead time.
- How many order rows the company has ordered to be delivered in equal to or more days than the part’s lead time.
- How many order rows have been confirmed by the supplier with equal to or fewer days than the part’s lead time.
- How many order rows have been confirmed by the supplier with a lead time that is longer than the part’s lead time.
- How many order rows have been delivered by the supplier within the part’s lead time.
- How many order rows have been delivered by the supplier with a lead time that is longer than the part’s lead time.
Grouped by part
If the list is grouped by part, the average lead times for order rows are compared to the part’s lead time. These lead times can be used to determine if the actual safety stock levels are sufficient.

#### Arrival reported order rows
The calculated column Arrival reported order rows shows the amount of fully or partially (depending on the selection row for Purchase order row – Status) arrival reported order rows.

#### Desired< Part’s (Lead time)
The column Desired < Part’s (Lead time Number of days between ordering date and delivery date. Normally used for purchased parts.) calculates order rows where Desired lead time < Part’s lead time. These are the amount of order rows where the part's lead time has not been taken into account.
Desired lead time = Desired delivery date – Print date

#### Desired => Part’s (Lead time)
The column Desired => Part’s (Lead time) calculates order rows where Desired lead time => Part’s (Lead time). These are the amount of order rows where we have successfully been able to take the part’s lead time into consideration.
Desired = Desired delivery date – Print date

#### Initial <= Part’s (Lead time)
The column Initial <= Part’s (Lead time) calculates order rows where Initial lead time <= Part’s lead time.
Initial lead time = Initial delivery date – Print date

#### Initial > Part’s (Lead time)
The column Initial > Part’s (Lead time) calculates order rows where Initial lead time > Part’s (Lead time).
Initial = Initial delivery date – Print date

#### Actual <= Part’s (Lead time)
The column Actual <= Part’s (Lead time) calculates order rows where Actual lead time <= Part’s lead time. These are the order rows where the supplier has delivered faster than or equal to the part’s lead time.
Actual = Actual delivery date – Print date

#### Actual > Part’s (Lead time)
The column Actual > Part’s (Lead time) calculates order rows where Actual lead time > Part’s (Lead time). These are the order rows where the supplier has delivered later than the part’s lead time.
Actual = Actual delivery date – Print date
