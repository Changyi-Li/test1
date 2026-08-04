### Authorization lists
In this box you register, copy, and delete authorization lists. An authorization list is a list of signers, and the invoice must be authorized by all signers in the list before it can be final recorded. In distinction from a signer group, when an invoice is sent to an authorization list it needs to become authorized by all signers in the list, unless one or more signers only forward the invoice. These signers will then not authorize the invoice. The signers will do their authorization in the order of the list, from the top, unless Parallel authorization has been activated.
An authorization list is useful if you for example have decided that all IT costs shall be authorized by a number of named persons. Then you create a code for IT and select which signers should be included in this authorization list.
On the function menu there are buttons to add, delete, and copy authorization lists. There is also a button you can use to view/show the signers. The purpose is to be able to create authorization lists based on signer code. You can for example use this function if you want all invoices with signer code CA (Carl Andersson) also should be forwarded and authorized by Nils Persson. You then check the box, select CA, and add Nils Persson to the box Selected. This signer code will then work in the same way as an authorization list.
You cannot change any information about the signer in this box. This must instead be made in the Signers box.

#### Code
Here you enter a code for the authorization list using a maximum of 8 characters.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Parallel authorization
If you check this box, the invoice will be sent for authorization to all signers at the same time, that is, the invoice does not have to be authorized in a specific order. When all signers have authorized the invoice it will be transferred to the final recording. This box is not checked by default when creating a new authorization list. If you check this box for existing lists, it will only affect new invoices and not existing invoices using this list. This way, this box can be set individually per invoice in its authorization list.
You can also activate parallel authorization for an individual signer. This is in that case done after you have chosen to show the signers in the box. Parallel authorization will then be activated by default in the authorization lists in which the signer is included. Meaning, in authorization lists the parallel authorization will be done first and then the other signers get to authorize in the order of the authorization list.

#### Active
An authorization list is active by default, but you can choose to deactivate authorization lists. These will then not be available in for example the Register supplier invoice procedure.
