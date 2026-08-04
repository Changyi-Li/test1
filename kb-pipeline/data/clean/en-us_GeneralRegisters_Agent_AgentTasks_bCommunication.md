### Communication
If it is possible to export the marked procedure in the Selected procedures box, you can here select in which format you want to export the result of the agent task. You also select if the result should be saved on the server and be sent via e-mail.

#### Export
Here you select export format for the result (list) of the agent task. At present, the following are supported: Excel, PDF, CSV (comma separated) and CSV (tab separated).

#### Raw data
If this checkbox is marked, raw data will be exported.
This setting is only available when applying agent tasks for the Print accounting report procedure when you have chosen to export to Excel.

#### Save
Select a path where you want to save the result of the agent task. You can select one of the active file paths that are registered in the Paths procedure.

#### Send
Here you choose if the result should be sent using E-mail or E-mail (user in Monitor ERP), or if it should be printed on a Server printer.

#### Receiver
Here you configure to which receivers the result should be sent, depending on which alternative you selected in the column Send..
-    
If you select E-mail, you enter an e-mail address here. You can enter several addresses by separating them using semicolon.
> The system setting called E-mail sender for result e-mail must be entered under the Agent tab in the System settings procedure, otherwise a warning will be displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png). The system settings called User name (Exchange) and Password (Exchange) under the sames tab should also be entered, if the Method for e-mail system setting has been configured to Server based, via Microsoft Exchange or Server based, via Microsoft Exchange Online.
- If E-mail (user in Monitor ERP) was selected, you should enter a user here. The user should have an e-mail address entered in the Users procedure.
- If you select Server printer, you choose a server printer here. You can select among the server printers that are registered in the Server printers procedure.

#### Export/Send empty lists
Here you determine if empty lists should be exported and sent.

#### Include
Here you decide if the Selection tab and filters, if any have been used, and a page header, should be included in the export. This makes it possible to see on the printout which selections have been made and which filters have been used to create the list. In the header of the printout you find information about, for example, from which company the printout is made as well as when the printout was made.

#### Override file name
Here you can enter a customized file name for the file that should be exported and saved/sent by the agent task. You do not have to enter the file extension (.pdf eller .xlsx). This is automatically added. If you leave the field empty, the file name will become the procedure plus today's date.
> Please note! The file name cannot contain characters which are invalid for file names. If you enter such a character, an error message will appear.
It is possible to enter variables in the file name. The available variables are described in the table below.
| Variable | Explanation | Examples |
|---|---|---|
| %y | Year (YY) | 21 |
| %Y | Year (YYYY) | 2021 |
| %m | Number of the month | 04 |
| %W, %w | Week number (start Mon.) | 14 |
| %U | Week number (start Sun.) | 15 |
| %a | Day of the week, name (short) | Fri. * |
| %A | Day of the week, name | Friday * |
| %b | Name of month (short) | Apr. * |
| %B | Name of month | April * |
| %j | Day of the year | 106 |
| %d | Day of the month | 16 |
| %x | Current date | 2021-04-16 * |
| %X | Current time (HHMM) | 1051 * |
| %c | Current date and time (HHMMSS) | 2021-04-16 105108 * |
| %H, %h | Hour (24 hours) | 16 |
| %I | Hour (12 hours) | 04 |
| %p | AM/PM (used with %I) | PM |
| %M, %i | Minute | 25 |
| %S, %s | Second | 59 |
| %% | Percentage sign | % |
> Please note! The date format and spelling of the day of the week and name of the month is determined by the regional settings and the language settings in Windows. Time is shown without separator between hour, minute, and second.
