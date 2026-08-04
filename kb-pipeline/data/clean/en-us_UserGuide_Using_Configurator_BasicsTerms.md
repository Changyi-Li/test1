### Terminology and basics

#### Basic BOM and routing
The BOM and routing for a configured manufactured part should describe a stripped basic model. That is, it should only include the elements that will always be included in the product and the elements which are not optional in any way. To this so-called Basic BOM and routing you then add operations and material via the configurator.

#### Part possible to configure and configuration group
A part which should be possible to configure you link to a Configuration group. The configuration group contains most of the logic. This is found in the Option lists and Variables which are required in order to define the wanted variants/versions/designs.

#### Rules
The configuration group also contains Rules. These are required in order to:
- Exclude invalid options.
- Automatically add options which are the result of other choices made.

#### Section
To facilitate during order registration you can divide a configuration group in Sections. Each section is shown as a page when registering orders. In a section you then place option lists and variables in any optional order.

#### Option lists
An option list is, simply put, a list of parts which should be possible to choose from when registering orders.

#### Variables
Variables can be of different types and are used to:
- Handle values which are needed as information, for example a color code.
- Perform time and quantity calculations.
- To create rules.
The value of a variable can be:
- Entered when you register an order.
- Calculated via formulas.
- Determined by the choices made in the configurator.

#### Formulas
Formulas are used in several different ways and the thing they have in common is the use of variables to perform calculations.

#### Configured instruction (CI)
A Configured instruction (CI) is an instruction containing variables and formulas embedded in static text. It is possible to configure instructions both for material and operations in BOM and routing.

#### Main part
A Main part"Main part" is the term used for the part in the top node (highest level) in a structure of parts. is the part in which the parts selected in the configurator should be included in when the manufacturing order is created. By entering a main part you can direct material to different levels in a structure order containing multiple levels.
