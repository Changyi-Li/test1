### General

#### Status
Here you select the agreement's status. An agreement always has a specific "status", depending at what stage the agreement is in the system. When you register an agreement it will be assigned status 1 (Negotiation). The different status levels for agreements are:
- 1 Negotiation – A new agreement will be assigned this status.
- 2 Signed/Valid – The agreement has been signed and a Date of agreement is entered. When this date is entered, this status will automatically be assigned.
- 3 Active – The agreement is active. When the agreement period is started (Valid from), the system will recognize this and this status will automatically be assigned by a monitoring task run on the Monitor ERP server each night. An agreement must have this status and also contain agreement rows in order for the agreement basis (invoice basis) to be created.
- 4 Terminated – The agreement has been terminated. If you select this status for an agreement, you must also enter a Date of termination.
- 6 Closed – The agreement is closed/inactive. If you select this status for an agreement, you must also enter a Date of termination. It is possible to reactivate agreements that have this status. This is done by using the Reactivate agreement button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) next to the field.
- 9 Historical – The status of the agreement is set to historical which means it cannot be reactivated.

#### Update status automatically
If this setting is activated, the system will check the "Valid from" date in cases where the agreement has status Signed/Valid. When the Valid from date is reached, the agreement will automatically get status Active. The default value of this setting is determined in the Order types procedure.

#### Valid from
This is the date when the agreement period starts. The default value of this setting is determined in the Order types procedure. Please note! It is the "Valid from" date on the rows which determines what the agreement bases will look like and the agreement bases created based on the Valid from, when the status of the agreement has been changed to Active.

#### Valid to
Here you see/enter the last day the agreement is valid. This field is empty by default, which means the agreement applies until further notice. If you enter a "Valid to" date for the agreement period, any remaining agreement bases, will be deleted.
Agreement bases are always created when the agreement is set to "Active".
- If a Valid to is entered under the Header tab, agreement bases will be created for the entire agreement period.
- If the Valid to field under the Header tab is empty, agreement bases will be created according to the setting called Create basis for.
- When a value is entered in the Valid to field under the Header tab, it is not possible to edit the Create basis for setting.

#### Date of agreement
Here you enter the date when the agreement was signed. When this is done, the status of the agreement will be changed to status 2 (Signed/Valid). If you manually change the agreement status to 2 or higher, the Date of agreement field becomes mandatory. This field is empty to begin with.

#### Last notice of termination
Here you can enter a date which is the final day for termination of the agreement. This is required if it should be possible to start a new agreement period.

#### Date of termination
If you enter a date of termination, the status of the agreement will automatically change to status 4 (Terminated). If you manually change the agreement to status 4, it is mandatory to enter a Date of termination. This field is empty to begin with.

#### Extension period
Here you select the number of months with which the agreement should be extended once the end date (Valid to date) has been reached. This field is empty by default, which means the agreement will be extended with the same period of time as the existing entered agreement period (valid from – valid to). If you have not entered a "Valid to" for the agreement period, the Extension period field will not be available.

#### Notice period
Here you can enter a notice period for the agreement. The default value is zero months. It is not possible to enter a negative value. In the Order types procedure you can choose a default notice period for the agreement type.
If the notice period is longer than zero months and you enter a date in the "Date of termination" field, the Valid to will be calculated/entered as Date of termination + number of months entered in the Notice period field. All rows which are empty or have the same validity period as in the Header tab, will be changed to the new Valid to. (This is similar to how it works if you manually enter a “Valid to” date for the agreement.)
If the notice period is longer than zero months and you manually change the status to Terminated, the Valid to will be calculated/entered as Today's date + number of months entered in the Notice period field. All rows which do not have a validity period or have the same validity period as in the Header tab, will be changed to the new Valid to. (This is similar to how it works if you manually enter a “Valid to” date for the agreement.)

#### Create upward adjustments automatically
With this setting you decide if upward adjustments should be created automatically by the monitoring service that is run on the Monitor ERP server each night. When this setting is activated, it is still possible to create manual upward adjustments on the rows.
