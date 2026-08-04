### Exceptions
Under this tab, you find a table where you configure general exceptions for matching of extra invoice rows that the supplier often adds on invoices. This can be rows used for freight, packaging, alloy costs, setup costs, etc. The purpose is that EIM Workflow should be able to match these extra invoice rows with the exceptions. This way you can prevent the invoice from being stopped in the flow.
In the Supplier register procedure, under the EIM Workflow tab, you can also add from these exceptions that will then only apply to the supplier in question. This will then override these general exceptions.
When you install the system, there are a number of rows with exceptions included in the system. These are commonly occurring exceptions for extra invoice rows, which match the part numbers that CrossState assigns extra invoice rows when interpreting. This will make it easier for you when you start using EIM Workflow, since invoices with extra invoice rows will be matched with a basis and will not be stopped in the work flow. Three invoice exceptions are also included in the Monitor-to-Monitor import. For these exceptions you can only configure amount limits. Part settings are configured in the System settings procedure.
There are three system settings relating to part number for freight cost, packaging cost, and alloy cost. These system settings are used for matching such extra invoice rows during import of XML invoices when EIM Workflow is not installed. The system settings will also come into action when EIM Workflow is used, in cases where extra invoice rows are not matched with any of the exceptions here, as well as when importing M2M invoices (Monitor-to-Monitor). See the system settings for Part number for freight charge/packaging cost/alloy cost when loading XML invoice under the Purchase tab.

#### Name
Here you enter an internal name of the exception. This name is shown if you add the exception under the EIM Workflow tab in the Supplier register procedure.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Invoice's part number
The invoice's part number describes the exception type, and is a matching term for the exception. This part number will be shown on the invoice. The code that CrossState uses, is set on rows with exceptions that are included in the system. This should not be changed. If the invoice's part number in the exception is matched with part number on an extra invoice row, then EIM will accept the invoice row. If the invoice's part number is not matched, EIM Workflow will try to match the invoice's part name.

#### Invoice's part name
The invoice's part name is a matching term for the exception. If you enter a part name in the field, this must match the part name on the extra invoice row. Which part names are shown on extra invoice rows might vary. If you leave this field empty, which is selected by default, then no matching will be performed on part name in EIM Workflow.

#### Exception type
Here you decide how the exception row is managed. You need to select a Matching rule for each exception type.
The following exception types are available:
- Standard (can be linked to part, account, allocate difference, or be exempted from matching)
- Setup cost (the exception is handled as a setup cost)

#### Matching rule
Here you decide how the exception row is matched. Different matching rules are available, depending on the exception type that has been selected.
If the exception type is Setup cost, you will need to choose whether the exception row should be managed manually or be linked to the above invoice row. If handled manually, you get to link the extra invoice row with the setup cost to an invoice row in the Register supplier invoice procedure. When linking to the invoice row above, the extra invoice row with the setup cost will automatically become linked to the invoice row (delivery row) which is positioned above the setup cost row on the invoice.
If the exception type is Standard, you will need to choose whether a part or an account should be linked to the exception row. You can also choose whether the row should be exempted from matching. Below you will find more information about the different matching rules.
Link part
The Link part matching rule allows you to select a part in the part register to link to the exception row. EIM Workflow will then create an order row on the invoice basis for the extra invoice row (for statistics) that is matched. This row will then be posted via the posting matrix (the part's product group and the supplier group). The part you want to link can be selected in the Part column. If you have selected a linked part, you cannot select an account.
Create posting
You can use the Create posting matching rule to select an account in the chart of accounts to link to the exception row. If you select an account, EIM Workflow will only create one posting row on the invoice basis for the extra invoice row that is matched. When you have selected an account, you can also add exception accounts to the row, see Exception account below.
Exclude invoice row from matching
When you select this matching rule, if the exception matches an invoice row, the invoice row will be deselected and excluded from matching in EIM Workflow. This means that any row amount will need to be posted/adjusted manually when authorizing/final recording.
> This matching rule is useful of you receive invoices with rows that you do not want to link to a specific part or account. This could be e.g., rows that affect the entire invoice such as a row with total discount. By exempting the invoice row from the matching, the invoice row will be ignored by EIM Workflow. This means that the invoice will not be “stuck” in the Find order/part inbox where it needs to be forced for authorization. The invoice will instead be automatically sent to the signer (as long as all the other invoice rows are matched) which helps create a more efficient workflow.
Allocate difference
When an exception with this matching rule matches an invoice row, the row amount will be distributed to the other matched/linked purchase order rows. This matching rule comes into effect at the final coding when it assumes that all invoice rows have been matched.
> Please note! This matching rule only works when EIM Workflow automatically can final code the invoice. If this condition is not met, you need to manually handle the allocation.
> This matching rule can make it easier for you who apply the FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. method to value your material purchases. You can then distribute, for example, the freight cost on the invoice, evenly over the purchase order rows – instead of posting the freight separately and that way loose the freight cost in the stock value.

#### Cost center/Cost unit/Project
If you have selected an account, you can here enter a distribution to different dimensions such as cost center, cost unit, and project.

#### Amount limit, price each
Here you see the amount entered as amount limit for price each in the company currency under the Amount limits button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).

#### Amount limit, row total
Here you see the amount entered as amount limit for row total in the company currency under the Amount limits button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).

#### Amount limit, invoice total
Here you see the amount entered as amount limit for invoice total in the company currency under the Amount limits button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).

#### Amount limits (A)
By clicking this button you can enter amount limits for the exception in different currencies. You can enter amount limits for price each, row total, and invoice total. You can enter amount limits for all currencies registered in the Currencies procedure. You do not have to authorize extra invoice rows that are matched with this exception, and that have row amounts up to and including this amount in the same currency. If a row amount is greater than this amount, then EIM Workflow will send the invoice row for approval.
If no amount limit has been entered (the field is empty) for a currency, all row amounts on extra invoice rows in that currency which matches this exception will be allowed. A warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is then also shown in the field. This lets you know that no amount limit has been entered for the currency. If you enter zero, no amount will be allowed.
-   
Amount limit, price each – EIM Workflow checks the price each on the invoice row for the exception. If the price each exceeds the amount limit, the invoice will be sent for approval.
-   
Amount limit, row total – EIM Workflow checks the row total for each invoice row for the exception. If the row total exceeds the amount limit, the invoice will be sent for approval.
-   
Amount limit, invoice total – EIM Workflow checks the invoice total, i.e. the total of all invoice rows for the exception. If the invoice total exceeds the amount limit, the invoice will be sent for approval.

#### Active
Here you decide if the exception should be active or not. All accounts are set as active by default. Then they are used in EIM Workflow to match extra invoice rows.

#### Exception account
By using the E button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select exception accounts for different supplier groups as exception for the selected account on the row. Then you can also select distribution in different dimensions.
