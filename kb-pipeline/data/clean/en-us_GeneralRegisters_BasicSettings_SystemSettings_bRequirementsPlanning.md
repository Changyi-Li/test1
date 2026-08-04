### Requirements planning

#### Number of work days per year
This system setting determines the number of work days per year in the company. The number of work days is a factor in the calculation of a part's daily pace, based on the part's annual budget. The daily pace is calculated as: Annual budget / Number of work days per year.

#### Validate best-before date
Here you decide how the system should check and handle expired best-before dates on parts’ batch number/serial number when these are withdrawn from stock. The following options are available:
- Inactive – No check/validation of best-before date is made. The batch number’s/serial number’s balance can be used in stock transactions. Best-before date is displayed at delivery reporting. In the Part register the batch number’s/serial number’s balance will be shown in red font if the best-before date has expired.
- Warn – A warning is shown informing you that the best-before date has expired for this batch number’s/serial number’s balance, if is used in stock transactions or during material clearance. In the Part register the batch number’s/serial number’s balance will be shown in red font if the best-before date has expired.
- Block – The batch number’s/serial number’s balance is blocked if the best-before date has expired and it is considered unavailable. It is not possible to clear or use balance with an expired best-before date in stock transactions. An error message will then be shown. Expired balance will also be excluded in requirement calculations. In the Part register the batch number’s/serial number’s balance will be shown in red font as well as crossed out, if the best-before date has expired.

#### Reschedule suggestion within safety time
With this setting you decide if the system should suggest rescheduling within the part’s safety time or not, if a need for this is found using a requirement calculation or via the Purchase order suggestion or Manufacturing order suggestion procedures.
- No (default) – The system will not suggest rescheduling within the parts’ safety time.
- Yes – The system will suggest rescheduling within the parts’ safety time.
