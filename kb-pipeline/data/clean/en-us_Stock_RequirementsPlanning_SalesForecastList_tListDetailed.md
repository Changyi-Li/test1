### The Detailed list

#### Forecast code
Here you can see the forecast code. This code is a unique number for the forecast.

#### Name
Here you can see the name of the forecast.

#### Part number
Here you can see the part number which has been forecast.

#### Delivery date
Here you see the forecast delivery date. This date can be changed.

#### Original forecast
Here you see the forecast quantity. It is always saved in the standard unit. This quantity can be changed.

#### Price each
Here you see the price each that applies to the part.

#### Original amount, forecast
The original amount is calculated: Price each in the company currency x original forecast quantity.

#### Net amount
The net amount is calculated: Price each in the company currency x Net forecast quantity.

#### Net forecast quantity
Original forecast minus Ordered quantity. Only actual customer order rows are deducted from the forecast. If the order or the order row is deleted, this quantity will no longer be deducted from the forecast (but they remain in the database for the order inflow). If you have manually deleted a remaining quantity, the ordered quantity will still be deducted.
You can modify the net forecast quantity manually. But if a net requirement calculation is then run and has the forecast deduction activated, it will calculate a new net forecast quantity. This means a manual change is only temporary.
This field is used when the parts' deduction method has been set to Periodic intervals. Please note! This field is shown even though you might not be using Periodic intervals as deduction method for the parts. The net forecast quantity will then correspond to the Quantity field in the Register sales forecast procedure and is used as forecast.

#### Ordered quantity
Here you see the ordered quantity of the part. This field is used when the parts' deduction method has been set to Periodic intervals.
