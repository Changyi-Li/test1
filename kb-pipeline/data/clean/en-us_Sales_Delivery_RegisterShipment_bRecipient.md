### Recipient
Information regarding recipient of the shipment is loaded from the customer register and the customer order if such has been registered.

#### Reference person, Phone, Mobile phone, and E-mail
If the source of information is Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order., Pick list with package structure, or Customer (and the customer has "Recipient of" set to Advice to shipping agent or Shipping agent's SMS advice), these values will be loaded to the fields for phone, e-mail, and mobile phone. If no communication records exist, the value from the customer's standard reference will be used instead.
If you use nShift Web-TA as plugin, there are checkboxes by the Phone, Mobile, and E-mail fields which will determine the advice method that should be used. Default value can be loaded from the Shipment template in the Shipment templates procedure. If you activate a checkbox, an already marked box, if any, will be deactivated.
In the same way as when you are using Customer as source of information, the sources of information Pick list/Pick list with package structure will load:
- Phone numbers from the Communication – Delivery address box, if it is marked as Advice to shipping agent in the Recipient of. Otherwise the phone number from the standard reference will be used.
- E-mail address from the Communication – Delivery address box, if it is marked as Advice to shipping agent in the Recipient of. Otherwise the e-mail address from the standard reference will be used.
- Mobile phone number from the Communication – Delivery address box, if it is marked as Shipping agent's SMS advice in the Recipient of. Otherwise the mobile phone number from the standard reference will be used.

#### Customer number, shipping agent
Here you can see the customer number at the shipping agent. This is loaded from the customer register.

#### Pallet registration number
Here you can see the pallet registration number at the shipping agent. This is loaded from the customer register.

#### Reference
The recipient's reference on the shipment is loaded according to the Load to the recipient's reference on shipment system setting.
