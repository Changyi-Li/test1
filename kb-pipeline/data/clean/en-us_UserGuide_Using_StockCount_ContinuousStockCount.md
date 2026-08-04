### Continuous stock count
The continuous stock count is managed per location/part with the help of a stock count intervals. You enter a stock count interval (interval of months) for the part and the interval is based on the previous stock count. If a stock count was performed on July 12, 2020, the final date for the next stock count will be July 12, 2021 (a 12-month interval). When a stock count has been performed, a Last stock count date is saved for the part.

#### The stock count interval can be determined using the ABC code.
The stock count interval can be linked to the part's ABCABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. code, meaning when an ABC code is entered, the interval will be included. You configure the intervals under the ABC codes tab in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure. The default interval is 12 months. It is possible to manually change the interval for a part even though an ABC code has been entered. This is done by marking the Override inherited interval checkbox and enter the interval you want (in months) under the Stock tab in the Part register procedure. In the Part list procedure you can mass-update stock count intervals.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/StockCount6.png)

#### Stock count due date
To be able to perform continuous stock count with a "stock count due date", you must perform an initial stock count for the part.

#### Stock count in list – Create stock count basis
In the settings for the "Create stock count basis" list type, it can be good to use "Stock count due date – To date" to be able to limit for how far ahead in time the list will present locations/parts.
In the settings you can name the stock count basis and enter a person responsible for the stock count.
You can configure this list and run it using the Agent option and there create an Agent task which will, for example, each month automatically print a stock count list over the parts that are to be stock counted "T+30 days ahead in time".
> In the logic behind continuous stock count, a Last stock count date is required in the Part register. The first time a part will be stock counted using continuous stock count you must create the list based on other criteria since there is no "last stock count date" because no stock count has been performed. To solve this there is a fallback value for the date meaning the registration date of the part will be used. If no such date is available, a very early date will be entered instead.

#### Stock count in list – Manage stock count
This list is used to manage/administer the stock count lists, and here you can start reporting of stock counts, pause, and delete stock count lists.
