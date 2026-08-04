### Settings – Check delivery times
Type of requirement to analyze

#### Actual orders
Requirements from actual purchase orders will be analyzed by CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. (default).

#### Suggestions
Requirements from order suggestions will be analyzed by CDT.

#### Forecast
Requirements from sales forecasts will be analyzed by CDT.
Simulate delay

#### Add X days to delivery date on confirmed row
Here you add a number of days to the delivery date so that CDT can simulate a delayed arrival of already confirmed purchase order rows. This way you see the consequences for existing material requirements, order suggestions, customer orders, sales forecasts, and stock orders. Zero (0) days is entered by default.

#### Add X days to delivery date on unconfirmed row
This setting corresponds to the setting above but for unconfirmed order rows instead.
Include

#### Parts without stock update
With this setting you decide if parts which are not stock updated should be included in CDT or not.
