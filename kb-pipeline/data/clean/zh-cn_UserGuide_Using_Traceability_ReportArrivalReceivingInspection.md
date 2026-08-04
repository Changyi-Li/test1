### 报告到货/到货质检
> 如果 到货质检 已为供应商、组件或订单行已激活，应在 到货质检 程序，与非 报告到货 程序。如果订单行已激活了到货质检，则整个 库位 邮箱将被未激活。你激活通过勾选到货质检订单行中的 质检 复选框。

#### 批次层级可追溯性
当到货报告组件采购件且具有可追溯性时 批次 层级，你可以在库位中输入批次号 库位 标记订单行的框。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ReportArrivalBatch.png)](../../../../Resources/Images/TrainingMaterial/ReportArrivalBatch.png)
默认下，该库位的已建议批次号为“采购订单号-位置号”，其它设置可以在 编号序列 程序。但是，你总是可以输入任意批次号。
如果设置 应用"此前最佳" 已已激活该组件，你将看到 此前最佳 在库位列输入已建议的日期，或者，根据组件的设置，强制的输入日期。你输入每的批次此前最佳。
你还可以输入 费用号 并链接文件 认证 到达 与到货报告连接的库位.同批次可以已添加到多个库位，多个批次也可以共享同一个库位。
当到货报告具有批次层级可追溯性的组件到货时，不强制的选择一个新建的库位来报告批次号。如果需要，你可以应用系统设置，在已报告到货创建时间新建库位，并自动命名新位置并赋予已建议的批次号。

#### 序列号层级的序列号的可追溯性
报告具有可追溯性级别的组件到货时 序列号，必须在库位必须输入序列号和数量。这是根据 序列号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 按钮 库位 为已选择的订单行方框。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ReportArrivalSerial.png)](../../../../Resources/Images/TrainingMaterial/ReportArrivalSerial.png)
为了快速连续报告多个序列号，可以已报告一或更多间隔。在​ 从 列，以及 数量，序列号将被设置，最终序列号显示在 到 列。
要输入不连续的序列号，你只需每序列号添加一个新行。A 前缀 可以输入间隔内的全部序列号。你还可以输入 费用号 并链接文件 认证 与到货报告连接的每个序列号间隔。也可以从包含序列号的文本文件已导入序列号。这是通过 导入序列号 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_import.png)。
在序列号的可追溯性层级应用可追溯性时，默认批次号仍然存在（就像在批次层级使用可追溯性时一样），并且可以已变更。你还可以输入库位的费用号，并将认证链接文件到这些号码。
对于采购件追溯至 序列号 (仅领用) 层级，你不在到货报告时输入任何序列号。在此阶段，对它们的处理方式与不可追溯性的组件相同。
