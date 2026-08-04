### FAQ – Changing the year
How do I change the year?
Follow this instruction to change accounting year:
1.   
Open the procedure called Change period/accounting year. Make sure the period in question is the last period of the accounting year. In the image, December is the current accounting period (Period 12). A black arrow is shown in the Current column next to the row which is the current accounting period.
2.    
Click the button Change year ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calendar_next.png) and then click OK (this button is activated when the current period is the final period of the accounting year).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/ChangeAccountingYear.png)](../../../../Resources/Images/FAQ_Snippet_Images/ChangeAccountingYear.png)
3.   
You then enter the new active accounting year. By default the next calendar year is suggested. Click OK to make the system generate the new accounting year.
> Please note! This generating of a new accounting year might take a few minutes and it might look as it the program is not responding. You must wait until the program has finished the generation of the new accounting year. Do not close the program bottom at this stage!
You can read more about [changing the year](../../Using/ChangeYear/ChangeYear.htm) here.
Can you work in the annual financial statement and the new accounting year at the same time?
When you have created the new accounting year, you can go back to the AFS (the previous accounting year) to add transactions and complete the financial statement.In the Accounting year section in the backstage of the desktop you can change the accounting year to work in. This change then applies for all procedures.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/ChangeAccountingYearBackstage.png)](../../../../Resources/Images/FAQ_Snippet_Images/ChangeAccountingYearBackstage.png)
If you shift between accounting years this will only apply for the logged-in user in question. Thus, it is possible for different users to work in different accounting years in parallel.
You can also temporarily shift accounting year in certain procedures by clicking the button Change accounting year ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calendar.png) on the toolbar of the procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/ChangeAccountingYearProcedure.png)](../../../../Resources/Images/FAQ_Snippet_Images/ChangeAccountingYearProcedure.png)
If you shift between accounting years in a procedure, it will only apply in that specific procedure and at that time. If you close the procedure and open it again, you will automatically be in the current accounting year (the new accounting year).
What is worth bearing in mind after having changed the year?
When you have changed year, you should check that:
- The period distribution for the new year is correct. Reopen the Change period/accounting year procedure and make sure periods 1–3 are open for accounting.
- The Income statement has been reset and the Balance sheet for the new year only contains preliminary OB. You should check this in the Print accounting report procedure.
- Check that the Income statement and Balance sheet in the annual financial statement are correct.
If the company use integration between the accounts payable/accounts receivable and the accounting, it is important to remember that journals belonging to the new accounting year cannot be printed and reset until you have you have changed to a new accounting year. This also applies when you use integration to the Accounting without printing a journal.
> Please note! A voucher number series linked to a journal with integration set to Direct per invoice, will keep going and does not restart the number series. For these voucher number series the field Next voucher number is deactivated. The other voucher number series automatically start over from 1 after you have changed to a new accounting year.
How do I load OB when year-end closing is completed?
When the year-end closing work in the AFS is completed (normally when the annual financial statement vouchers have been loaded in the AFS) a definite loading of the opening balance (OB) to the new accounting year. Follow these instructions:
1. Make sure you are working in the current accounting year (the new accounting year).
2. Open the Opening balance.
3. To load all opening balances, you click on the button Load OB from previous year's CB![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_databaseImport.png).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/ChangeYearLoadOB.png)](../../../../Resources/Images/FAQ_Snippet_Images/ChangeYearLoadOB.png)
Please note! You can load the OB as many times as you wish.
> Please note! Remember to close the final period in the AFS (the previous accounting year) when all reconciliations have been performed!
How do I record the result of the financial year at the start of the new accounting year?
The recorded result in the AFS (the previous accounting year) must be manually recorded in the current accounting year (the new accounting year).
Why is there a difference between the accounting program and Monitor ERP?
If there is a difference between the accounting program and Monitor ERP, and you consider the annual financial statements to be complete, the most common reason is that not all of the annual financial statement vouchers have been loaded into Monitor ERP.
