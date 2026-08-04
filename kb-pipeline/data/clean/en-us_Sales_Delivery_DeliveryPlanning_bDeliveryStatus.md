### Delivery status (Customer)
In the Delivery status or Customer box (for the Picking plan – Per customer list type) on the Rows tab, you see the calculated delivery status for selected customer orders. For each customer order you find the following information: customer number, customer name, city, delivery address (DA), delivery method, number of orders, number of rows, and number of handing units.
At the bottom of the tab you see a total of number of orders and number of rows, net weight and gross weight, net volume and gross volume, pick time, and number of handling units. This is the total for all orders where Pick is marked in the list. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see shipping information for each handling unit.
The rows of customer orders are grouped in sections according to the following (not for the Picking plan – Per customer list type):
1. Ready for delivery – Here you will see orders for which you can print a pick list and also deliver. One pick list will be printed per customer and delivery address.
2. Ready for delivery – Credit limit exceeded – Here you see orders you can delivery, but which have exceeded the credit limit. If the system setting Handling of credit limit at delivery has been set to Block, then it is not possible to deliver when the credit limit has been exceeded. With the system setting called Credit limit compared with, you determine what the credit limit should be compared with.
3. Ready for delivery – Unpaid advance invoice – Here you see orders you can deliver, but the advance on the order has not been paid in full. If the setting called Check for unpaid advance invoices in the Invoicing plans procedure has been set to Block, then it is not possible to deliver. However, you can still print a pick list for the order.
4. Waiting list – Here you see orders you can deliver, but that are not grouped under "Ready for delivery" because partial delivery is not allowed on order level.
5. Shortage list – Here you see orders you should deliver, but that are not possible to deliver because of part shortage.
6. Unconfirmed – Here you see orders where the delivery date on the order rows cannot be confirmed.
7. Preliminary – Here you see orders where preliminary pick list is applied.
8. Preliminary – Credit limit exceeded – Here you see orders that apply preliminary pick list, but which have exceeded the credit limit. If the Handling of credit limit at delivery system setting has been set to Block, then it is not possible to deliver when the credit limit has been exceeded. With the system setting called Credit limit compared with, you determine what the credit limit should be compared with.

#### Pick
Check the Pick checkbox for the orders ready for delivery which you want to include on pick list when saving. In the Order rows box, the Pick checkbox will be marked for all order rows on the selected order. Only orders in the section Ready for delivery can be marked to be included in pick lists. By using the setting Suggest picking of orders ready for delivery under the Selection tab, you can determine whether or not the checkbox should be activated by default for all orders in the section Ready for delivery. It is also possible to check the box in the column heading to mark all orders.

#### Delivery address (DA)
By clicking the button Delivery address ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) (DA) on the row, you open a dialog where you can see the customer's delivery address. In the dialog window you can use the button Settings for address ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_settings.png) to see (and change) the language, document group, and address format, for the delivery address. Here you also find a button to preview the delivery address and to see it in Google Maps.

#### Number of rows with shortage (List type Picking plan – Per customer)
Here you see how many of the order rows that have a shortage, that is, where there is a shortage of the parts.
