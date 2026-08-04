### Periods
In this box you see all accounting periods for the.accounting year you have selected. There are three function buttons with different functions:
- With the function button Change period ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_set_active.png) you move the current period ahead, one period at a time. It is not possible to move the current period ahead more than to the last period of the accounting year.
- With the function button Undo change of period ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_cancel.png) you move the current period back in time, one period at a time. It is not possible to go back to a locked period.
- Using the function button Change year ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calendar_next.png) you will change to the next accounting year. This button is only available if the current period is the last period in the accounting year. You then first receive a control question asking if you want to change accounting year. If the next accounting year is already registered in the Register accounting year procedure, you can see the name and the date of the next accounting year. If the next accounting year is not registered, then this will be created and you get to enter a name for this new accounting year.
> When you change year, the transactions of the past year are transferred to an AFS. This enables you to, parallel to the current accounting for the new year, make transactions that only concern the annual financial statement, AFS. Thus, the annual financial statement is a copy of the accounting of the last year. When changing year, the closing balances (CB) of the last year are also transferred as opening balance (OB) for the new year. While working with the annual financial statement you can continuously update opening balance for the new year by using the button Load OB from previous year's CB in the Opening balance procedure.

#### Current period
An arrow is shown on the row of the current accounting period.

#### Period
In this column you see the number of the period.

#### From date/To date
In these columns you see from which date and to which date the period applies.

#### Status
In this column you select if the period on the row should be open, closed, or locked.
- Open – If you select Open it is allowed to record in the accounting period. In an open period it is possible to determine if specific voucher number series should be locked and not possible to access for recording. For example, the month is open but only manual recording should be allowed. Then you should lock all series except for the manual series.
- Closed – If you select this option it is not allowed to record/book in the period in question, but it is possible to open the period. When the period is closed (or locked) it means that all voucher number series are locked and not possible to access for recording.
- Locked – If you select this option it is not allowed to record/book in the period in question, and it is also not possible to open the period. To lock a period you must do it in chronological order starting with the first period and then you lock the next, and so on. It is not possible to lock the current period. If a period has warnings it is not possible to lock it.

#### Warnings exists
If the period is closed and there are things left to do in the period, you will in this column see a button with a warning symbol. By clicking the button you can then see what needs to be done, and it is also possible to go to the affected procedures procedures from there. What is checked and can cause warnings is:
- There are accruals left to release.
- There are preliminary vouchers left to record.
- The VAT report has not been recorded.
- There are automatic posting left to release.
- Scheduled depreciations have not been recorded.
- There are journals left to record/book (check per journal type). For example customer invoice journals or fixed assets journal.

#### Locked voucher number series
If the period is open you can use the button Locked voucher number series ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to see and lock specific voucher number series for recording/booking. If the user marks the Locked checkbox for a voucher number series, you will here see the user name of the person who locked the series as well as the date and time when this was done. The button Locked voucher number series shows a symbol with a padlock ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) if there already are locked series in the period. It is always possible to remove the lock for a series.
Locking of voucher number series in open periods is useful for example when you have reconciled accounts payable/accounts receivable and want to prevent new bookings there, but still want to be able to record/book manual vouchers.
