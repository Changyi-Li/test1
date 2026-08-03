### Show

#### Sectioning
Here you choose if and how you want to section the loading information in the chart/list. The alternatives that you can choose between are None, Loading types, and Work centers. The sectioning shows each loading type or each work center as a separate row and color in the total under the heading Loading information. This color is also used on the bars in the chart to show each respective type/group. None is selected by default. This means that no sectioning is made and the loading chart will display one single color on all bars.

#### Type of time scale
Here you select which type of time scale that should be used in the chart/list. You can choose between Fixed or Dynamic.
If you select Dynamic, you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to open a table where you can enter how many days, weeks, and months that should be displayed in the loading chart and list. The total of the number of periods must be 10, for example 4 days, 4 weeks, and 2 months. Please note that the first week shown might not contain 5 days of work, since Monday and Tuesday may already be displayed as individual days. The same goes for the first month, meaning it will only contain the days remaining after the last week displayed.

#### Time scale
If you selected Fixed as Type of time scale, you can here determine how the chart’s time axis should be grouped. You can choose between the alternatives Hour, Day, Week, and Month. Week is the most commonly used alternative and is therefore selected by default. The alternative Hour can only be selected if you have activated the system setting Enable hourly planning for work center.

#### Total per work center
With this setting you decide if you want to show data per work center also in the total mode. The None option is selected by default. You can select to show Capacity, Suggestion, Orders, Total loading (hrs), Difference (hrs), Load (%), or Accumulated difference (hrs).

#### Percentage loading
This setting is not checked by default. If you activating this setting, the loading hours will not be displayed in the chart. The bars in the chart will instead be displayed as percentages of the loading divided by capacity. That is, the bars display a loading of 100 % when the loading is the same as the capacity.
By activating this setting, you automatically deactivate the setting Calculate with man-hours.

#### Calculate with man-hours
This setting is not checked by default. If you activating this setting, the remaining setup time will be multiplied by the staffing factor for setup time, and the remaining unit time will be multiplied by the staffing factor for unit time. The staffing factor is entered for the work center, but it can be overridden for a particular manufacturing operation.

#### Accumulated difference including lag
This checkbox is activated by default. It determines if the accumulated difference should include the hours that are lagging or if the difference should be counted from now on.

#### Consider simulation factor
This setting is not checked by default. By activating this setting, the remaining time will be divided by the percentage entered as simulation factor for the work center. If you e.g. have a loading of 100 hours and you have entered 80% as simulation factor, you will get a loading of 125 hours instead. This affects the number of loading hours, but not the positioning of the loading on the time axis.
