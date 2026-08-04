### Desktop

#### Message center
In the message center you can handle different types of messages.
- Notifications can for example be a message from the system saying that the Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. is completed and presenting the result, or that there is an update available for downloading.
- Chat messagescan be sent to and received from other users.
- Tasks are things you are supposed do something about and which you should get reminders about. It can for example be that there is an activity for a customer which should be performed. The task can be reported directly in the window without you having to go to e.g. the customer register.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/MessageCenter.png)](../../../../../Resources/Images/News/MessageCenter.png)
The menu in the message center (in the upper left corner of the desktop).
If you are logged in when a notification, message, or task is received, then a message box will appear in the bottom part of the program (similar to a notification for received e-mail in Outlook). If you click the message box you will be linked to the affected record in the message center.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Notification.png)](../../../../../Resources/Images/News/Notification.png)

#### Clipboard
You can open a clipboard window without having opened a list procedure. If you manually add a row in the selection in the Clipboard, then the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature will be linked to the specific register, for example the part register.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/ClipBoard.png)](../../../../../Resources/Images/News/ClipBoard.png)
When you add a selection from a list you will see a box in the program letting you know how many records have been added in the selection. If you click this box you will be linked to the Clipboard window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Notification2.png)](../../../../../Resources/Images/News/Notification2.png)
> You can use the selection you have in the Clipboard when making selection in lists by checking the Clipboard checkbox to the right of the selection term. This checkbox is only available for the terms which at the moment have a selection in the Clipboard.

#### Find procedure
In Find procedure there are two tabs. The Search result tab is active when you have started writing a text in the search field and is filtered depending on what you type in the field. The Recent tab is active when you click the arrow in the search field and it displays the ten procedures most recently started by the user.

#### Monitor search
Here you can search among almost all data in the system. For example a text on an order, a phone number, a reference person, etc. The search result is shown in a result window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/MONITORSearch.png)](../../../../../Resources/Images/News/MONITORSearch.png)
The result window after a search has been made for the word "Lucka".
The sorting of the search result depends on three parameters:
1. Relevance for the search. If the text you search by provides a complete match in any data, this will be considered a better result that if the text only is a partial match. If you for example make a search for the word "lucka" and there is a part name that is "Lucka" then you have an exact match, unlike if the name of the part is "Sidolucka". Both parts will be included in the result but the part with the name "Lucka" will be ranked higher than the part with the name "Sidolucka".
2. Which field provides the match. For a part, the part number and name are ranked higher than all other fields. In the customer register it is customer number and name which are ranked the highest, etc.
3. The role of the user. If you for example belong to the role Seller, then customers and customer orders will be ranked the highest. If you for example belong to the role Purchaser, then suppliers and purchase orders will be ranked the highest.
The purpose of this ranking and sorting is to emphasize such data which is more likely for you to be searching for. Please note! You will get the same number of matches (and the same matches) in the result regardless of these three parameters. They only affect the sorting.
The result can be grouped and filtered. It is also possible to link to the registers relevant for the record found in the search. If you for example get a match for a part and you use the "Go to" link, the procedure Part register with the part in question already loaded will open.

#### The Module menu
When you click on a module to select and start a procedure you see all procedures in that module at the same time and they are grouped in sections. This is a difference from G4 where each section has a drop-down menu.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/ProcedureMenu.png)](../../../../../Resources/Images/News/ProcedureMenu.png)

#### Backstage
In the backstage of the desktop you find general functions and settings for the program. The parallel possible to make with G4 is the File menu which was shown when no procedure window was open and the menu item Settings.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/Backstage.png)](../../../../../Resources/Images/News/Backstage.png)
What you can do in the desktop backstage is:
- Configure settings, e.g. change the color theme or activate Go to next field using Enter
- Change warehouse
- Change language
- Change accounting year
- Create your own desktop configurations or add a new desktop template containing different desktop components, for example, Inbox Monitor-to-Monitor and Favorites. Desktop templates have to be created by an administrator in the separate procedure called Desktop templates (see video above).
- See information about the current program version and read the changelog, see what options and licenses are installed, synchronize system configuration (see below).
- Log out.
For the desktop component Favorites it is also possible to add shortcuts to procedures, but also to websites and external programs and files.

#### Synchronize system configuration
Under About in the backstage it is possible to use the button Synchronize to synchronize the system configuration. This means you can quickly access and start using, for example, new user licenses or options ordered, without having to install a new key file as in G4. You do not even have to restart the server or wait until the next day (an automatic synchronization is run once every day).
