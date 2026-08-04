### Scheduling
Under this tab, you activate or deactivate the service for EIM Workflow. You also configure how often the service should be run in the time interval field.

#### Active
Here you determine if the service for EIM Workflow should be active or not.
You can trigger the service to handle incoming invoices by deactivating it and then save. Then you activate the service and save again.

#### Time interval
Here you enter a time interval that determines how often the service for EIM Workflow should handle incoming invoices in the inboxes. This way the invoices will be included in the invoice flow.

#### Workflow service – Result from latest run
In this section you can see the result of the latest run of the EIM Workflow service.
In the Status field, you see the status of the service. If no errors exist, OK is displayed in the field. Otherwise, Error is displayed in the field. You will then see an explanation for the error in the field to the right.
In the field Status of XML import, you see the status of the invoice import from the XML inbox. If no errors exist, OK is displayed in the field. Otherwise, Error is displayed in the field. You will then see an explanation for the error in the field to the right.
In the Start time field, you see the date and time of the most recent run.
In the Run time field, you see how long it took to handle incoming invoices.
In the Processed invoices field, you see how many invoices that were handled by the service in the latest run.

#### The Error messages button
When you click this button you access a log showing which invoices have been set to "pending" due to errors. The invoices will remain in the log until they either are final recorded or canceled/deleted which will remove the log record.

#### The Notify when error occurs button
Here you select recipients for any error messages. The error messages are shown as notifications for the affected users in the system.
