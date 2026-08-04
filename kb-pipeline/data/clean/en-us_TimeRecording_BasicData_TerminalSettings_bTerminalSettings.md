### The Terminal settings table
In this table you add users as terminal users and configure different function for their recording terminals.

#### Terminal user
In this column you select a user name from the register. A "terminal user" is the user who is logged in to Monitor ERP in the recording terminal. The name is shown in the field to the right.

#### Attendance recording
With this checkbox you decide if it should be allowed to record attendance on the recording terminal in question (checked by default).

#### Work recording
With this checkbox you decide if it should be allowed to record work on the recording terminal in question (checked by default).

#### Only card
With this setting you determine if recording can only be made using card number/card code on the recording terminal in question and in the mobile client. A card number/card code must be entered for the persons who will be recording on this recording terminal. This is registered in the Personnel records – Time recording procedure.
In the Recording terminal procedure the person then enters his/her card number/code instead of the employee number. Normally, the recording terminal computer is then equipped with a card reader to use. The person swipes his/her card through the card reader which reads/scans the card and automatically fills in the field Employee number in the recording terminal. The field shows an asterisk (*) for each character, meaning you cannot see the card number or card code on the screen. The card must first have been registered by the administrator in the above mentioned procedure.

#### Touch screen
If you check this checkbox it means a numerical key pad is shown on screen when a person clicks or touches the Employee number field on the recording terminal. This facilitates clocking in/out when a touch screen is used.

#### Empty desktop
With this checkbox you decide if the recording terminal always should display the a standard layout in the basic mode, that is, the mode when no employee number has been selected in the recording terminal. This setting is not activated by default. Then the basic mode in the recording terminal shows the desktop configuration which has been configured for the logged-on terminal user in Monitor ERP on the recording terminal computer.

#### Training mode
This setting is only visible if you have activated the system setting Enable training mode in the procedure Terminal settings. With this checkbox you decide if it should be possible to set the terminal user's recording terminal in training mode. When using the training mode it means that date and time will be possible to edit in the recording terminal. This is used with test companies to educate the personnel in time recording.
Windows client:
To put the recording terminal in training mode, press the shortcut keys Ctrl + Shift + D in the terminal user's recording terminal. After that you can enter a date and time and click the button OK to activate the new date and time. To exit the training mode you just click the same shortcut keys again. Then the date and time will be reset to the computer's current date and time.
Mobile client:
To put the recording terminal in training mode you should press the button Activate in the section called Activate training mode. This section is available in the terminal user's recording terminal when this setting is activated. After that you can enter a date and time and click the button Update to activate the new date and time. In this section you can also click End training mode when you want to exit the training mode. Then the date and time will be reset to the unit's current date and time.

#### Stay logged in
If the checkbox is checked, you will stay logged in to the Recording terminal while reporting time and quantity, and any drawings you have open will not be closed at each recording.

#### Default site for clocking in
If site recording is activated (via the system setting called Activate site recording), you can here select a default site for the recording terminal for persons who record attendance using the terminal in question. You register sites in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance procedure.
A default site for clocking in can also be set for individuals by using the Personnel records – Time recording procedure. If a default site for clocking in has been entered for the recording terminal, this will override the setting configured for the person/individual who records using the recording terminal in question.
If there is no default site selected for the person – or for the recording terminal – the suggested clock-in site will be the site where you were most recently clocked in.

#### Default site for recording breaks
If site recording is activated (via the system setting called Activate site recording), you can here select a default site for the recording terminal for persons who record break time using the terminal in question.
A default site for recording of breaks can also be set for individuals by using the Personnel records – Time recording procedure. If a default site for recording of breaks has been entered for the recording terminal, this will override the setting configured for the person/individual who records using the recording terminal in question.
If there is no default site selected for the person – or for the recording terminal – the suggested clock-in site will be the site where you were most recently clocked in.
