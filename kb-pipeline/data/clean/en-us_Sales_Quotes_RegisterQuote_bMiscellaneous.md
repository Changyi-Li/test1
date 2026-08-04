### Miscellaneous
Here you find miscellaneous information about the quote. The information in this box corresponds to the information in the [Miscellaneous](../../Orders/RegisterCustomerOrder/bMiscellaneous.htm) box on a customer order, apart from the information described below.
Order date will be entered in the Customer order box, when the customer order is created from the quote.

#### Preliminary
Activate the Preliminary checkbox on quotes which are not yet finished (preliminary). A preliminary quote is labeled with the text "Preliminary" diagonally across the quote at printout. A preliminary quote exists in the quote register and can be listed in the Quote list procedure. It is not possible to create customer orders based on preliminary quotes.

#### Probability code
Here you enter how probable it is that the quote will be turned into a customer order. The suggested probability code for a new quote is the code selected by default in the Probability codes procedure.
Under the Probability code field a text shows if the quote is included in the requirement calculation or not. This is determined by the order type for the quote. The probability code of the quote determines how big a percentage of the quote row quantity should be included in the requirement calculation/net requirement calculation. In the Requirement calculation and Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedures, Quote must also be selected to be included in the calculation.

#### Requirement calculation
Here you see if this order type is included in the requirement calculation and net requirement calculation. This is determined by a setting on the order type for quote in the Order types procedure. Each quote row that has a delivery date entered will be included in the calculations according to the probability percent linked to the quote's probability code. Preliminary quotes cannot be included in requirement calculations or net requirement calculations.

#### Status
In this field you see/enter the status of the quote. The available quote status options are:
- 1) Registered – This is the default status for new quotes that you register.
- 2) Printed – This status is given when the quote is printed from the Documents tab.
- 6) Finished – This status can be set manually, if you wish to finish the quote without turning it into an order. When you select status 6, you must also select a cause code regarding why the quote was lost. You can also enter a comment for the cause.
- 7) Partial order – This status is used when the quote is turned into a customer order and the setting Finish this quote is unchecked under the button Create customer order.
- 8) Order via related quote – This status is given when a customer order is created based on a quote related to this quote and the setting Finish related quote is checked under the Create customer order button.
- 9) Order – This status is given when the quote is turned into a customer order and the setting Finish this quote is checked under the button Create customer order.

#### Cause of lost quote
If the status is set to 6 (Finished), you must select a cause code in this field. Cause codes for lost quotes are handled in the Cause codes procedure. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to the right of the cause field, you can enter a comment regarding the the cause, that is, why the quote is being finished. This comment can be configured as mandatory.

#### Factoring
With this setting you select if factoring should be used for this quote. If factoring is activated for the customer in the Customer register, this checkbox will be activated by default on the quote.
