### File management

#### Use same path as the original file when generating unique files
For operations and material in BOM and routing for parts, and for projects in the Project register, you also have the opportunity to activate Generate a unique file for linked files. Then the system creates and links a copy of the original file. This is then done for each manufacturing order of the part. The unique linked file then get the order number and a consecutive number in the file name. This feature can for example be applied for measuring records which need to accompany a manufacturing order and be filled out by the operators.
If you have a file linked to an activity in an activity template, and you use the activity template in a project, a unique file (copy) will be saved for the project in the same file path as the original file.
Here you select if the copy of the file should be saved in the same path as the original file.

#### Path to generated unique files
If you have configured No in the system setting above, you must here select a path where generated unique files should be saved. The path must first be registered and activated in the Paths procedure. Other users must also have to access the path from their Monitor ERP clients.

#### Method for copying files to Monitor folders
Here you decide if the files should be copied Manually (default) or Automatically when files are imported by using drag and drop in to Monitor ERP. When you choose Automatic copying you must enter a path in the system setting below.

#### File path for files being imported to Monitor
If you selected the Automatic option in the system setting above you must here select/enter a path. The path must first be registered and activated in the Paths procedure. Other users must also have to access the path from their Monitor ERP clients.
> Please note! A path selected in this setting will override the user rights configured for the path in the Paths procedure This means users can upload files even though the path has user rights configured.
