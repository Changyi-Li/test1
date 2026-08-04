### General

#### Time recording
With this setting you determine if both attendance and working time can be recorded, or if only working time can be recorded by the person in question. The final option is that no time can be recorded.
- No – With this option it is not possible to record time. All settings which belong to attendance and work will become deactivated if you select this alternative.
- Attendance/Work – With this option it is possible to record both attendance and work. It is selected by default. This is the option normally used for persons registered in the personnel records.
- Only work – If you select this option it is only possible to record work. This alternative is selected for machinery. The boxes Time banks and Planned absence becomes inactivated if you select this alternative. There will be no attendance, overtime, flex time, or absence for a machine, but only work recording (start/stop of the machine). Read more about [machine recording](../../Recording/RecordingTerminal/MachineRecording.htm).

#### Parameter group
Here you select the parameter group to which the person should belong. You register parameter groups in the Parameter groups procedure. These govern all settings having to do with overtime, shorter working hours, flex time, time banks, absence, and additions (allowances, disbursements, etc.).

#### Schedule management
With this setting you determine if schedule management should be applied. The default option here is No schedule. If the option According to schedule cycle is selected, then the boxes Time banks, Schedule exceptions, Schedule cycles, and Planned absence will become available. You can also access the table Available schedules at schedule change by using the button with the same name.

#### Default site for clocking in
If site recording is activated (via the system setting called Activate site recording), you can here select a default site for the person for recording of attendance. You register sites in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance procedure.
A default site for clocking in can also be set for recording terminals in the Terminal settings procedure. If a default site for clocking in has been entered for the recording terminal used by the person, this will override the setting configured for the person/individual.
If there is no default site selected for the person – or for the recording terminal – the suggested clock-in site will be the site where you were most recently clocked in.

#### Default site for recording breaks
If site recording is activated (via the system setting called Activate site recording), you can here select a default site for the person for recording of break.
A default site for recording of breaks can also be set for recording terminals in the Terminal settings procedure. If a default site for recording of breaks has been entered for the recording terminal used by the person, this will override the setting configured for the person/individual.
If there is no default site selected for the person – or for the recording terminal – the suggested clock-in site will be the site where you were most recently clocked in.

#### Card number
By clicking this button you access a table where you in the column Card number can enter a unique card number or a code for the person. The number or the code you enter here is displayed as asterisks (*******) so it will not be revealed.
The card number does not refer to a PIN code. It is the number which is saved on the card's magnetic stripe. You can equip the computer with a card reader for magnetic stripe, then the card number will automatically be entered in the field when you swipe the card through the card reader. The card which the person chooses to register here should then be used by that person when recording in the recording terminal. The recording terminal computer must then be equipped with a similar card reader.
If you instead enter a code in the field, no cards or card readers are needed. But in this case, the person must remember the code and enter it each time he/she is recording in a recording terminal.
You can also enter a Comment regarding the card number or the code. For example, you might write a comment stating that the card used is the person's credit card.
In the column called Valid to you can enter to which date this card number or code is valid. This does not refer to a card's validity period, but is a date you choose as end date for the card number/code. If you leave this field empty, the registered card number or code will apply until further notice.
> Other technology (than card reader for card with magnetic strip) that works for card number in Monitor ERP are for example Near-field communication (NFC).

#### Terminal access
By clicking this button you can configure the access to different terminals for the person. This limits which recording terminals the person is allowed to record on. If no user is added here, it means that the person is allowed to record on all recording terminals.
In the User column you select a user name for a recording terminal. If you have added a user and the person should also be able to record in the recording terminal on his/her own computer, then you must here also add the user to whom the person is connected.
Type shows if it is possible to record attendance and/or work with the specific terminal.
In the column Only card you see a Yes if the terminal only allows recording using card. Otherwise you will here see No.
