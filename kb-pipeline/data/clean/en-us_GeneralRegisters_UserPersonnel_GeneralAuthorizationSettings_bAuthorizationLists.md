### Authorization lists
In this box you register, copy, and delete authorization lists. An authorization list is a list of signers. A purchase order row must be approved by all signers in the list before it can be printed, sent via e-mail, or arrival reported. In distinction from a signer group, when a purchase order is sent to an authorization list it needs to become approved by all signers in the list. The approval takes place according to the order in an authorization flow, unless you have activated Parallel authorization.
An authorization list is useful if you for example have decided that all IT purchases should be approved by a number of named persons. Then you create a code for IT and select which signers should be included in this authorization list and their respective order in the authorization list.
You can also change an authorization list directly on a purchase order row in the procedures Register purchase order and Approve purchase order. This applies to users who have user rights to modify the authorization list. This can be configured as user-specific user right for purchase orders in the Users procedure. Only users with the role ERP manager and Purchasing manager are by default allowed to modify authorization lists.

#### Code
Here you enter a code for the authorization list using a maximum of 8 characters.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Parallel authorization
If you check this box, the purchase order will be sent for approval to all signers at the same time, that is, the purchase order does not have to be approved in a specific order. When all signers have approved, the purchase order can go ahead in the flow and can be printed or sent via e-mail to the supplier. This box is not checked by default when creating a new authorization list. If you change this setting for existing lists, it will only affect new purchase orders and not existing purchase orders using this list. The setting can also be configured individually per purchase order row in the authorization list in question in the Approve purchase order procedure.

#### Active
An authorization list is active by default, but you can choose to deactivate authorization lists. Then these list will not be available on order rows in for example the Register purchase order procedure.

#### Show signers
If you check this box, the signers appear in the Authorization lists box. The purpose is to be able to create authorization lists based on signer code. You can for example use this function if you want all purchase orders with signer code CA (Carl Andersson) also should be forwarded and approved by Nils Persson. You then check the box, select CA, and add Nils Persson to the box Selected. This signer code will then work in the same way as an authorization list.
You cannot change any information about the signers in this box. This must instead be made in the Users.
