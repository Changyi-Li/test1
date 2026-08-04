### Change password for ReadOnlyUser
> This only applies if you use SQL Anywhere.
Under the Database access tab you find this box where you can configure a or change password for the SQL Anywhere database user called ReadOnlyUser.
> Fact box: The ReadOnlyUser has read permissions in the database. This is used if you load data from Monitor ERP to another application via an ODBC data source in Windows. The ReadOnlyUser can create "Procedures" and "Functions", run "Query functions", create own tables, and create/update/delete views in the database.

#### New password
Here you enter the new password. The password must at least be 10 characters. It must contain a minimum of one digit, one upper-case letter and one lower-case letter, as well as at least one special character.

#### Confirm new password
Here you enter the new password one more time.
By using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) on the toolbar of the procedure, you apply the new password or execute the change of password. The first time you create/enter the password, the database user will also be created.
> Please note! Keep track of the password you select for the ReadOnlyUser.
