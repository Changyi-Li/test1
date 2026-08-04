### The list Order simulated price (and External)
In this list you calculate the price corresponding to the price created at registration of customer order. The price can be loaded from price list or from customer link. The discount can be loaded from customer link for, customer's general discount, or customer's discount category. The list is printed for one customer at a time.
The external list is the same as the list described above, but it is adapted to be sent by e-mail to customer. A text file is attached in e-mail messages sent from the procedure.

#### Quantity
Here you see the quantity according to the order of priority entered in the table called Order of priority for quantity.

#### Gross price
In this column you see the price loaded when registering the order. The order type selected under the Selection tab will be taken into consideration.

#### Discount
The discount is primarily loaded form the customer link. If that discount is 0, then 0% is shown regardless if the customer has a discount category or a general discount. However, if there is no discount in the customer link, then the discount from the discount category will be shown. For this, the same as described earlier will apply. If discount category is missing, the discount will instead be loaded from the customer's general discount.
> The discount being 0 (zero) is not the same as when no discount has been entered. Zero counts as a value. If there is not discount, it means that the field in question is empty.

#### Net price
This column shows the gross price minus discount, if any. This is calculated as gross price × (1 − discount ∕ 100).

#### Price via
(Not in the External list) Here you see if the price is loaded from a price list or a customer link. If the price is loaded from a price list, then you can see from which price list in the next field.
If staggered prices are shown, then the price is shown without the discount selected for the customer.

#### Lead time
The price on the row also determines which lead time that is shown. If the price is via a customer link then it is the customer link's lead time which is loaded (from the Part register). If the price is via price list, then it is the lead time entered in the Miscellaneous box under the Sales tab in the Part register that will be loaded.
