### BOM and routing
As mentioned earlier, you can in BOM and routing link the part to a configuration group, choose if the configuration window should open automatically, and select template.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfiguratorBOMAndRouting.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorBOMAndRouting.png)
In BOM and routing you can also use the following functions on all parts in your configuration group. That is, both on the main part and also for all included/incorporated order oriented manufactured parts and also for fictitious parts, regardless if they become included on the order via the basic BOM and routing or via options.
- For operations you can use formulas to calculate unit time and setup time, and you can create configured instructions.
- For material rows you can calculate quantity and setup quantity and here as well you can create configured instructions.
- The configurator can create unique variant codes which makes it possible for you to use terms based on variant code both for operations and material.

#### Configured instructions
Operations and material (and options in option lists) can have configured instructions. In a configured instruction you can combine static texts and images with values on variables and values from calculations in formulas you created in the configured instruction.
The CI button on operation and material rows opens the window Configured instruction.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfiguredInstruction.png)](../../../../Resources/Images/TrainingMaterial/ConfiguredInstruction.png)
In the Instructions section to the left in the window you add variants of the instruction and link each variant to one or more configuration groups. Each variant will be given a consecutive number. The first variant starts on 1001.
In the section called Variables in the bottom right corner you see the variables available in the configuration groups.
In the section called Formulas in the to right corner you can add formulas, and with the help of available variables you can calculate values and give them formula names.
In the middle section called Instruction, you write the actual instruction. Both variables and formulas can be added anywhere in the instruction using the drag and drop function. An alternative is to manually enter variables and formulas in the instruction as [v:variable code] and [f:formula name]. Validations are made to make sure the entered variables and formulas are available.
In the image above they are highlighted in green in the instruction, but this is only to them clearly. Of course you can format both text, variables, and formulas, in instructions as you want.
You can at any time test the outcome of the entire instruction by using the button Preview instruction ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) next to the instruction.
When you are done you should save the configured instruction with the OK button.
> Tip! The procedure Simulate manufacturing order is a good tool to test a configuration group. In that procedure you can easily see if material and operations have been created in the way you wanted them. If you want to test the design of documents and see that configured instructions are correct, it is in most cases best to create test orders in the procedure Register customer order and create a manufacturing order from the customer order. You can activate From manufacturing order in the system setting Transfer info from causing requirement to purchase order. This means that instructions (which you might have determined with the configurator) are transferred from material rows on manufacturing order to the purchase which should supply the row. (Support to transfer info from causing requirement to purchase order From customer order will be added later on.)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfiguratorSystemSettings2.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorSystemSettings2.png)
