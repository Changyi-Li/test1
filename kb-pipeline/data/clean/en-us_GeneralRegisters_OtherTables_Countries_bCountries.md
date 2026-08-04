### The Countries table
This table contains international standardized country codes according to ISO 3166 and names for all countries in the world. The country determines many instances of data in the entire system, such as, language, currency, and address format for customers and suppliers.
For the purpose of Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reporting in certain countries, there are also the additional country codes Unknown country (QO), Unknown country EU (QV), and Unknown country, third country (QW). These can be used to enter Country of origin for parts.

#### EU
Here you determine if the country belongs to EU. By default, this box is checked for all countries included in EU at the moment. The column can also be updated with new EU countries when updating the system. This box must be checked for all countries included in EU in order for the Intrastat report to work properly.

#### Language
Here you select language for the country. Selectable languages are the active languages in the Languages procedure.

#### Currency
Here you select currency for the country. Selectable currencies are the currencies registered in the Currencies procedure. The currency is selected by default for countries that have one of the following currencies as official currency SEK, USD, EUR, NOK, DKK, and GBP. Other countries do not have any default currency. If the country of the mailing address does not have any default currency when new customer/supplier is registered, the company currency will be suggested.

#### Address format
Each country has a default address format. In many countries, you normally do not need as many address rows as there are in the system’s address format. If you leave these rows empty, they will be hidden. There are five address formats in the system:
| Address format | Examples | Explanation |
|---|---|---|
| Zip code + City | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/address_format_zip_code_city.png)](../../../../Resources/Images/SubProjects/address_format_zip_code_city.png) | This format is used, e.g., in Sweden, Norway, Finland, Denmark, Germany, and Estonia. |
| City + State/Region + Zip code | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/address_format_city_state_region_zip_code.png)](../../../../Resources/Images/SubProjects/address_format_city_state_region_zip_code.png) | This format is used, e.g., in the USA, Canada, and Australia. |
| City + Zip code (two rows) | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/address_format_city_zip_code_new_row.png)](../../../../Resources/Images/SubProjects/address_format_city_zip_code_new_row.png) | This format is used e.g. in the USA, Canada, and Australia. |
| City/Province + Zip code | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/address_format_city_province_zip_code.png)](../../../../Resources/Images/SubProjects/address_format_city_province_zip_code.png) | This format is used e.g. in China. |
| General | [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/address_format_general.png)](../../../../Resources/Images/SubProjects/address_format_general.png) | This format is intended for countries that do not have a unique address format, e.g., no specific field for zip code. Here you can enter any optional text on all rows, except from the last row which is reserved for the mailing address. However, this is not displayed in the address that is printed. |

#### Customer group
Here you select customer group. The customer groups must be registered in the Posting matrix procedure. The purpose of linking a customer group to a country is to make the system automatically select a customer group for new customers, based on the country to which they belong. The customer group then determines the posting on order rows, and is often registered e.g. with the groups domestic, EU and export.

#### Customer VAT group
Here you select VAT group (optional). The VAT groups must be registered in the VAT settings procedure. A VAT group indicates which type of (tax related) trade you have with customers and suppliers, for example, domestic, EU, export, and so on.
Each VAT group is linked to a VAT code in the abovementioned procedure. The system will then automatically suggest a VAT code on the order/invoice depending on the selected VAT group. VAT groups are entered for customers and suppliers. However, the VAT code can be changed on order/invoice.

#### Supplier group
Here you select supplier group. The supplier groups must be registered in the Posting matrix procedure. The purpose of linking a supplier group to a country is to make the system automatically select a supplier group for new suppliers, based on the country to which they belong. The supplier group then determines the posting on order rows, and is often registered e.g. with the groups domestic, EU and import.

#### Supplier VAT group
Here you select VAT group (optional). The VAT groups must be registered in the VAT settings procedure. A VAT group indicates which type of (tax related) trade you have with customers and suppliers, for example, domestic, EU, export, and so on.
Each VAT group is linked to a VAT code in the abovementioned procedure. The system will then automatically suggest a VAT code on the order/invoice depending on the selected VAT group. VAT groups are entered for customers and suppliers. However, the VAT code can be changed on order/invoice.

#### Active
Here you determine if the country is active in the system. All countries are active by default. If you deactivate a country, it will not be selectable in the country field in different parts of the system. The purpose of this check box is to be able to filter out countries where you do not have any business relations.

#### VAT registration number exception
Some countries have another country code in their VAT registration number. For example, Greece has country code GR but in the VAT registration number they use EL. In this field you then enter "EL" for Greece. The warning function in the EC sales list procedure checks against this exception field.

#### Region/Subregion/Intermediate region
Here you see to which region, subregion, and intermediate region the country belongs according to the UN, if applicable.
