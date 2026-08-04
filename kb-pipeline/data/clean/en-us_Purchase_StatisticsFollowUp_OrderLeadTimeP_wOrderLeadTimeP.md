## Order Lead Time – Purchase
The purpose of this procedure is to measure the lead time for various stages of purchase orders. All statistics are based on information in the supplier register, the purchase order register, and the arrival log. The lists cannot be updated.
- How long does it take from registering a purchase order to it being sent to the supplier?
- How long does it take for the supplier to confirm the purchase order?
- What is the desired lead time? Meaning, how many days does your company give the supplier to deliver and is this sufficient in relation to the part’s lead time?
- What is the initial lead time? Does the supplier take the order’s lead time into consideration when confirming the order?
This information can be useful when you are deciding the level of your safety stock for parts, taking the supplier’s upholding of lead times into consideration. One reason to use safety stock is the uncertainty in lead time.
This is also useful as a complement when measuring delivery reliability. If the follow-up of lead time shows that the order is made with shorter lead time than agreed, this can be one reason for the supplier's low delivery reliability.
> Consider that the system setting Question when changing delivery date, applies to frozen initial/desired affects the calculations.
List types

#### Lead time to printing
This list shows how many days have passed between purchase order registration and the order being sent to the supplier.

#### Confirmation lead time
This list shows how many days it takes for the supplier to confirm the purchase order. The print date is compared to the confirmation date.

#### Desired lead time
This list shows desired lead time, from print date to desired delivery date. The list also shows whether the supplier is given a realistic chance, meaning that there is enough time to achieve the desired delivery date considering the part's lead time. This list shows your company’s performance. How many days does your company give the supplier to deliver and is this sufficient in relation to the part’s lead time?

#### Initial lead time
This list shows the initial lead time, from print date to initial delivery date. The list also shows the initial lead time in relation to the lead times of the parts. If the supplier promised to deliver within the part’s lead time, this can be a reason for poor delivery reliability. If the supplier promises to deliver after the part’s lead time, the part’s lead time may need to be adjusted. This list lets you analyze the supplier’s performance.
If the setting Part’s lead time is checked, the initial lead time is compared to the part’s lead time.

#### Planned lead time
This list shows how the order row has been planned in relation to desired delivery date and the part’s lead time.
If the setting Part’s lead time is checked, it is also possible to analyze how the order row has been planned in relation to the part’s lead time.

#### Actual lead time
This list shows how the order row has been planned in relation to desired delivery date and the part’s lead time. The actual lead time, from print date to arrival date, is shown. The list shows how the supplier has delivered in relation to desired delivery date and the part’s lead time.
Only order rows that have been partially arrival reported or fully arrival reported will be included in the list.

#### Total
If the list is grouped by supplier, it will show the amount of order rows that have been desired, confirmed (initial) and delivered (actual) before or after the part’s lead time. This is shown summarized per supplier.
If the list is grouped by part, the average lead times for order rows are compared to the part’s lead time. These lead times can be used to determine if the actual safety stock levels are sufficient.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
