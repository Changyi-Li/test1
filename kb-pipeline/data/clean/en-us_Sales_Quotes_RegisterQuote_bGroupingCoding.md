### Grouping/Posting

#### Seller
The responsible seller. The seller selected for the customer is loaded by default, but this can be changed for the current order. By using the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see information about the selected seller. You can also open the chat function called Monitor chat by clicking the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonChat.png) button. There you can send chat messages to the seller. To be able to use the Monitor chat, the logged in user has to be linked to an employee.
By entering a seller for the quote, you create statistics for the seller. The seller will also be available as a selection term in different lists.

#### Quote category
Here you can enter a category for the quote. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.
Quote categories can for example be of help when you want to get statistics from the quote register.

#### Customer group
Here you enter the customer group to which the quote belongs. The customer group selected for the customer is loaded by default, or alternatively, the customer group for the selected delivery address. However, you can change customer group for the quote in question. Customer group together with the order type's posting group, determine the posting on quote rows. The customer group is handled in the Posting matrix procedure.

#### VAT group
Here you see/enter the VAT group to which the quote belongs. The VAT group selected for the customer is loaded by default, or alternatively, the VAT group for the selected delivery address. However, you can change VAT group for the quote in question. The VAT group determines which VAT code that by default is used on the quote rows. This is registered in the VAT settings procedure.

#### Project
Here you can select a project to which the quote should be linked. Project is used for postings in the system.
If you do not have a project to link to the order/quote, you can create a new project here to link to the order/quote. With the Create project button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add.png) you open a dialog where you enter information about the new project as described below.
When you click the OK button in the dialog, the project is created and in the Project field on the order, the project number for the new project will be inserted. Information from the customer order/quote is loaded to the project (for example, seller, reference information and customer order information). If the Open project checkbox was marked, the project will also open in the Project register procedure.

#### Project number
The project number suggested here is the same as the order/quote number, if the order is saved. If the order is not saved, you can instead enter a project number. If you leave this field empty, a project number will be loaded from the number series for project.

#### Name
It is mandatory to enter a name of the project.

#### Project type
You can selected among the project types registered in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure.

#### Copy internal/external comment
It is possible to copy internal and/or external comments that have been registered for the customer order/quote. These are then copied to the corresponding internal and external comment for the project.

#### Update rows
With this checkbox you decide if the order rows should also be updated with the created project number. If a project number already exists on the rows, this will now be overwritten. This applies to all posting rows (for sales account, setup, COGS, stock). Posting rows that do not handle projects, will not become updated.

#### Open project
With this checkbox you decide if the procedure Project register should open with the project loaded when you click the OK button to create the project.

#### Discounts
Under the Discounts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see which discounts can be applied the quote, customer order, or invoice basis.
You can change the discount rate for Discount (code 1) and General project discount (code 4). If you change the discount rate, the part or project specific discount will be overwritten.
Here you can decide whether a discount code should be applied or not to the order.
You can change the priority for Discount on discount and Project discount. This determines the order in which the discount should be deducted from the price each. In the Register discount procedure, you can change the priority for these two discounts.
It is not possible to make changes for Order discount (code 2) or for Total row’s discount (code 3). Changes to these discounts can only be made under the Rows tab.

#### Priority
The priority of quotes can be 1 to 9, where 1 is the highest priority. By default, you will see the priority that is the highest, either the customer's priority or the order type's priority. Priority is mandatory to enter on the quote.
