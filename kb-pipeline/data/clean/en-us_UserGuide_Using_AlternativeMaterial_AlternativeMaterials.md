## Alternative material

#### Introduction and purpose
Alternative material is a function which makes it possible to define and use alternative parts if a material shortage should occur for a manufacturing order. You can activate this function both for part level and for BOM and routing. The purpose is to provide Production planners with:
- Better control of the situation when material shortages occur.
- A simplification of daily decisions.
- A reduced risk of delays when the primary material is missing.
- The function is intended to solve short-term material shortages and is NOT linked to the net requirement calculation.
Watch the video about alternative material (Only available in English):
| English |
|---|
|   |

#### Basic data (BOM and routing or Part register)
Alternative materials can be defined both on the BOM and routing level and the part level. In the BOM and routing you can add alternative parts directly in the material list.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AlternativeMaterial1.png)
On part level, you configure alternative materials under the Manufacturing tab in the Part register procedure.
> An alternative material entered in the BOM and routing procedure will override any alternative material configured in the Part register, if such has been entered in both procedures.

#### Replanning
When a material shortage occurs, you can change to a predefined alternative material directly on the manufacturing order or in the Priority planning procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AlternativeMaterial2.png)

#### Material clearance
In the Material clearance procedure, there is a section displaying which alternative materials can be used and Monitor ERP will take into consideration if that material will be needed for other orders within the lead time.
You can open a dialog to access more information about the alternative material, for example, disposable balance within lead time.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AlternativeMaterial3.png)
When an alternative material is used, a symbol will be displayed indicating that the material clearance needs to be run again. After this is done, you execute the part replacement/change and the clearance by saving the material clearance.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AlternativeMaterial4.png)

#### Material list and part import
There are lists that can be updated in the Material list procedure and in the Part list procedure, where alternative materials in BOM and routing and the Part register can be handled. You can also import alternative materials to the BOM and routing via the Part import procedure.
