### 回退值
有关回退值的设置应用于新的组件的导入。在否列的案件下使用回退值 组件模板 在导入文件和已选择格式模板中。如果在导入文件和格式模板中已选择了组件模板，则该模板中的值将覆盖低于的回退值。

#### 组件类型
在这里，你可以确定导入之后应将哪种组件类型已分配给新的组件。

#### 组件状态
一个组件有七种不同的状态。这些反映了部件的生命周期（以及未激活组件的附加状态），低于表格的状态阶段所示：
| 象征 | 代码 | 名称 |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeFictitious.png) | 1 | 报价 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypePrototype.png) | 2 | 样品 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/green_dot.png) | 3 | 新组件 |
|   | 4 | 正常的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeUpgrade.png) | 5 | 新版本 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDowngrade.png) | 6 | 逐步淘汰 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDeleted.png) | 9 | 过时的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/RedPadlock.png) | 99 | 未激活 |
不同组件状态是固定的。不添加或删除组件状态。例如，在订单行上显示组件的状态。你可以根据不同列表中的组件状态选择。
将为新建已导入的组件已分配默认组件状态。这然后覆盖系统设置中输入的组件状态 新组件的默认状态。

#### 库存更新
通过此设置，你可以决定是否应已更新新的组件的库存。

#### 组件模板
你可以选择在导入时获取哪个组件模板。但是，模板中的值不自动用于该组件。通过程序 同步组件模板 导入之后，你可以从模板中提供组件值。
