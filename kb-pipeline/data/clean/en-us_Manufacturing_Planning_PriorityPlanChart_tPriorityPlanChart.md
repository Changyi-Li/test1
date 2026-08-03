### The Priority plan chart tab
Under this tab you can see the priority plan chart. In the View field you determine which information should be shown in the chart. You decide the scale of the chart in the field below. The operations are shown as blocks. The operations belonging to the same order have the same color marking. If you click on an operation in an order, all operations belonging to that order will be displayed in yellow. A validation will display overlapping operations in the same order, in red.
The work center’s operations are shown on two rows, where the bottom row displays the operations which are not manually planned. You plan an operation in detail by dragging it from the bottom row to the top row. The operation is then assigned Priority 9. The prioritized operations will then be displayed with a green background color in the Priority planning and in the Recording terminal.
Instead of “dragging and dropping” operations to plan them, you can use the button called Modify operation data ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) and mark Scheduled. When needed, you can also enter a different Planned start and Planned finished than the suggested ones.
The time axis is gray if there is time that does not fall under a schedule for that day. If there is schedule time it will be displayed in white. This is shown separately for each work center. In the chart you will see a vertical line representing the time at present. When you reschedule an operation with time for start and finish, you will see lines indicating the beginning and then end of the operation. At the bottom of the window there are buttons you can use to move ahead and back in the chart. In the middle of the button row there is a button which will take you back to the current/present day in the chart.
In the tooltip to the operations you will see additional information. If you have selected to show the Status view, this tooltip will for example say "Not reported" at the bottom if the order is not reported. You can for example see planned quantity, reported quantity, and remaining quantity in the tooltip.
In the chart it is possible for you to change capacity, see if there are any work items in progress in the work center, see what is ready to run based on previous operation and material clearance, see if material has been cleared, and if the previous operation is finished. The lag hours that exist before the start of the chart, are shown under the information button for the work center.
In the function menu in the Priority plan chart you will find the following functions:
- Replan the entire order – With this button you can choose to replan, that is, to reschedule the entire order, when you reschedule an operation.
- Consider simulation factor – With this button the operation time will be shown as 125% (if the simulation factor is 80%, which is the standard value). This makes it harder to overload the say.
- Show setup time – This function provides you with a handy overview of the setup and you can see if anything clashes. For example, two setups should not be planned at the same time if there is only one machine setter.
- Change work center – Using this button you can change the work center for an operation.
- Go to procedure – Using this button you will load the selected operation to the procedure you choose to go to. There you can see additional data regarding the operation and analyze it further.
- Show suggestions – Using this button you will also show manufacturing order suggestions in the priority plan chart.

#### View
With this setting you decide which information should be shown in the tooltips for the blocks.
- Overview – Only shows the overview information about the operations.
- Replanning – Shows if operations are overloaded and thereby need to be replanned.
- Status – Shows the status for the operations (for example "Not reported").
- Comparison with New finish – Shows time comparison regarding new finish (for example "On time" or "Late").

#### Scale
Here you select the scale you want to use in the chart. The options are Hour and Day.
You can also zoom in the chart – 100 to 400 percent – in the lower right corner of the window, regardless of the selected scale. The lead time chart saves the most recently used scale for the next time you open the procedure.
