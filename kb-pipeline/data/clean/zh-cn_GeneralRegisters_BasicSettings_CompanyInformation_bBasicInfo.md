### 基础信息
在此框中你有关公司的基础信息。

#### 公司名称
在输入你银行。

#### 企业 ID 号
在输入你的企业 ID 号。

#### 注册地
这里你输入公司的注册地。

#### 语言
在这里你可以选择使用哪种语言作为公司语言。
当可翻译文本（名称等）在 Monitor ERP 中否用户语言的翻译时，将使用公司语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 货币
在这里你选择公司会计以及组件标准价格中使用的本位币。应用至货币​​ 仓库 用来。货币名称以用户的语言显示。通过使用 变更货币 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_record.png)，你可以更改本位币。
> 请注意！ 你应该只在空数据库中仅更改本位币。现有的数据将不转换为新公司货币。

#### GS1 公司前缀
你在此处输入GS1 标准组织针对公司所在地区或业务线已分配的唯一公司前缀。公司前缀是六至九位数字的组合。GS1 公司前缀用于为公司销售的为组件创建唯一的 GTIN 编号。公司前缀位于为组件GTIN编号的开头。
下一个是 GS1 代码 字段，在销售标签页下 组件登记 程序，你查询一个用来为组件生成唯一 GTIN 号码的功能。如果使用此功能，并且公司由七到九位数字的公司前缀组成，然后在此字段中输入公司前缀的第一个六位数字。数字七至九被输入到编号序列中 GS1 代码，在库存标签页下 编号序列 程序。编号序列必须以公司前缀的剩余数字加上流水号的若干编号零开始。该编号序列合计应由六位数字（千）组成。
当组件登记中生成 GTIN13编号时，公司前缀中的六位数字然后与从编号序列中加载的六位编号放在一起。然后已添加一个控制数字。全部， GTIN13编号组成13位数字组成。你还可以在字段中计算检查数字 GTIN-13 在页上 [https://gs1.se/en/standards-and-services/check-digit-calculator/](https://www.gs1.se/Support/Berakna-kontrollsiffra/)。
如果不使用GS1 公司前缀，你将该字段空。

#### 银行账号
在选择你的默认银行账号。你已登记选择在 银行设置 程序。

#### 我方合作伙伴代码
“我方合作伙伴代码”用于在采购订单和交货日程表的EDI导出文件中识别公司。你也可以在公司的备选交货地址中输入“我方合作伙伴代码”。

#### EORI 号
在输入你的EORI 号（经济操作员登记和识别号）。你可以使用EORI 号来处理欧盟境内全部与海关相关的业务。在里面 文档模板 程序你在文档部件页脚中添加EORI 号。
您可以根据欧盟佣金可用的数据库来验证您输入的EORI 号。点击 EORI 号无效 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 然后 验证 EORI 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_validate.png)。在你验证了EORI 号后，有关该公司的信息将加载到窗口中，你可以查看EORI 号或不有效。按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 将更已变更 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) 如果EORI 号有效。无论EORI 号或不有效，你都可以在按钮的工具提示中看到该编号最近的验证时间及验证者。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/EORI_validation_valid.png)](../../../../Resources/Images/SubProjects/EORI_validation_valid.png) [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/EORI_validation_invalid.png)](../../../../Resources/Images/SubProjects/EORI_validation_invalid.png)
