### 国家 / 地区表格
该表格包含根据ISO 3166 的国际的标准化国家 / 地区代码以及世界全部国家 / 地区的名称。国家 / 地区决定了整个系统中许多数据实例，例如，语言、货币以及客户和供应商的地址格式。
为了在某​​些国家 / 地区进行境内的报告，还需要额外的国家 / 地区代码 未知国家(QO)， 未知欧盟国家 (QV)， 和 未知第三方国家（QW）。这些可以用来输入 原产地 为组件.

#### 欧盟
在这里你可以确定该国家 / 地区是否属于欧盟。默认下，此框对于目前被用于欧盟的全部国家 / 地区均处于选中状态。更新系统时，该列还可以已更新新建的欧盟国家 / 地区。订单确保境内的报告正常上班，必须为全部被用于欧盟的国家 / 地区选中此框。

#### 语言
在这里你可以选择该国家 / 地区/地区的选择语言。可选的语言激活​ 语言 程序。

#### 货币
你在此选择该国家 / 地区/地区的货币。可选的的货币货币 货币 程序。对于以以下货币一作为官方货币的国家 / 地区，将默认已选择该货币：SEK、USD、EUR、NOK、DKK 和 GBP。其它国家 / 地区不任何默认货币。如果新客户 / 供应商已登记时邮寄地址所在国家 / 地区不任何默认货币，则已建议本位币。

#### 地址格式
每个国家 / 地区都有一个默认的地址格式。在许多国家 / 地区，通常你像系统地址格式那样多的地址行。如果你这些行空，它们将被隐藏。系统中有五种地址格式：
| 地址格式 | 例子 | 解释 |
|---|---|---|
| 邮编+城市 | [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/address_format_zip_code_city.png)](../../../../Resources/Images/SubProjects/address_format_zip_code_city.png) | 例如，瑞典、挪威、芬兰、丹麦、德语和爱沙尼亚都使用这种格式。 |
| 城市 + 国家 / 地区 + 邮编 | [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/address_format_city_state_region_zip_code.png)](../../../../Resources/Images/SubProjects/address_format_city_state_region_zip_code.png) | 例如，美国、加拿大和澳大利亚都使用这种格式。 |
| 城市+邮编(两行) | [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/address_format_city_zip_code_new_row.png)](../../../../Resources/Images/SubProjects/address_format_city_zip_code_new_row.png) | 例如，美国、加拿大和澳大利亚都使用这种格式。 |
| 城市 / 省+邮编 | [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/address_format_city_province_zip_code.png)](../../../../Resources/Images/SubProjects/address_format_city_province_zip_code.png) | 例如在中国就使用这种格式。 |
| 通用的 | [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/SubProjects/address_format_general.png)](../../../../Resources/Images/SubProjects/address_format_general.png) | 此格式适用于不唯一地址格式的国家 / 地区（例如，否特定的邮编字段）。除了最后行（保留需求 ( - )邮寄地址）之外，你可在此处的全部行输入可选文本。然而，这并不显示在已打印的地址中。 |

#### 客户组
在这里你选择客户组。客户组必须在 过账矩阵 程序。将客户组与国家 / 地区联系起来的目的是让系统基于新客户所属的国家 / 地区自动为其选择客户组。然后，客户组确定订单行的过账，并且通常已登记为国内组、欧盟和导出。

#### 客户VAT 组
在这里你选择VAT 组（可选）。VAT 组必须在 VAT设置 程序。VAT 组表明你与客户和供应商之间的贸易类型（税相关），例如国内、欧盟、导出等等。
按照上述程序，每个VAT 组都与一个VAT 代码相链接。然后，系统将根据已选择的VAT 组自动在订单/发票上建议VAT 代码。为客户和供应商输入VAT 组。但是，VAT 代码可以在订单/发票上已变更。

#### 供应商组
在这里你供应商组。供应商组必须在 过账矩阵 程序。将供应商组与国家 / 地区联系起来的目的是使系统基于新建供应商所属的国家 / 地区自动选择供应商组。然后，供应商组确定订单行上的过账，并且通常会已登记国内组、欧盟和导入等。

#### 供应商 VAT 组
在这里你选择VAT 组（可选）。VAT 组必须在 VAT设置 程序。VAT 组表明你与客户和供应商之间的贸易类型（税相关），例如国内、欧盟、导出等等。
按照上述程序，每个VAT 组都与一个VAT 代码相链接。然后，系统将根据已选择的VAT 组自动在订单/发票上建议VAT 代码。为客户和供应商输入VAT 组。但是，VAT 代码可以在订单/发票上已变更。

#### 激活的
在这里你可以确定该国家 / 地区是否在系统中已激活。全部国家 / 地区默认都处于激活。如果你停用某个国家 / 地区，则系统各个组件的国家 / 地区字段中将不可选的该国家。此检查的目的是能够筛选下班与你不任何业务关系的国家 / 地区。

#### VAT 登记号例外
一些国家 / 地区的VAT 登记号中有其他国家 / 地区代码。例如，希腊的国家 / 地区代码 生长素 但他们使用的VAT 登记号 发光。然后在此字段中你“EL”输入希腊。中的警告功能 EC销售列表 程序检查此例外字段。

#### 地区/次区域/中级地区
在这里，你可以看到根据联合国的规定该国家 / 地区属于哪个地区、次区域和中级地区（如果适用）。
