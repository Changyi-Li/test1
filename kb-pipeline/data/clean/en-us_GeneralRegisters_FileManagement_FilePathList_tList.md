### The List tab
In this list you’ll find existing paths to files already linked to records in the database. You also see the name of the paths. If linked files exist in file paths (sub-directories) to a path, this will also be shown.
In the list, you can change to new paths or enter new file paths to these files. You must do this if the files have been or will be moved to a new directory structure on a file server, or in SharePoint Online. The file name of each linked file in each respective path is shown and represented by a row in the list.
In the last column in the list you’ll see the complete file path, which is: path + file path + file name.
By using the button Find ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) (Ctrl + B) you can search for a text in the columns and filter the list to only show the rows containing hits.
By using the Find & replace button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) (Ctrl + H) you can replace a path or file path with another path or file path on all affected rows.

#### New path
In this column you can change the path on the row. You can select among the paths registered in the Paths procedure.

#### New file path
In this column you can enter a new file path (sub-directory) to the file on the row. If the file path is a sub-directory one level down from the path, enter the name of the sub-directory in the column. If the file path comprises sub-directories on multiple levels, you enter the name of the directories separated by a slash.
For example: If it should be two levels down in a UNC path, enter "directory_level1\directory_level2". If it should be two levels down in a SharePoint Online URL path, enter "directory_level1/directory_level2".
> Please note that no check is made to ensure the sub-directories you enter exist in the path. That is, you must ensure these sub-directories already exist, or are created, with the same name and levels in which they appear here. The files must also be moved to the relevant sub-directory. It must be possible to access the files according to the path in the Complete file path column.
