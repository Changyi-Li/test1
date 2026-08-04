### FAQ – Stock count
What does the work flow for a stock count look like?
The flow chart below shows a recommended work flow during stock count in Monitor ERP.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/StockCount3.png)](../../../../Resources/Images/TrainingMaterial/StockCount3.png)
You can naturally do your stock count in many different ways. Each company has its own routines and procedures that are used for stock counts. You can say that there are two main types of taking stock: Continuous/Recurring and Full.

#### Continuous stock count
The recurring stock count is usually carried out according to a rolling schedule, where you stock count certain locations, part types, or departments at a time. During this stock count, the manufacturing and its corresponding stock transactions are still in progress.

#### Complete stock count
During a full/complete stock count, you usually do a stock count of the entire stock, at a time when the production is stopped for example on a weekend.
> Please note! You need to do some reconciliations prior to performing a complete stock count.
What needs to be reviewed prior to performing a complete stock count?
The following lists need to be reconciled prior to a complete stock count:
Order list – Purchase
This should be checked to see if all received goods have also been arrival reported. This should be combined with a verbal reconciliation with the staff at your goods receiving department.
Order list – Sales
Check this list to see that all delivered goods has also been delivery reported. This should be combined with a verbal reconciliation with the staff in your shipping department.
Order list – Manufacturing
Check this list to see that all the manufactured parts have been reported in the workshop. If an operation has been completed but not reported, then the material has not been deducted from stock. That will cause inaccuracies in the stock count. If reporting is done after the stock count, then the stock balance will again become incorrect.
Rule: Always report manufactured parts before taking stock, even if this means making several partial reports. Inform your staff/personnel. Print a reconciliation list for orders in progress (status 3).
Final reporting of order (manufacturing)
This should primarily be checked to control the warnings on finished manufacturing orders (status 4).
Stock value, negative balances
Check this in list of parts with negative balances. These parts have an obvious inaccuracy in the balance. These should be corrected before you begin the stock count. Create the list and filter by balances less than 0.
Why can I not include certain locations on the stock count basis in Stock count in list?
If you are not able to include a location, it is because the location is already included on another stock count basis (stock count number). You have to either close or remove the basis before you are able to create a new one. If you scroll to the right in the list, you will be able to see on which basis (stock count number) the locations are included.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_StockCount1.png)](../../../../Resources/Images/FAQ/FAQ_StockCount1.png)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_StockCount2.png)](../../../../Resources/Images/FAQ/FAQ_StockCount2.png)
Is there a list where I can check that all parts have been stock counted?
In the Stock value procedure you can choose to display Last stock count date, and you can then check whether the parts’ last stock count date is the same date as you stock counted them.
Why can I not see the last stock count date on the location that I moved the balance to?
Stock counts are performed per location, not on the part. This means that the latest stock count date is not brought across when you move the balance (the part) to another location.
Can I write a comment when I stock count?
Yes, in the Stock count in list procedure, in the list type Manage stock count, under the Reporting tab, you can enter comments ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) in the upper right as you report.
I cannot make a new stock count basis, why?
This may be because the parts/locations are already on a stock count basis. A part/location cannot be on two stock count bases at the same time. To solve this, you need to remove or report the existing stock count basis.
How do I see which parts have not been stock counted in the stock count basis?
In the stock count basis you are able to see the part’s status if it is stock counted, being stock counted, or not stock counted.
In the Stock count procedure I cannot find a column for stock count difference. Where can I see the stock count difference?
To see the stock count difference, go to the Stock count difference procedure. There you are able to select the parts that you want to see the stock count difference of.
Where can I change the arrival location in a list?
Use Part list list type Location settings. Make the list updatable so you can mark Arrival location on the locations that are arrival locations. The system setting Apply arrival location must be activated.
Which right is needed to be able to move stock balance?
It is the Report stock count right under Stock in the User procedure which gives access to move stock balance.
