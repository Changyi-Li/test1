### The Standard list
The Standard list displays different part information depending on which presentation you have selected. The information you can update when making the list Updateable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) (Ctrl + U), is described below.

#### Name
Part name can be updated in all presentations of the list.

#### Part type
Part type can be updated in all presentations of the list. The part type determines what kind of part it is: Purchased, Manufactured, Fictitious, Service, and Subcontract. A subcontract part is created by the system when you add a subcontract in the BOM and routing. Read about the different [part types](../PartRegister/hPartRegister.htm) in the help function for the Part register procedure. Read about [subcontract parts](../SubcontractParts/wSubcontractParts.htm) in the help function for the Subcontract parts procedure.
General

#### Standard price
Each part can have one current standard price per unit. The standard price is always entered in the part's main unit and in the company currency.

#### Part category
The part category is used as a selection term and grouping term in lists.

#### Part code
The part code is used as a selection term and grouping term in lists. Part codes are handled in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part.

#### Product group
The product group determines the part's posting and VAT. Product groups are handled in the Posting matrix procedure.

#### Stock update
With this setting you decide if the part should be stock updated. Stock update is selected by default for new parts. Parts of the type Fictitious or Service are not stock updated. For parts with traceability it is not possible to deactivate the stock update setting.

#### Purchase/Manufacturing on project (P)
This checkbox determines if purchased parts should be purchased on project and manufactured parts should be manufactured on project.

#### Country of origin
Here you can see the part's country of origin (applies to IntrastatIntrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states.).

#### Random stock location
With this setting you decide if random stock location should be applied for the part. Random stock location is activated by default for new parts. This means that if the balance of the location becomes zero (0), the location will be deleted for the part. This is done automatically when you report withdrawals from the stock which empty the location.

#### Status
Read the [help function for the Part register](../PartRegister/bStatusBlock.htm) procedure, to learn about status.

#### Net weight
The part's net weight can be entered by using two to five decimals. The unit is always entered in kg.

#### Fixed weight
Here you decide if the net weight for the part should be fixed and cannot be recalculated in the Calculate weight procedure.

#### Administrator
You can select an administrator via employee number of the reference persons registered in the Personal records procedure. Part administrators are used as selection terms in many lists. This way all planners are able to print lists of parts that they administer.

#### CN code
Here you can see the part's CN code (goods code).
Purchase

#### Default transport label (Purchase)
This setting determines the default type of transport label for the printout when the part is arrival reported. This setting applies for all part types, except for Fictitious. None is selected by default, that is, that no transport label will be printed. Here you can also select Transport label – A4, Transport label – A5, or Label. The label size is 76×51 mm.

#### Quantity/package (Purchase)
Here you enter how many of the part that fits in a package when the part is purchased. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, a transport label will be printed for each package that has been arrival reported on the purchase order. The part unit is according to the setting in the part register.

#### Alloy code/Mark-up
In this field you enter the alloy cost that applies when purchasing the part. The alloy code/mark-ups are handled in the Basic data – Part procedure.

#### Alloy quantity
Here you enter a quantity of the mark-up included in the part. The unit is loaded from the Basic data – Part procedure.

#### Comment (Purchase) – Shown on
This setting determines where the general purchase comment should be shown. You can choose on which documents, Inquiry and/or Order, the purchase comment should be shown. If a comment is entered on the supplier link, this will override the general purchase comment.
Sales

#### Lead time to customer
Here you can enter a general lead time to customer for the part. This is entered in number of work days. A check will be made against this date when registering orders.

#### Quantity for lead time
Here you enter the general quantity of parts on the order for lead time to customer.

#### Comment (Sales) – Shown on
This setting determines where the general sales should be shown. You can choose on which documents, Quote, Order confirmation, Delivery note, and/or Invoice, the sales comment should be shown. If a comment is entered on the customer link, this will override the general sales comment.

#### GS1 code
In this column you see the general GS1 code which applies to the part.
Manufacturing

#### Quantity/package (Manufacturing)
Here you indicate the quantity of the part that fits in the package when the part is manufactured. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, a transport label will be printed for each package that has been reported as finished on the manufacturing order. The part unit is according to the setting in the part register.

#### Calculation mark-up
Calculation mark-ups such as SC mark-up, SO mark-up, Sales OH, and Profit can be updated.

#### Calculated quantity
You can enter a quantity that should be selected by default for the part in pre-calculations. If the option Warehouse is installed in the system, it is mainly the value you enter here that will be used. If no calculated quantity is entered, the part's order quantity for the warehouse you are working in will be used instead.
If you have not installed the option Warehouse, the values for order quantity and calculated quantity are synchronized.

#### Production engineer
Information about which production engineer is responsible for the part's BOM and routing. Both employee number and name are shown in the list.

#### Default transport label
This setting determines the default type of transport label for the printout when the part is manufactured. This setting applies for all part types, except for Fictitious. None is selected by default, that is, that no transport label will be printed. Here you can also select Transport label – A4, Transport label – A5, or Label. The label size is 76×51 mm.
Shipping

#### Net weight
In this column you see the part's net weight. The unit used is kg.

#### Volume
Here you see/enter the part's volume. The unit is cubic meters.

#### Loading meters
Here you see/enter the part's loading meters. The unit is meter.

#### Quantity/package (Sales)
Here you indicate the quantity of the part that fits in a package when the part is sold. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, one transport label will be printed for each package that has been delivery reported on the customer order. The quantity meant when linking a packaging part is the quantity/package that fits in the inner packaging. The part unit is according to the setting in the part register.

#### Packaging part
Here you select a general packaging part that should be linked to the part. You can select among the parts for which the setting The part is a packaging part has been activated in the part register. You can also link a packaging part to the part in the customer link. It will then override the general packaging part.

#### Packaging template
Here you can select a general packaging template for the part. A packaging template is useful if the part should always be packed using the same combination of packaging parts. When you have selected a packaging template, the packaging part used to pack the part in, will automatically be entered in the column called Packaging part. You can also link a packaging template to the part in the customer link. It will then override the general packaging template.

#### Default transport label
The default label type determines the type of transport label selected by default for the printout when the part is delivery reported on a customer order. This setting applies for all part types, except for Fictitious. None is selected by default, that is, that no transport label will be printed. Here you can also select Transport label – A4, Transport label – A5, or Label. The label size is 76×51 mm.

#### Goods type
Here you see/select the goods type of the part. This information is printed on shipping documents. Goods types are handled in the procedure Basic data – Part.

#### Package type
Here you can enter the package type of the part. This is done in order to classify the packaging to the shipping agent. Package types are handled in the procedure Basic data – Part. Examples of package types are pallet, roll, and barrel.

#### Packaging type
The packaging type you select here determines how packaging structures should be created. There are different rules for which transport labels should be used for the different packaging types. The default option is Unspecified. In addition to this you can also select Outer packaging, EUR pallet, Inner packaging, or Cover packaging.

#### Package volume consists of
There are two alternatives to choose from that describes of what the package volume consists. This is used to determine how the package should be calculated in the delivery reporting. The available alternatives are Package volume (enclosing) and Package volume + part volume.

#### Length, Width, and Height
In these columns you see measures used to specify how large the packaging will be.

#### Transport cost
A standard amount for the transport cost per unit to ship the part to the national border.
