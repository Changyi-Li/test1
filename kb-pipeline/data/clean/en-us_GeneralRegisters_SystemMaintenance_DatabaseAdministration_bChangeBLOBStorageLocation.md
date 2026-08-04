### Change BLOB storage location
The BLOB storage tab, with this section – Change BLOB storage location – appears if the function is activated in the company in your Monitor ERP system.
BLOB stands for “binary large object”.

#### BLOB types
Here you can select what types of BLOB data you’ll be exporting. These are Document printouts, E-mail and EIM documents. By default, all types are selected for export. Estimated size for each type of BLOB data is shown to give you an idea of how much storage space is required for the data you are exporting.

#### Storage path
Here you enter a path where the exported BLOB data will be stored upon export. It is stored in sub-directories, by date. Before you export BLOB data you must make sure that; (1) the path for storage is set to a directory with sufficient storage space, and (2) that there is sufficient space for the temporary file which is created and saved in the temp-folder on the database server. The available space should be greater than the size of the database in question in both paths.
> Please note! If you change this path later, you must also move the existing BLOB data from the old path to the new path.

#### Run export of current data
This button is used to begin export of the BLOB data. Once the export is completed, the progress bar in the field under the button shows “100%”, with “OK” shown in the bottom field.
> Please note! Before exporting the existing data you must take a backup of the current database. BLOB data you have exported will not be included in the regular backup of the database. You must therefore make sure to regularly back up all sub-directories in the path where the exported BLOB data is stored.
After exporting the BLOB data you can reduce the physical file size of the database, as it now contains empty spaces in which BLOB data was previously stored. You can read more in the guide [Reduce the size of the database](GuideReduceDatabaseSize.htm).
BLOB data can be exported both from a live company and a test company. If you want to export BLOB data from a test company, this will not take place automatically when you export BLOB data from an actual/live company. This means you have to open the test company and export the BLOB data from there.

#### History
Use this button to view a log of previous exports, showing the timestamp and status of the export.
