## Server printers
In this procedure you register server printers.
Server printers are used for printouts initiated from the mobile client or from the Agent. The printouts are made by the application server (the Monitor server).
- For locally installed printers, the correct printer driver must be installed on the application server, and it must be accessible to the Windows account running the application server service.
- For Cloud printers using PrintNode, PrintNode must be correctly configured in the Settings for Cloud printer procedure.
- For e-mail based printers, a printer capable of receiving print jobs via its e-mail address is required.
In the Users procedure, in the Documents/Printers table, you link a server printer to the documents that each mobile user should be able to print. Each user who needs print capability must have such a link/connection.

#### Printer types and their settings
Locally installed printer
Select this option when the printer is installed directly on the application server, either locally or as a network printer.
When this type is used, settings are displayed that allow you to choose: printer, paper orientation (portrait or landscape), whether the printout should be duplex (two-sided), what paper size to use. If a custom paper size is selected, you can manually specify width and height. There is also an option to choose between color or black‑and‑white printing.
In the Location and Comment fields, you can enter any additional information.
E-mail based printer
Select this option when the printout should be sent as e-mail to a printer which has support for printing via e-mail.
In this mode you see the Printer's e-mail address field. It is mandatory. Here you enter the address to where the printout should be sent.
In the Location and Comment fields, you can enter any additional information.
PrintNode printer (Cloud printer)
This printer type is used for printing using PrintNode. To be able to choose a PrintNode printer, a valid API key must be registered in the Settings for Cloud printer procedure. Not until then is it possible for Monitor ERP to load the list of available printers from PrintNode.
When this type is selected, a field is shown where you choose a PrintNode printer. You can also decide paper orientation, duplex printout, paper size, and color or black-and-white.
In the Location and Comment fields, you can enter any additional information.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png)
