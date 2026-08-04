### Rows
Under the Rows tab you can add rows for the parts that are to be included in the specific quote and information regarding them.
The information and functions on quote rows and below the rows in the tab, are the same as on [customer order rows](../../Orders/RegisterCustomerOrder/tRows.htm). The information that differs from the customer order rows, are described below.

#### Mark-up
The system setting called Manage mark-up on quote determines if quote rows should manage mark-up in percent on standard price to provide a quote price. In addition to the contribution ratio (CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage.) you will also see the contribution margin (CM The contribution margin (CM) is the difference between the standard price and the sales price.) for both the quote row and in total for the quote.

#### Delivery date
The delivery date on quote rows is always empty by default, unlike on customer order rows. It is not mandatory to select a delivery date. Normally, you enter the delivery date in the quote header or you select a certain Delivery time after an order has been registered.

#### Calculate
For row type 1, you can with this function perform a pre-calculation of the quote row. You can perform the pre-calculation by using the button Calculate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) on the toolbar, if this checkbox is activated. If you do not use that button, the calculation is instead made when saving. The calculation takes place in the background.
Under the Document structure tab, you can add documents of the type Calculation for the function Calculate. These documents will show summarized information from pre-calculations made for the quote rows. Please note that the calculation document that is printed or sent by e-mail always shows information in the standard unit of the parts.

#### Link to pre-calculation (L)
If a pre-calculation has been performed regarding the quote row, a button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) will appear in this column. Using this button you can then go to/link to the calculation in the Pre-calculation procedure.

#### Calculation
For row type 1 that have not been calculated, or for row type 2, you can manually create a simplified calculation. By using the button Calculation ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), a calculation window will open where you can add cost types (Material, Subcontract, Processing), texts that describe each respective cost, unit and setup costs, mark-ups, and prices. By using the button Apply calculation in the window, the calculation will be saved on the quote row. The button Calculation on the quote row changes color ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png) when a calculation is saved.
The system setting Load sales price from quote calculation determines if the sales price should be updated from the calculation. Otherwise, only the standard price will be saved on the quote row and the sales price is configured as usual (price linked to the customer or price from the part’s price list).
Both calculation variants generate different prices depending on the quote row quantity if setup times/setup costs are included in the calculation. You can then create a quote row, copy it, and then modify the quantity in order to quickly be able to provide the customer with different prices for different quantities.
A setting for the Quote document in the Document settings procedure, determines whether or not calculation information should be displayed on the quote when printed, and in that case, if the calculation information will be detailed or total.
If you check Calculate on the quote row, the Calculation button will disappear from the row. A pre-calculation can then instead be performed for the quote row, according to the description above.

#### Customer order
When creating a customer order based on the quote, this checkbox determines if the quote row should be included on the order. You can only choose to include main rows and only the rows that have not already been included in a customer order. You create customer order from quote by using the Create customer order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_new.png) in the Customer order box under the Header tab.

#### Blanket order
When creating a blanket order based on the quote, this checkbox determines if the quote row should be included on the blanket order. You can only choose to include main rows and only the rows that have not already been included in a customer order or blanket order. You create a blanket order from quote by using the Create customer order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_new.png) in the Customer order box under the Header tab.

#### Order number
If the quote row is already included in a customer order, you will in this column see the customer order number where it is included.

#### Link to customer order (L)
If the quote row is already included in a customer order, you can here go to/ink to the Register customer order procedure with the order in question loaded.

#### Exclude from statistics
With this checkbox you determine if the quote row should be shown in the Quote list and Quote statistics procedures. However, in these procedures it is possible to select to show excluded rows. If the checkbox Customer order is marked, then it is not possible to check the box Exclude from statistics.

#### Posting
Posting is never mandatory for quote rows, but can be mandatory for customer order rows. This is configured with the system setting Mandatory posting on order row. If you apply mandatory posting and do not select a posting of the quote row, you will get a warning letting you know that you should post the customer order row after the quote row has been turned into a customer order row.
Posting of dimensions can be performed automatically when they are linked to registers. This is determined by settings in the Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure. If you have a dimension linked to Employee, you will get an automatic posting via the seller entered in the Header tab.

#### Total
At the bottom of the tab there is a total of the row totals, including and excluding VAT. Read more about the [total](../../Orders/RegisterCustomerOrder/bSummaryOfRows.htm) here.
You can also see a total of the standard prices for all rows. This is calculated as standard price × quantity per row, and then the rows will be added together.
A total of the order's total net weight and volume are shown.
The transport time is also shown at the bottom of the tab. It refers to the transport time to the selected delivery address, primarily on the quote and secondarily on the delivery address entered on the customer. This transport time is possible to change. The customer's delivery days are also displayed. You can here see the rows’ total CM and CR to the right.

#### Transfer profile
This field is shown if the option Customer order transfer is used. Here you see the part's default transfer profile on a new quote row, if the part has a default transfer profile configured in the part register. Otherwise you can select a transfer profile for this row. This should be done in the sales company.
If you also use the Product configurator option and the order row has been remote configured, then it is not possible to change the transfer profile.
You can leave the field empty or clear the field, if the new order row shouldn't have a transfer profile.
