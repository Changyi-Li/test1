### Pre-calculation
The pre-calculation should be run on all manufactured parts (and fictitious parts, if any). The main purpose is to:
- Calculate a planned manufacturing cost, which will be saved to the part's standard price.
- Calculate a throughput time or lead time for the parts.
Other purposes:
- To calculate a quote price or sales price, or a cost price.
Pre-calculation is used to make a calculation for an individual part or a selection of parts.

#### The Selection tab
Here you configure settings for the pre-calculation.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Precalculation1.png)](../../../../Resources/Images/TrainingMaterial/Precalculation1.png)
List types
- New calculation – This list type means new pre-calculations for the parts you select to the list. You can then save the result of the calculation to the parts. See below which settings that affect the calculation.
- Existing calculation – This list type means you can see already saved pre-calculations for the parts. No calculation or update is made. See below which settings you can configure for existing calculations.
- Calculate alloy cost – This list type allows you to calculate alloy costs based on the product structures. Alloy costs are aggregated and saved on the main parts in the same way as when a new calculation is made.
Selection
Here you select which part or parts should be included in the List for calculation.
Settings
If you select the list type New calculation you can make different settings regarding price types and costs for material and operations, SO mark-up, Sales OH, and profit mark-up. These affect the result of the calculation. You can also select different settings regarding saving calculated quantity and cost/quote price to a price type for the parts. You find the description of these settings in the topic under the help section [The New calculation list](../../../Manufacturing/Calculations/PreCalculation/tListNewCalculation.htm).
If you select the list type Existing calculation you can make price comparisons and choose to save cost/quote price to a price type for the parts. You find the description of these settings in the topic under the help section [The Existing calculation list](../../../Manufacturing/Calculations/PreCalculation/tListExistingCalculation.htm).
If you select the list type Calculated alloy cost you can choose if all parts should have the checkbox "Include" pre-selected when you open the list, otherwise you manually have to choose the parts.
> Save the settings to be used in your company by using the function Default values in the backstage of the procedure.

#### The List tab
The List tab opens after you have clicked the button Load ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) on the toolbar. In the list you see all selected parts.
If the list type New calculation is selected, you can in this list check and adjust quantity and uncheck parts that should not be included in the calculation. You start the calculation using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar. If you under the Saving heading under the Selection tab selected a price alternative to save to, then it is possible to after the calculation, deselect parts for which you do not want to save a new price. If you for example chose the Stock driven M-parts option for setting Recalculate, these will be shown after the calculation. Then you will for example see new prices and warnings, if any, for these parts.
If the Existing calculation list type is selected, you can in the list see all calculations previously saved for the parts. If you under Saving have chosen cost/quote price to save to a price type on the parts, you can then in the list mark to which calculations you wish to save new price.
If the list type called Calculate alloy cost was selected, you can in the list deselect parts which should not be included in the calculation of alloy cost. You start the calculation using the same button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar.

#### Other tabs
The other tabs in the procedure becomes available after you have started new calculation, calculation of alloy costs, or if you loaded existing calculations. These tabs show a summary of the calculation, detailed information about direct material and included order oriented/stock driven manufacturing parts, operations, and a level list. Warnings which occurred during a new calculation are also shown, if any. For existing calculations the corresponding information is shown (except for warnings) and you will also see information about settings for price comparison under a separate tab. For calculation of alloy costs you will only see a summary for each part. You find the description of these tabs in the help section Post-calculation [Pre-calculation](../../../Manufacturing/Calculations/PreCalculation/wPreCalculation.htm).
