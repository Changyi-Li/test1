### 准备工作
在这里你可以阅读在开始你出口代理之前需要进行哪些已配置。

#### 导出 / 导入设置
你可以在以下位置查询出口代理的设置 导出 标签页下的导出类型 托收保付。要配置的设置取决于银行使用由的格式。在中间格式的设置可能有所不同，例如，客户登记应已导出为单独的文件，或者你必须选择在托收保付公司你的服务。应用至全部银行格式的一件事是，你必须选择路径目录路径和用于导出的文件名称。
目前支持“ 商业银行 格式 ”（应用至瑞典）、“瑞典银行支付”（应用至瑞典）、“北欧银行 财务”（应用至挪威）、“ DNB ”（应用至挪威）、“ Sparebank1 ”（应用至挪威）、“北欧银行 财务”（应用至芬兰）和“ Peppol BIS 3.0”格式。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/Factoring1.png)](../../../../Resources/Images/TrainingMaterial/Factoring1.png)
阅读更多有关设置的更多信息 在本章节中[银行特定设置](BankSpecificDetails.htm)。

#### 银行设置
在此程序中，你需要登记托收保付公司的银行账号信息，并输入您（公司）在托收保付公司使用的客户编号。你还可以在此处配置设置，以使不同文档（发票等）页脚中的银行信息基于预期货币，以及是否用于客户使用托收保付。
银行账号标签页
在此标签页下，你登记托收保付公司的科目及其帐号等信息。对于某些托收保付公司，科目你需要登记多于一。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/factoring2.png)](../../../../Resources/Images/TrainingMaterial/factoring2.png)
文档信息标签页
在此标签页下，你配置设置，以使不同文档（发票等）页脚中的银行信息基于预期的货币。如果该客户应用了托收保付，你还输入要在文档页脚中显示的科目信息。
客户编号
如果导出文件中强制的包含客户编号，行你至少总是输入一本位币，并链接至您自己的银行账号和托收保付公司的银行账号，以及银行的客户编号。
如果你已登记了多个货币作为托收保付信息，然后只需在引用本位币的行中输入客户编号即可。
对于某些出口，银行要求你为每货币提供不同的客户端编号。在这种案件下，你必须为每个货币登记一，并且你在最右边的列中输入该货币的客户编号。
在低于的例如中，该公司在银行有多个不同外币科目，这就是为什么要为每个货币输入单独的银行账号和托收保付科目。然而，例如中的银行不要求根据货币提供不同的客户端编号，因此你仅在本位币行中输入该信息。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/factoring3.png)](../../../../Resources/Images/TrainingMaterial/factoring3.png)

#### 客户列表
为了能够导出托收保付，你需要为每个客户激活设置 托收保付。这是在 标准 列表格式 其它的。更新​​ 托收保付 每个行的列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/factoring4.png)](../../../../Resources/Images/TrainingMaterial/factoring4.png)
> 使用 查询 & 替换 时间为多个客户更新列。
