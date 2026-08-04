### Requirements planning – different planning methods
There are different ways to perform requirements planning. The basics in the requirements planning can be described as three different methods. By dividing it in three methods, it is easier to learn and to gain understanding of how the system works. These three are described in short below and are described in detail further down.
1. Work method – Part register – For an individual part you open a planning window in order to analyze your requirements and discover shortages. This is the decision basis for manual registration of manufacturing and purchase orders. This is called the manual method. This method is also used together with the other methods.
2. Work method – Requirement calculation – This is used in order to analyze the requirements for various parts that have been selected. Here there is an option to only view parts that have a shortage. In addition, order suggestions can be provided for automatic generation of actual orders. This works is performed per level throughout the structure. This method is called the semi-automatic method.
3. Work method – Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. – Works its way through all levels during one and the same run/calculation. After the run/calculation, order suggestions are shown in separate suggestion lists. The net requirement calculation generates order suggestions without displaying "why". This method is called the automatic method.
The choice of method often depends on which of the basic prerequisites currently exist in the system, as well as the required level of automation. If you will perform requirements planning often, using many parts and a large quantity of registered orders, then you often need a higher level of automation than if you have few parts and few orders.
> The demands regarding basic data, correct order backlogs, and stock balances increase as the level of automation increases. See the image below.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/RequirementsPlanningLevels.png)](../../../../Resources/Images/UserGuide/RequirementsPlanningLevels.png)
Work method – Part register
1. Open the Part register (F12) to see shortages in the planning window.
2. If shortages are discovered, you can register the orders manually or you can release order suggestions, if any, from the requirements calculation (for the loaded part) which you can run.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PartRegisterPlanningWindow.png)](../../../../Resources/Images/UserGuide/PartRegisterPlanningWindow.png)
Click the button Requirement calculation to see the rows which are requirement calculated. You can then see the finish date and the requirement date. Click on the same button again to exist that mode.
Work method – Requirement calculation
1. Open the procedure Requirement calculation, select a range of parts and select settings for the list.
2. Load the list. If there are parts with shortages, you will see the shortage balance in red in the Available balanceAvailable balance is the current part balance on the locations minus the cleared quantity. column.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/RequirementCalculation.png)](../../../../Resources/Images/UserGuide/RequirementCalculation.png)
You can here click a part to see a more detailed planning window in the lower part of the window.
You can turn the suggestion into an order directly in the planning window. Re-scheduling suggestions can also be executed here.
Once the actual orders have been registered, a new requirement calculation can be run in order to check which shortages these orders might have created. You repeat these steps until there are no more shortages/suggestions left.
Work method – Net requirement calculation
1. Open the Net requirement calculation procedure and select the range of parts you want to do a net requirement calculation for.
2. Schedule the net requirement calculation and when needed, you can activate continuous net requirement calculation and configure intervals for the running of it. See more information about scheduling below.
3. Save in the procedure. Then the selection you made will be saved and also the scheduling.
> In the Net requirement calculation you save a selection using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) in the procedure, not as a "default value" as in other list procedures.
Scheduling
You schedule two different types of net requirement calculations:
- Net requirement calculation – A net requirement calculation is made for all the selected parts. The calculation finds shortages and creates suggestions for manufacturing and purchases of material. You schedule which days and what time the calculation should run.
- Continuous net requirement calculation – The continuous net requirement calculation only goes through the parts which have been modified since the last total net requirement calculation and the last continuous calculation. This type of calculation is much faster to run than the above mentioned type. You can schedule continuous calculations in intervals. The intervals are entered in number of minutes.
Get different types of suggestions
You can get different types of suggestions after running the requirement calculation and net requirement calculation:
1. Suggestion – Manufacturing order – You get this if there is a shortage of a manufactured part.
2. Suggestion – Purchase order – You get this if there is a shortage of a purchased part.
3. Rescheduling – In – Instead of registering a new order, you can get suggestions to reschedule an existing order, and plan to do it earlier than intended. The suggestion means that you can change the date of an existing purchase or manufacturing order.
4. Rescheduling – Out – Reschedule an existing order since the requirement occurs later.
5. Unnecessary order – There is no requirement for this order.
6. Suggestion – Stock order – You get this suggestion if there is a shortage of a purchased or manufactured part and that part has a selected warehouse with the setting Refill from warehouse. This suggestion type is available if the option Warehouse is installed.
The image below shows the difference between requirement calculation and net requirement calculation:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/RequirementsPlanningMethods.png)](../../../../Resources/Images/UserGuide/RequirementsPlanningMethods.png)
> Monitor tip! Enter a fixed delivery day for the supplier in the field Delivery days in the Supplier register procedure. This way the purchase order suggestions will be set to that weekday. You can change supplier for a suggestion, from the active supplier to an alternative supplier. Use the Planning list in the Part list procedure, to update the planning information which exists under the Planning tab in the Part register procedure. Under the Manufacturing tab in the Part register, there is a button called Material enough for. There you can see how many items you can manufacture of the part with the balance of incorporated materials.
