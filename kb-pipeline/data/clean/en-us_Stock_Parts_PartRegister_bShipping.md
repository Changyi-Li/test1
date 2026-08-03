### Shipping
In this box you configure shipping settings for the part. If the part is a packaging part, you can configure specific packaging settings. For parts of the Service and Fictitious type you cannot enter any shipping settings. However, for the Fictitious part type it is possible to enter pick instructions and to link files to pick instructions.

#### Volume
Here you see/enter the part's volume. The unit is cubic meters.

#### Loading meters
Here you see/enter the part's loading meters. The unit is meter.

#### Quantity/package
Does not apply to packaging parts. Here you indicate the quantity of the part that fits in a package when the part is sold. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, one transport label will be printed for each package that has been delivery reported on the customer order. The quantity is displayed in the unit selected on the main row, but it will be saved in the standard unit. The quantity meant when linking a packaging part is the quantity/package that fits in the inner packaging. It is overridden by the quantity/package of the customer link in the box Customer links. This field is not available for parts of type Service.

#### Packaging part
Does not apply to packaging parts. Here you can link a general packaging part to the part link. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature you can select among the parts for which the setting The part is a packaging part has been activated.
You can also link a packaging part to the part in the customer link. It will then override the general packaging part.

#### Packaging template
Here you can link a general packaging template to the part. A packaging template is useful if the part should always be packed using the same combination of packaging parts.
You create packaging templates in the Packaging templates procedure. A packaging template is used to form a package structure which will be included when the part is included in pick lists created using the Picking plan list type in the Delivery planning procedure. The package structure is then shown and used in the Pack for delivery procedure when you load the pick list.
When you have selected a packaging template, the packaging part used to pack the part in, will automatically be entered in the field called Packaging part. By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) next to the field you can see the packaging parts included in the template. For these parts you can see level, packaging type, and minimum quantity.
You can also link a packaging template to the part in the customer link. It will then override the general packaging template.

#### Goods type
Does not apply to packaging parts. Here you see/select the goods type of the part. This information is printed on shipping documents. Goods types are handled in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part.

#### Default transport label
Does not apply to packaging parts. The default label type determines the type of transport label selected by default for the printout when the part is delivery reported on a customer order. This setting applies for all part types, except for Fictitious. The None option is selected by default. The options available as default transport label in the field are: None, Transport label – A4, Transport label – A5, Label, or Transport label – Grouped.

#### Document variant
Here you can choose a variant of the default transport label which should be default for the part when you report delivery. You can also select from you own transport label variants created in the Document templates procedure.

#### Transport cost
Does not apply to packaging parts. Here you can enter a standard transport cost per unit, that is, the cost to ship the part to the national border.

#### Pick instruction
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).
Here you can enter a general pick instruction for the part respectively the packaging. This text is shown on the pick list for customer orders that are delivery reported. If a pick instruction has been entered in a customer link on the part, this will instead be shown on the pick list.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
The files can be printed automatically together with the pick list.
Packaging part

#### The part is a packaging part
Check the this box if the part is a packaging part. This will activate the following fields which are specific for packaging parts. At the same time, some of the other shipping fields will become unavailable since they do not apply to packaging parts.

#### Packaging type
The packaging type you select here determines how packaging structures should be created. There are rules for which transport labels should be used for the different packaging types. The packaging types available to choose from in Monitor ERP are: Unspecified packaging, Outer packaging, EUR pallet,, Inner and Cover packaging. The packaging type Unspecified is selected by default for a new packaging part.

#### Assign package number
With this checkbox you decide if the packaging part should be assigned a package number (an internal consecutive number for packages). The packaging types Outer packaging, Inner packaging, and EUR pallet, will by default be given package numbers. Package number is used if you apply packing in Monitor ERP. This is a step between delivery planning and delivery.

#### Package type
Here you can select the package type of the packaging part. Package type Package type describes what kind of package that is used, such as "pallet" for EU pallets, "box" for cardboard boxes etc. is used to classify the packaging to the shipping agent. You can select among the package types that have been set as active in the Basic data– Part procedure..

#### Package volume consists of
There are two alternatives to choose from regarding how the volume of the package should be calculated. You either use only the packaging part's volume, or you use the packaging part's volume and the part's volume, in the volume calculation on the order row/delivery.

#### Length, Width, and Height
In these columns you can enter measures used to specify how large the packaging part is.

#### Transport label – Pkg struct.
Here you decide which variant of the document Transport label – Package structure that is default to be printed for the packaging part.
