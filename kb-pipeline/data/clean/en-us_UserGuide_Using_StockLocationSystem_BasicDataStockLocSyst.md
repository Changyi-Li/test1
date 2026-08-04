### Basic data – Stock location system
In the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Stock location system procedure you must configure settings for the storage types in the warehouse.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/StockLocation1.png)
Example of how a warehouse can be structured using coordinates.
Please note! You must also generate locations in the Generate locations procedure before you can use the Stock location system. Use the location coordinates which you create in this procedure as a template/starting point when you generate locations. The format of the coordinates and the location names will then match.

#### Naming conventions – Advanced stock management
We highly recommend using naming conventions for ALL locations in the warehouse.
Why is it so important?
- To facilitate implementation of putaway strategies.
- Make it easier to sort locations.
- Using consistent names will reduce misunderstandings.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Coordinates.png)
Example of how location names (coordinates) can be constructed.

#### Storage type
In the Storage type box you must create storage types in order to be able to define the different possible structures (coordinates) in the warehouse. For example, pallet racks (for different types of pallet), pipe racks (for long parts such as pipes, rods and cable racks), box systems and more.
> Use a good name which describes the storage type.

#### Location coordinates
This is linked to the storage type, so here, you decide which coordinates will be used for the storage type. As an example we can use A1-B1-C1-01.
> Please note! It is recommended to have the same location name and location coordinates as it is not possible to load the coordinates automatically if the location name does not match the coordinate system.
Basic types
The basic types are used to define which coordinate is which in the structure. There are a few predefined basic types: Zone, Aisle, Shelf, and Level, plus four others, as well as a Delimiter. Coordinates are created for each storage type, for example, Zone, Aisle, Shelf, and Level. For each coordinate, a format is entered which builds the location name. For example, A1-B1-C1-01 could describe Zone A1, Aisle B1, Shelf C1, and Level 01. You can enter up to 8 basic types for a storage type (plus delimiter). A basic type can only be used once, except for the delimiter which can be used multiple times.
> Use the Description field to explain what the different basic types mean for your company.
Number of characters
The number of characters describes how many characters are in the coordinate on that level. If it is A1-B1-C1-01, it is 2 characters per coordinate.
Delimiter
The delimiter determines which character can go between the coordinates. You can use a period and a minus sign as a delimiter.

#### Location templates
In the Location templates box you can create templates to simplify the work of deciding the size of the locations, and enter a maximum weight for the locations.
It is possible to enter both minimum and maximum measurements. The minimum measurement is used to determine, e.g., whether or not half-pallets can be used. (If there is an extra beam in the shelf where half of the pallet’s length would fit)
