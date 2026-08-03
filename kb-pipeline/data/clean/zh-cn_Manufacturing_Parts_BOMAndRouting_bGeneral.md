### 通用的
此框包含结构中已选择组件的通用信息 导航 盒子。

#### 组件号
在这里你可以看到组件的组件号。

#### 名称
在这里你可以看到/输入组件的名称。对于新组件，此强制字段。你可以通过单击“挂锁”按钮来编辑现有组件的名称文本 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Padlock.png) 在字段的到右边.你以公司语言输入名称。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 组件类型
在选择你的类型。新组件的默认组件类型为 生产件。在物料BOM 与工艺路线中，你还可以创建采购件和虚拟件。

#### 产品工程师
在这里你选择一位产品工程师，他是负责人该零件的BOM 与工艺路线的员工。你可以从员工记录中选择一个员工。名称显示在到右边字段中。点击 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 查看有关此员工的更多信息。

#### 图纸
在输入你的图号。通过使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 按钮，你可以在表格中添加图纸编号。
对于每个图号，你可以添加图纸版本，并输入其中哪个应为默认版本。点击 版本 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 在图号行上选择要激活的图纸。请保持，字段中显示的是表格顶部行的图号。你应该将“最重要的”图纸或例如汇总图纸放在顶部。

#### 版本
这里你可以看到该组件的版本。通过使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 按钮，你可以在表格中添加组件版本。你可以输入应处于激活的版本、输入版本的应用日期、输入版本评论以及链接文件。
零件的版本版本是使用备选BOM与工艺路线时可以加工工序行和物料行已选择的术语。

#### 状态
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
新的组件将获得默认组件状态，该状态由系统设置决定 新组件的默认状态。
零件状态是使用备选BOM与工艺路线时可加工工序行和物料行已选择的术语。

#### 余额
你可以在这里看到你所在仓库的零件组件总余额。
该部分的默认单位显示在余额字段的到右边。BOM 与工艺路线总是在该单位中已创建。这个单位与余额不同，是全部仓库共同的。

#### 评论
你可以在这里输入/查看生产评论。这与你可以在 生产 标签页卡中的 组件登记 程序。此评论将被已打印在工单文档上。
单击此按钮，你访问文本编辑器，你可以在其中编写和格式文本、插入图像和签名以及超链接等。当有评论/文本时，按钮上的符号将从空的气泡更改 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_no_comment.png) 到已填满的对话泡泡 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。

#### 文件
在这里你可以看到与该组件链接的文件。这些将与工单文档一起已打印。这些文件也可以已链接到 生产 标签页卡中的 组件登记 程序。
支持直接查看 PDF 文件。使用扩展文件阅读器可选功能，您可以查看/显示更多的文件类型，例如不同的图纸格式和Office格式。通过单击此链接，您可以访问[支持文件格式](https://www.rasterex.com/file-formats?hsCtaTracking=f7142bf7-4cfa-4c3b-8be8-cde24df7f2b4%7Cdae7ecbb-26b0-43cd-b9d0-3579248ec31b)的完整列表。

#### 计算加成
在此按钮下，你可以选择该组件的通用计算加价或选择例外。这些必须第一个在 计算加成 程序。对于采购件的组件， 仓储费用加成字段是仅可用的字段。对于生产件，有外协成本加成、销售管理费用和利润字段。对于虚拟件，否可用计算加价。默认已选择通用计算加价。
计算加成的例外可以是外协成本加成、 仓储费用或两者。

#### 标准成本计算日期
你可以在此处看到已保存标准成本的日期。使用按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_link.png)，你可以打开然后进行的计算。

#### 净重
在此列你可以看到零件的净重。通过使用 计算重量 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_calculate.png) 重量可以已计算为所合并物料行的净值合计。也可以时间对列表中的多个组件进行重量计算 计算重量 程序。

#### 固定重量
通过激活此设置，你决定零件的净重应固定，并且重新计算不自动默认已保存在 计算重量 程序。例如，对于由原材料加工而成的为组件，如果已完成重量低于总物料的重量，则使用固定重量。对于这些组件，你人工的输入净重，并且它不在下一个计算时被覆盖。
然而，组件 固定重量 已激活后，可以计算重量并将其保存在此处或 计算重量 程序。

#### 筛选器条款
点击 筛选器条款 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以为组件中包含的工序和物料所已选择的条款配置一个筛选。你还可以选择是否应已激活筛选，并且你选择应激活筛选的哪些组件。你可以根据可用于选择的不同条款筛选，以选择工序和物料。
当筛选已激活时，全部不筛选的工序行和物料行将被隐藏。如果你仅查看特定期限内涉及的工序和物料，此功能很有用。在计算零件的净重时它也很有用，因为仅在筛选已激活时显示的物料行才会被用于在计算中。
