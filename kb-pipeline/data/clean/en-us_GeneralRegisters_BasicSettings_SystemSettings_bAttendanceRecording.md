### Attendance recording
In this section, you will find settings that apply to attendance recording in the recording terminal.

#### Name – Absence 1 and 2
Here you enter the name for the headings of the two absence columns in the Schedules procedure. In that procedure you select which salary types should be possible to generate during each respective absence. These names also apply to the two absence columns in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance procedure. In these columns you can determine, per row, which salary types should be generated to these absence codes. The columns can for example be used to generate salary types for IWH and IWH sickness to the absence codes for business travels and sickness.

#### Handling when user forgets to clock out
This setting determines how to handle when an employee forgets to clock out and then at a later time clocks in again in the recording terminal. In the system there is a 20 hour rule which applies if the employee forgets to clock out. The rule works like this:
If there are 20 hours or more since start of schedule and the schedule end has passed, it is considered a forgotten clock out. If the start of next day's schedule has passed, it is always considered a forgotten clock out. For overtime schedules, 20 hours apply from when the employee clocked in. No check will be made regarding the schedule end in this case.
The options available in this system setting are:
- Editable – By using this option, the time of the schedule end or the most recent work/attendance recording (if such has been made later than the schedule end) will be suggested as clock out. However, this can be edited by the employee.
- Schedule end – By using this option the time of the schedule end or the most recent work/attendance recording (if such has been made later than the schedule end) will be shown. This cannot be edited by the employee.
- Last recording – By using this option the time of the most recent work/attendance recording will be shown. This cannot be edited by the employee.

#### Time limit for planned absence part of day (min)
This system setting determines which time limit, before and after planned absence for part of day, should apply when clocking in and clocking out. Any recording made within this time limit will be considered to be the start time and end time for the planned absence. The planned absence code will then be the default absence code when clocking out. This absence recording will then be marked as OK during authorization and follow-up.
However, if the clock in/clock out is made outside this time limit, then the time between the recording time and the start/end time of the planned absence will be considered to be a separate absence recording. You must then select a separate absence code for the recording in question.

#### Reduce capacity on not approved planned absence
This setting determines whether not approved planned absence should reduce the work center’s capacity. This takes effect when you activate that the work center’s capacity should be determined by linked employees. Please note that the work center must be of the type Manual work.

#### Automatic generation of absence (change of period)
This system setting determines that attendance recording in progress will be ended and new absence records will be created for days passed. This is needed to be able to authorize. A recorded absence can create new absence days up until the person clocks in again. A planned absence will stop generating absence days when the planned absence period has reached its end date.

#### Breakpoint for change of period
This system setting will be activated if the system setting above has been activated. Here you can enter the time when the change of period should be made.

#### Enable training mode in the procedure Terminal settings
This system setting determines that the checkbox called Training mode will be displayed in the Terminal settings procedure. If you activate this system setting for a recording terminal in that procedure, it is possible to set the recording terminal in question in training mode.
> Training mode is activated by a specific shortcut key in the Recording terminal procedure. Then it will be possible to edit date and time in the recording terminal. This is used to simulate attendance and work recording when training the personnel. Training mode should only be used in test companies.

#### Activate site recording
With this setting you decide if site recording should be applied. Sites are used when recording attendance and breaks to describe the physical location to which the employees record in/out. Sites are used in order to, in the Attendance list and Evacuation list, show where all staff who are clocked in and all staff who are clocked out on a break are currently located – that is, within the building or elsewhere. Clocked out personnel can enter a site to indicate that they are still in the building. Site recording can also be used when working remotely, when employees are working from home or from another site.
When you activate the system setting with Yes, the following functions will open:
- The Sites tab is displayed in the Basic data – Attendance procedure. There you can register the sites which should be possible to use. You can, for example, register one location per recording terminal, department, building, one site for working remotely, etc.
- For persons in the Personnel records – Time recording and for recording terminals in the Terminal settings you can decide a default site for clocking in and a default site for when clocking out to go on a break. In the Personnel list – Time recording procedure you can update this for multiple persons by using the Attendance settings list.
- In the Recording terminal you will in the recording mode see the default site on the recording buttons for clocking in and for clocking out on break. A button used to select a different site ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Site.png) is available next to each recording button. This should be used if the default site should not be the one recorded on. A separate button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_in_google_maps.png) is also shown. This button makes it possible to at any time change site when the person is clocked-in or is on a break. You can also choose a site when the person has clocked out (when clocking out, the most recently recorded site will be removed). The purpose of this is to show in the evacuation list, that the person who is right now on his/her break is not in the building, or that the person is still in the building after he/she has clocked out.
- In the Recording log there is a specific list called Log list – Site, where you can see site recordings made.
- If you activate site recording, it is also supported in the Recording terminal in the mobile client and comes with the corresponding functions.

#### Block overlapping attendance + absence
Here you can activate a validation to prevent attendance + absence from overlapping each other. If you choose to allow overlapping, it means that absence or break will always override attendance.
