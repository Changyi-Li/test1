### Serial number
Number series for serial numbers on parts. These number series can be created using different formats.
Which number series will be used depends on the Grouping term and its intervals From – To. A part can have several different number series for serial numbers. If so, the grouping term Part number carries the most weight. Then Part code and finally Product group. If there are several number series within the same grouping term, then the order of the rows determines which number series will be used. For parts you can configure that serial numbers should be loaded from number series. If there is no convenient number series for a part, part code, or product group, a serial number must be manually set when the part should be assigned a serial number. That is, when the customer order is registered or delivery reported.
There is a general number series to fall back on if you do not find a number series. This number series is included in the system when you start up the program for the first time. It has a high number so it will end up last in the list of number series. This row cannot be deleted but you can change the next number in that series. The default format is <code> but this can be changed.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Grouping term
The grouping term determines where the number series should be used. You can select from the following: Part number, Part code, and Product group.
Which number series will be used depends on the grouping term and its limitations. A part can in theory be included by multiple number series. Then the grouping on the part number will be the primary, secondly the part code, and thirdly the product group. If multiple number series match on the same grouping term, it is the sequence among the number series which applies (the row here in the table which is at the top of the rows with the same grouping term).

#### From and To
In these fields you can enter an interval for the selected grouping term which the number series applies to.

#### Next number
Here you enter the number that should be used the next time a number is created from the number series. The greatest number allowed is 2,147,483,647.

#### Format
In this field you enter one or multiple tags that describe structure and contents of the number series The available tags are described below: In a number series for Serial numbers you must at least include the tag <code> in the field. In a number series for Batch A batch is the set of components/products manufactured at the same time and made from the same original material. numbers you can leave the field empty if you want to. This means any batch number can instead be entered manually when reporting.
| Tag | Description |
|---|---|
| <code> | The next number in the number series. |
| <code:NN> | The next number in the number series, plus a "filling" of zeros. NN is the number of positions of zeros + numbers, up to a maximum of 19 positions available for number series. NN can be from 0 to 19. For example, if the next number in the number series is "1234" and you enter <code:19>, the next number will be "0000000000000001234". If you enter <code:10>, the next number will be "0000001234". If you enter <code:2>, the next number will be "1234". |
| <yyyy> | The year, containing four digits, for example "2016". |
| <yy> | The year, containing two digits, for example "16". |
| <MM> | The month, where "01" means January. |
| <dd> | The day in the month, for example "22". |
| <HH> | Hour. |
| <mm> | Minute. |
| <ss> | Second. |
| <week> | The week number, containing two digits, for example 01-53. |
| <part> | Part number. |
| <rev> | The part's revision on customer order or manufacturing order. |
| <orderno> | Order number on purchase order, manufacturing order, or customer order. |
| <pos> | Order row position on purchase order or customer order. |
| <node> | Node A node is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the highest level is called the main part (order). number for part with maximum quantity in manufacturing order or part in coordinated processing. |
| <number> | Partial delivery number. Increases each partial delivery by +1 in order to get unique batch numbers on parts with batch traceability. The tag can be used to suggest batch numbers for transfer to stock from purchase orders and manufacturing orders. The <number> tag provides a unique counter per reporting of purchase order rows or parts on manufacturing orders. This tag needs to be combined with at least one other tag to create a batch number, e.g., <orderno>-<part>-<number>. |
A number series can be composed by different tags which are separated with an optional character, see example below.
Examples of composed number series:
<code>/<rev> results in numbers such as "10001/A", "10002/A".
<code>:<yy>-<MM>-<dd> results in numbers such as for example "10001:16-02-19", "10002:16-02-19".
> Please note! The tags are case sensitive.
