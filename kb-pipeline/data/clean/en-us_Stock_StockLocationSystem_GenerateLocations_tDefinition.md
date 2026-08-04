### Definition
In the table under this tab you create the definition for location names in the location register.
You create location names based on different coordinates such as aisle, section, level, or whatever you might call them in your stock. For each coordinate you enter start value, interval, and number of repetitions. You create several coordinates, which together creates the location name.
The location name can consist of a maximum of 35 characters. You can use letters, digits, and special characters when you create your coordinates. The characters _ and % are not allowed.
Below the table you see how many rows with location names will be generated based on the entered definition. A validation will be made if the definition results in more than 1 million rows.
Example:
Location A-18-10-01 is a location in Zone A, Aisle 18, Section 10, and Level 1. The location name consists of nine characters. (See the image below. Click the image to see a larger version).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/StockLocationChart.png)](../../../../Resources/Images/SubProjects/StockLocationChart.png)
In the table, the abovementioned zone in the location register would be defined with four coordinates (plus three separators) according to the image below. The zone consists of nine aisles, ten sections, and nine levels. The zone is the first coordinate. This definition generates 810 unique location names.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/StockLocationDefinition.png)
Storage types with linked location coordinates are loaded from the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Advanced stock management procedure.

#### Coordinate
Here you see/enter the number of the coordinate.

#### Start value
The start value is the numerical value or letter on which the coordinate should start.

#### Interval
Here you enter interval between each value. You can enter intervals for numerical start values.

#### Number of repetitions
Number of repetitions means how many times the start value should be counted up. You can enter this value for numerical values and if you only use one letter as start value. If you use two characters of which at least one is a letter, this field will be deactivated and you must instead use Custom sequence in order to access multiple variants for this coordinate.

#### Custom sequence
By using the button Custom sequence ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add a custom sequence of the coordinate in the location name. For example, if you want the name to start with Zone1, Zone2, and Zone3, or if it should start with A1, A2, and A3. Then you add these on separate rows under this button.
You can mix different names in a sequence. For example enter Zone1, Zone2, A1, and A2.
When you have entered a custom sequence, the columns Start value, Interval, and Number of repetitions will no longer apply to the coordinate on the row in question.
You can combine custom sequences in several coordinates. You can, for example, in the first coordinate term enter Zone1 and Zone2, and in next coordinate enter A1 and A2.
