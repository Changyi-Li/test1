### 付款
在此框中你输入有关应付应付账款中付款的信息。

#### 付款方式
在这里你可以选择向相关供应商付款时应使用的付款方式。你可以在已登记的付款方式在中间选择 银行设置 程序。你可以在那里编辑和/或添加付款方式。此强制字段，不能为空。

#### 支付由
如果要通过其他供应商付款，你可以在此处输入另一个供应商号。默认下，此字段将包含与主行相同的供应商号，但可以已变更。如果已发送发票的供应商已将发票交给财务公司（例如北欧银行 Finans、Klarna），这将很有用。这要求你在供应商登记中将财务公司已登记为单独的供应商。

#### 联系人编号
如果供应商有固定联系人号，则检查此框，该编号用于在供应商发票中登记 登记供应商发票 程序。对于对联系人编号有官方处理的国家 / 地区，字段中内置有校验，如果你输入了无效的编号，则会出现校验错误。
Bank accounts
By using the Bank accounts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) you can register one or multiple bank accounts.To the left you can see the accounts you register, and there you can also select which one you wish to use by default.To the right you fill in information for the respective account according to the following.

#### Bank account type
Here you select which type of account that is being registered.You can choose between IBAN, BBAN, UPIC, and Other.

#### Account number/IBAN
Here you enter the bank account number or IBAN, using a maximum of 50 characters.

#### SWIFT/BIC
Here you enter the bank’s BIC or SWIFT code, using a maximum of 20 characters.

#### Clearing number/Routing number
Here you enter the bank’s clearing number or routing number (not used together with IBAN), using a maximum of 20 characters.

#### Clearing system/Bank code
Here you enter the bank’s clearing system or bank code (not used together with IBAN), using a maximum of 20 characters.

#### Currency
Here you link the bank account to a currency.The currency used by default is the same as the currency in the Export box, but this can be changed.The bank account is primarily suggested based on the currency of the invoice.If the there are several bank accounts in the same currency as the invoice, then the bank account that is set as default will be suggested.

#### Recipient’s country
The recipient’s country is by default the same country as is used in the mailing address, but this can be changed.

#### Country
In this field you enter the country where the bank is situated.By default you will here see the same country as in the mailing address, but this can be changed.The selected country affects the address format that will be applied.If you select a country that does not have a specific address format, a general address format will be applied.You link countries to address formats in the Countries procedure.If you change the country code, the address format will also be changed.
Settings for address
To the right of the Country field you find the Settings for address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_settings.png) where you can see and add more information that is linked to the bank's country.By clicking the button, a window called Settings for address opens with the fields Language and Document group will appear.In the window you can also see the address format that applies for the selected country.At the bottom of the window you can preview the address according to the address format.

#### Language
The language you select here is the language that will be used in documents to the bank.The language is filled in automatically when you select the country.The field can be edited and you can select any language.This can e.g. be useful when dealing with countries where more than one language is commonly used.By using the Lookup function, you can select among the languages registered as active in the Language procedure.

#### Document group
In this field you select a document group which determines the document group that will be used by default in documents to the bank.The document group is based on the selected language and is linked to the language in the Languages procedure.

#### Address format
This is an information field displaying the format applied for the selected country.This field is not possible to edit.

#### Preview
Here you can see a preview of the entered address in the address format of the selected country.
通过使用按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_show_in_google_maps.png)，您可以找到并查看输入的地址在 Google 地图中的位置。

#### Name
Here you enter the name of the bank.

#### Address
Enter the street address or post office box number of the bank.

#### Zip code
Here you enter the zip code of the bank.If there are zip code tables registered for the country in question in the Zip code register procedure, you can select a zip code by using the Lookup feature.

#### City
Here you enter the city where the bank is situated.This field is automatically filled in if the corresponding information has been entered for the country’s zip codes in the Zip code register procedure.
The City field is available for the following address formats:
- Zip code + City
- City, Zip code (two rows)
- City + State/Region + Zip code.

#### State/Region
Here you enter the state or the region of the bank.This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.
The field State/Region is available in the address format City + State/Region + Zip code.This address format is used e.g. in the U.S.

#### City/Province
Here you enter the city or province for the bank.This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.
The field State/Province is available in the address format City/Province + Zip code.This address format is used e.g. in China.
导出设置
点击按钮 导出设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你选择你使用的导出格式以及是否你对供应商使用任何例外。

#### 导出格式
在这里你可以决定应该使用哪种导出格式。你可以选择的格式是银行激活标签页下已激活的格式 银行设置 程序。对于导出类型 付款文件 你配置设置​ 导出 / 导入设置 程序。
如果已选择 付款方式 供应商与 付款格式 在里面 银行设置 程序，然后这里就会默认设置这种格式。

#### 例外
不应用至导出格式 供应商付款LB， 北欧银行， 和 电子支付 Netbox, Nordea, FI。通过设置，你可以为该供应商设置已选导出格式用于的默认代码的例外。例如，供应商可能有不同的付款格式或付款方式。
对于Danske 银行（瑞典）和北欧银行（付款），你可以通过例外 使用批量付款 设置。
