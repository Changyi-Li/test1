### FAQ – E-invoices and invoice interpretation
What is meant by e-invoice?
An e-invoice is a digital invoice which is sent or received in an electronically structured format. A PDF invoice which is sent via e-mail does not count as an e-invoice.
What is a VAN operator?
A VAN operator functions as an intermediary, distributing e-invoices from and to your company. VAN stands for Value Added Network. If you use any of the integrations in Monitor ERP, you can have Crediflow or Maventa (Finland) as a VAN operator.
How do I start sending/receiving e-invoices?
[You can read more here](../../Using/EInvoice/EInvoice.htm) about how you activate a digital invoice flow.
What is GLN (Global Location Number)?
A GLN (Global Location Number) is used to identify a location or a company. GS1 has created a global standard for how GLN should be put together. Please note that Monitor ERP System AB cannot help you register a GLN, but if you have an existing number, we can help you to activate it on your e-invoice account.
How do I add a GLN (Global Location Number) to my account?
If you have a GLN number (Global Location Number) registered, please contact the Monitor Support Center to get help to activate it on your CrossState/Crediflow account.
Which e-invoice format is supported?
Does your customer wish to receive e-invoices in the format Svefaktura or perhaps Peppol? When using our integration with Crediflow, you do not have to worry. Crediflow takes care of all your outgoing invoices, ensuring they reach the recipient in the method they can and wish to receive them.
How do I stop sending e-invoices to a specific customer?
If you want to stop sending e-invoices to a customer, you can delete the party connection in Customer register.
To delete a customer e-invoice connection, follow the below steps:
1.    
Open the e-invoice connection with the help of the Open Crediflow dialog button.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Connection2.png)](../../../../Resources/Images/SubProjects/Einvoice_Connection2.png)
2.    
Click the information button next to Party-id.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_PartID.png)](../../../../Resources/Images/SubProjects/Einvoice_PartID.png)
3.    
Under Party information you select Delete party connection.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Party_Information.png)](../../../../Resources/Images/SubProjects/Einvoice_Party_Information.png)
4.   
Save the procedure.
How does invoice interpretation via CrossState work?
Below you can find out more about how invoice interpretation with CrossState works for those of you who have installed the option called Electronic invoice management (EIM).
The invoice interpretation service in CrossState helps you save time by automatically capturing the invoice information from your PDF invoices. This way you will not have to enter these manually in the Register supplier invoice procedure.
When the invoice arrives at CrossState, everything on the invoice image is interpreted. The system starts by identifying supplier details/information which are then matched with the supplier register which is loaded from Monitor ERPevery night. The interpreter will then search for texts/key words/identifiers such as "invoice date". When the key word is found, CrossState loads/retrieves the value to the right or just below the key word and presents it as a suggestion. When you accept the suggested value, by verifying the invoice in the For registration/verification inbox, feedback is sent to CrossState and information about the supplier is stored.
When you use the EIM option, information is interpreted at invoice header level, for example, supplier, invoice type (debit/credit), invoice number, invoice date, and amount. The information is then imported together with the invoice image into the For registration/verification inbox in the Register supplier invoice procedure. In the inbox, you verify the interpreted data and ensure that the correct values ​​have been found by CrossState.
[You can read more here](../../Using/EInvoice/InvoiceInterpretationCrossState.htm) about how invoice interpretation via CrossState works, as well as tips and recommendations for optimal invoice interpretation.
Why isn’t CrossState able to find the supplier on the invoice?
If CrossState cannot find the supplier, it can be worth checking the following:
1.    
Information in the Supplier register
Is there enough data registered? Compare the information in the invoice image with the information in the Supplier register, do they match? For example, is the correct corporate ID number/VAT registration number specified? Also check if there are duplicates of the supplier in the Supplier register, if so, it may be difficult for the interpretation feature to know which supplier to choose. If any information distinguishes the invoices, it can help to use the CrossState "Slogan" field.
2.    
Is the supplier register uploaded to CrossState?
If the supplier is new or you have recently made changes to the supplier register, it may happen that data has not yet been uploaded to CrossState. In the Settings for export/import procedure you can see when the most recent update of registers was made. If you have configured a scheduled upload of records, the registers will automatically be uploaded to CrossState every night (between 19:00-22:00). If you have made changes to the supplier register that you want the interpreter to take into consideration immediately, you can do a manual upload of the registers. This is done by using the Manual upload button in the Settings for export/import procedure. [Here you can read more about uploading of register](../../../GeneralRegisters/ExportImport/SettingsForExportImport/tImport.htm).
3.    
If supplier information is missing on the first page of the invoice
CrossState looks for supplier information on the first page of the invoice. If information that enables a supplier match is missing on the first page of the invoice, it can therefore be difficult for the interpreter to find the supplier. In such cases, it is good to enter as much other information as possible in the Supplier register that can be matched on the first page of the invoice. For example, a website address or visiting address. If this does not help, you can contact our support department who will investigate whether further adjustments can be made.
Why can’t CrossState find the correct value on the invoice?
If CrossState cannot find the correct value, it can be worth checking the following:
> The following only applies when CrossState has identified the supplier on the invoice.
1.     
Have a sufficient number of invoices from the supplier been verified?
Have multiple invoices from the supplier been verified? If only a few invoices have been verified, it may be that the interpreter has not yet stored all the information it needs to make a safe interpretation of the value. Please keep in mind that at least one day needs to pass between invoices for the information/knowledge to be saved for the supplier. If you e.g. verify 7 invoices from the same supplier all at one time, the interpreter will not have "learned" more on the seventh invoice than on the first, as feedback from the verification has not yet reached CrossState.
> It is not possible to say a general number of invoices that need to be verified to ensure that the value of the invoices will be found. The system continually gathers and uses information/knowledge. And the complexity and logic affect the learning of the interpretation function.
2.     
If the interpreter does not find an amount
If there are amounts that are not found, you can contact our support department for help with an amount template. An amount template helps the interpreter find the amounts on invoices from the specific supplier.
> When amount templates are to be created, the invoice flow in CrossState needs to be temporarily stopped. No invoices will during this time be interpreted or imported to Monitor ERP from CrossState. If there are invoices from different suppliers where the amount cannot be found, it is therefore good to notify support about all of them, that way the invoice flow does not have to be stopped several times.
3.    
Incorrect information/knowledge has been stored
If you failed to correct incorrect information found by the interpreter when verifying your invoices, incorrect information may be stored on the supplier. This may also be the case if your supplier has changed the appearance of their invoices. This causes the interpreter to look for the wrong values ​​on the invoice, which results in the correct values ​​never being found. You can get help removing incorrect information/knowledge by contacting our support department.
