### Product configurator
In G5, the Product configurator is an option in the same way as it is a supplement in G4.

#### General
- In G5 you can configure both manufactured and purchased parts.
- New versions (snapshots) of a configuration group is automatically created to avoid problems with locked registered orders.

#### Part register
- Default variable values are replaced by Default configuration/template which contains both variable values and options.
- There is a new alternative Open automatically which determine if the configuration window should be opened automatically or not.

#### BOM and routing
- Formulas for unit time and setup time on operation rows are found under the same button. The same applies for quantity formula and formula for setup quantity on material rows.
- You can choose if the result of formulas should add, multiply, or replace the regular value.
- No list of functions is shown in the formula editor, instead the available variables and functions are easy found by pressing Ctrl + space.
- The formula editor has a built-in "IntelliSense" which suggests variables and functions as you type.
- Instruction for configuration (IC) has changed name to Configured instruction (CI).
- It is possible to use variables directly in CI without first having to create a formula number.
- CI is also copied if you select Save as on an existing configuration group to a new configuration group.

#### Option lists
- All option lists are general and can be reused.
- Selection group types don't exist, they have been replaced by Minimum number of options and Maximum number of options. If the Minimum number of options is 0 or empty, this means an unrestricted option list. If the Minimum number of options is 1 or higher, this means it is a mandatory option list.
- You can choose to have Automatic option or not (i.e. manual) also in groups where you must choose at least on option.
- It is possible to define an option list by using a Selection. This replaces the function Optional in G4. It is possible to configure a lot more settings in this selection in G5, such as select the selection of part records by different terms and configure which part columns should be shown
- You can determine which information should be printed for the options separately on sales documents, manufacturing order documents, and purchase order documents.
- The function Additions in G4 is called Sub-rows in G5.
- It is optional if the quantity on the sub-rows should be multiplied with the quantity on the main row or if it should just be added.

#### Variables
- New variable types: Date and Boolean (which gives true or false as result).
- You can decide printout of a variable on documents separately for customer order, manufacturing order, and purchase order.
- You can add a default formula for a variable.
- You can add a comment for a variable which is shown during order registration.

#### Configuration group
- The procedure window is divided in tabs to make it easier to get an overall view.
- There is a new term, Section, which has been added. It is used to divide the order window in pages. In a section you can add both option lists and variables in any optional order.
- Variables can be linked to multiple option lists and in this context they can also select type of calculation.
- You can load variable values from fields in the part register for the options you link to the variable. This way you don't have to register them multiple times in configurations.
-   
A variable can now get its value from other fields: from Standard price, Net weight, Extra fields, Selected quantity, and Setup quantity. If multiple options are selected in an option list it is possible to total, get an average value, or get min. or max. of these values.
- Rules and rule formulas have been merged and all rules are entered in the same place.
- Rules will always get a rule number and it is possible to enter a description for the rule.
- It is possible to create more complex rules since the Boolean operator AND is supported in rule definitions.
- You can create rules combining options and variable values.
- It is also possible to copy rules.

#### Configuration templates
- Instead of entering default value in an option list and default values on variables, Configuration templates can be used. A template can contain both variable values and options.
- It is also possible to copy configuration templates.

#### Configuration window (order/quote)
- The quantity from the order row can be edited in the window and you can use it in the calculation.
- Options and variables are shown in a Guide with one page per section.
- Instructions for the configuration group, the option lists and the options are shown in a box.
- The result is shown in a separate tab.
- You can run calculation and lead time calculation in the configuration window without closing it.
- You can configure by copying from a template or from a previously configured order/quote.
- It is possible to save the current configuration as a template, even if it is not complete.
- A configuration for an order will not become invalid due to changed configuration group after order registration. This is prevented by the order using a "snapshot" of the configuration group which is never changed.
- You can synchronize an order with the most recent version (snapshot) of the configuration group if you want these changes to take affect.

#### Not implemented in G5
- There is no Change part function with which you can replace a part in all option lists.
- There is not yet a list for Sales Statistics - Configuration.
