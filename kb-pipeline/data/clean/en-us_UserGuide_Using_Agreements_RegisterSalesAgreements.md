### Register customer agreement
In the Register customer agreement procedure, you register new agreements and modify existing agreements. Unlike a customer order, for example, an agreement never results in stock transactions. Agreements are intended to be used for invoicing of, for example, a service according to a decided invoicing interval.
When you register an agreement and this agreement gets status 3 (Active), an agreement basis is created based on the settings configured and the rows on the agreement.
To create an invoice basis you have to release an agreement basis.
> An agreement basis which has been released is blocked from all changes that is done on the agreement. That is, if you make changes on an agreement this will only affect/update agreement bases which have not yet been released. These agreement bases are updated every time you click Save.
The Header tab

#### General
In the General section you configure the duration and dates that apply for the agreement. For example, between which dates the agreement is valid, when the agreement was signed, and how long the notice period is, etc.
Here you can also see the status of the agreement. Only when an agreement reaches status 3 (Active) will an agreement basis be created based on the settings made under this tab, and also based on the rows registered on the agreement.
If you activate the Update status automatically setting, the status of the agreement will become updated from status 2 (Signed/Valid) to status 3 (Active) when the Valid from date occurs. The same way the agreement will change to status 6 (Closed) when the date entered under Valid to has passed.
Important if you have suspended VAT activated during advance invoicing for agreements
- When invoicing, the VAT account for suspended VAT is used as well as the standard account for preliminary accrual account.
- When payment is made, the suspended VAT is transferred to the account for output VAT and the net amount is transferred to the accrual account according to the agreement.
- If the Basis for VAT report is loaded from system setting has been set to VAT code in general ledger transactions, the following applies: When paying an advance invoice a VAT code is entered on the posting row regarding paid advances. The VAT code is loaded from the invoice being paid. This results in a correct accounting of turnover in connection with when the VAT accounting loads the basis for the VAT report via VAT code on general ledger transactions.
- If the system setting is set to load VAT code in chart of accounts, the VAT code will be used according to the setting of the account, when you do not consider the VAT code of the transaction. In order not to create differences in the VAT accounting, the account for paid advances is linked to the VAT row for turnover liable to VAT.

#### Invoicing
During invoicing, you decide how, and how often, the agreement will be invoiced. It is important to keep in mind that the invoicing interval determines what type of price is used on the agreement rows. If you, for example, have selected the Annually option as invoicing interval, this means the price on the agreement row will be interpreted as an annual price.
Price definition
If you have entered an annual price in the Part register which you wish to invoice per month, you should use the Price definition. Here you enter what type of price is registered on the agreement rows. This makes it possible to divide an annual price and invoice it per month. For example, if a part has an annual price of EUR 12,000 you can by configuring the Price definition to Annual, and the Invoicing interval to Monthly, invoice the customer EUR 1000 per month.
Invoice current month
Determines if the current month will also be invoiced.
Release basis automatically
In order to avoid manual administration to release agreement bases for all agreements you have registered, you can use the function called Release basis automatically. This function will release the invoice bases on the date entered as Planned invoice date. The default value of this setting is determined in the Order types procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement2.png)](../../../../Resources/Images/UserGuide/Agreement2.png)
Customer order
As mentioned earlier, no stock transactions are made from an agreement. But it is possible to link/connect an agreement to a customer order. This is done in the Customer orders box. You can only link an order which has the same customer as the agreement. When an agreement and a customer order is linked/connected, you are able to see the agreement number under Grouping/Posting in the Register customer order procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement3.png)
The Rows tab
Under the Rows tab you add the parts (services) that should be included in the agreement. If you use Price definition on the agreement you see the price that will be invoiced according to the entered Invoicing interval. This is shown in the Price/Inv. interval column.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement4.png)](../../../../Resources/Images/UserGuide/Agreement4.png)
One-time costs
If there are costs you only wish to invoice one (1) time, you can on the row mark that it is a one-time cost. This is done via the One-time cost button. Enter if the row should be invoiced together with the other rows on the agreement or if a new agreement basis should be created, that is, it should be invoiced separately. If you choose to invoice the row separately, you are free to enter a Planned invoice date.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement5.png)
In the same way as in the General section under the Header tab, you can per row enter a Valid from and a Valid to. This is useful if you, for example, wish to invoice specific rows only for a certain period of the agreement period. The dates you enter here will determine on which agreement bases the agreement row will be included.
Upward adjustment rows
In cases where an agreement is invoiced in advance, and when the agreement is changed during a period which is already invoiced, then you can separately invoice the extra cost that arises for the customer (or put it on the next invoice). This is done with the help of a so-called Upward adjustment.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement6.png)](../../../../Resources/Images/UserGuide/Agreement6.png)
There are two ways to trigger an Upward adjustment. Either by modifying something directly on the row which affects the row amount, for example, changing the quantity, price, or discount.
- You can also trigger an Upward adjustment by entering a Future quantity, Future price, and/or Future discount, which starts applying in an already invoiced period.
- In the example below the price is increased from EUR 12,000/year to EUR 15,000/year as of May 19, 2022. Since the period May 1, 2022 – May 31, 2022 is already invoiced, an upward adjustment of EUR 125/month will be suggested for the period May 19, 2022 – May 31, 2022.
If you place the cursor over the button on the row, you will see the suggested upward adjustment amount.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement7.png)
To create an upward adjustment you just click the plus button. A new row is then created on the agreement with the amount which was suggested as upward adjustment, as well as a linked text row where you see the period to which the row refers. The created row will be a One-time cost, that is, it will only be invoiced once. The other agreement bases which are not yet released, will be adjusted according to the changes made.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement8.png)](../../../../Resources/Images/UserGuide/Agreement8.png)
You can hide the one-time costs by using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusInvoice.png) button on the function menu.
The Agreement basis tab
Under the Agreement basis tab you find all agreement bases created for the agreement in question. This tab is available when agreement bases exist. These are created by a monitoring service which runs on the Monitor server every night and creates agreement bases for agreements that have been given the status 3 (Active) and have agreement rows. Agreement bases are only generated for 12 months ahead. This means that if an agreement spans more than 12 months, you will initially only see invoice bases for 12 months ahead anyway. The system ensures that there are always bases for 12 months ahead.
Under this tab you can Release agreement basis ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png). The invoice basis is not created until the agreement basis is released. As mentioned earlier, a released agreement basis is not affected by changes made to the agreement.
If you have released a basis by mistake, you can Undo release of agreement basis ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png).
It is not possible to undo an agreement basis which is invoiced. In that case you first have to credit the invoice. This can be done via the Credit invoice button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/addCreditImage.png). Under the Credit invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/addCreditImage.png) button there are two options, Re-invoice after credit and Invoicing complete after credit. All information from the basis and customer order that are created in the background are loaded.
Re-invoice after credit backtracks the status of the agreement basis to Registered, and the basis can once again be released after credit. This means the customer will be invoiced once again when you have credited the agreement basis.
- Invoicing complete after credit retains the status of Invoiced on the agreement basis after credit. This is used when the customer is not to be invoiced again after you have applied a credit.
- Use the Suspend ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPaused.png) button to suspend an agreement basis, and it is no longer possible to release the agreement basis. This is useful if you don’t want the agreement basis to be invoiced. This means the agreement basis can no longer be released automatically if you have checked the Release basis automatically setting. When an agreement basis has been suspended, it cannot be released manually.
Use the Resume ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) button to once again release the agreement basis which is suspended. The Resume button is used to change the status of the agreement basis from Suspended to Registered.
Under Row information you see all rows that exist in the agreement basis which in their turn will be included on the invoice basis.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Agreement9.png)](../../../../Resources/Images/UserGuide/Agreement9.png)
Under Row information you see all rows that exist in the agreement basis which in their turn will be included on the invoice basis.
