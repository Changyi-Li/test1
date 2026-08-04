### FAQ – EDI and shipping
Can I get a receipt list for shipments from Monitor ERP?
Yes, you can get a receipt list from the Shipment list, list type Receipt list.
E-mail address is missing in Sender in Register shipment. How do I add an E-mail address?
The e-mail address is loaded according to the Load to our reference on shipment system setting. This system setting determines whether the e-mail address should be loaded from the User procedure, either from the Description field from a linked Employee number (loaded from Personnel records) or from Our reference on customer order. The alternative None also exists, which will leave the e-mail address empty.
How do I add more package types to use in the shipping integration in Monitor ERP?
You add more package types under the Package typePackage type describes what kind of package that is used, such as "pallet" for EU pallets, "box" for cardboard boxes etc. tab in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure.
How do I add more Goods types so they’re available on package rows in Register shipment?
You add more goods types under the Goods typeGoods type describes what kind of part it is, for example machine parts, electronics, etc. Goods type is printed on shipping documents. tab in the Basic data – Part procedure.
The package type code is wrong, how do I correct it?
Check valid package type codes for the shipping agents in the shipping integration’s portal (nShift Delivery, nShift Web-TA or Logtrade) and adjust the package type code in the Basic data – Part procedure, under the Package types tab. For the current shipment you can write the correct package type code.
I want to change the default package type, how do I do that?
The default package type is determined by the Default package type system setting, when you change the default package type, the change will be applied to new orders/deliveries. The selectable package types must first be registered in the Basic data – Part procedure, under the Package type tab.
Am I able to export customs information for a shipment that I have created in Monitor ERP?
If you use a freight integration, you will be able to carry over the information you enter under the Customs information tab in the Register shipment procedure.
How can I save temporary files of shipments that are sent via the integration?
By marking the Save temporary files at export in the Settings for export/import procedure, a temporary file is saved on the Monitor server for the user using the Monitor service.
Here can I specify which printer should be used when printing freight documents?
This can be configured in the Users procedure. You can read more about [Printer for freight documents](../../../GeneralRegisters/UserPersonnel/Users/bPrinters.htm) here.
