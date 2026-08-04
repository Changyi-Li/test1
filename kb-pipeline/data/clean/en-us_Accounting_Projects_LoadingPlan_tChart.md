### The Chart tab
The tab is divided into three different sections. To the left there is a section containing [settings](bSettings.htm) that can be configured for the chart. To the right you see the actual chart and at the bottom of the window there is a total.

#### The chart
When you have loaded the information the chart will be shown for the day/week/month, depending on which time scale you have selected. The first bar in the chart is the period preceding the current period. Following it you will see the current period. And this is followed by 9 more bars representing nine days/weeks/months ahead in time. That is, a total of 11 bars are displayed in the chart. It is also possible to move one or 10 bars at a time, back or forward. You can also move to the first respectively last bar on the time axis. However, to be able to move back to the earliest order, there must be a lag.
Today's date is marked with a red vertical line on the time axis.
In the chart you will see the capacity as a line and the loading as bars. If you under the Selection tab have chosen to section the loading, these sections are displayed in separate colors in the loading bar. When you move the cursor over a bar, regardless of section or color, you will see summarized information about the capacity and loading for that particular bar. If you click the section you are pointing, the focus will also be moved to the current row in the Total section.

#### Navigation buttons
You find the following buttons under the chart/list which you can use to navigate:
- First period with loading ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_first.png) – This button takes you back in time to the first period in the chart/list where loading exists.
- Ten periods back in time ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_backward.png) – This button takes you back ten periods in time from today's period. You can then use the button again to go another ten periods back in time.
- One period back in time ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_previous.png) – This button moves the focus back one period at a time.
- Today ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_today.png) – Click this button in order to return to the red line that marks today’s date on the time axis.
- One period ahead ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_next.png) – This button moves the focus ahead, one period at a time.
- Ten periods ahead in time ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_forward_10.png) – This button takes you ten periods ahead in time from today's period. You can then use the button again to go another ten periods ahead in time.
- Last period with loading ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_last.png) – This button takes you ahead in time to the last period in the chart/list where loading exists.
Under the row of navigation buttons there is also a split function that can be used to change the size of the sections in the procedure window with the cursor.

#### Total
In the table under the chart/list you will see total loading information for each day/week/month, depending on your configured settings. The total follows the periods displayed above in the chart/list.
The values that are always shown, regardless of other settings, are Capacity (%), Total loading (hrs), Difference per period (hrs), Load (%) and Accumulated difference (hrs).
Under Capacity, you can see one row for each data type that you have chosen to section by. If you, for example, have chosen to section by project, one row per project that you have chosen/selected is shown. You will only see rows for what is displayed in the loading chart. If you, for example, chose not to display the loading for project X, it means that you will also not see a row for that project. If you choose to use sectioning, one color is displayed as the background color for each data type (the same color as in the bars). If you selected None for the sectioning, the colorful row will not be displayed but only the total loading along with the capacity.
Difference refers to the difference between the Capacity and Total loading. The Load (%) is the percentage of the capacity that is occupied (loading divided by capacity). The Accumulated diff. (hrs) shows the difference in number of hours between the capacity and the loading (taking previous periods into consideration).
Directly above this table you can see Total lag (loading in the past) and Total horizon (loading in the flexible future). The totals that are displayed here also include loading outside the period of time (11 periods), and therefore, they are not displayed as separate columns in the chart.
