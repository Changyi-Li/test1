### Stop work
In this section, you will find settings referring to stop work in the recording terminal.

#### Reasonability check of excess reporting
If you activate this setting, a validation will be made that will warn or block an operation during excess reporting of quantity if the quantity exceeds the allowed excess reporting in percent.

#### Allowed excess reporting in % of planned quantity
Here you enter a limit in percent for allowed excess reporting of planned quantity in an operation.

#### Reasonability check for deletion of remaining quantity
If you activate this setting, a validation will be made that will warn for or block from deletion of remaining quantity in an operation if the quantity exceeds the allowed deletion in percent.

#### Max. deletion of remaining allowed in % of planned quantity
Here you enter a limit in percent for allowed deletion of planned quantity in an operation.

#### Enter signing employee number at machine recording
This system setting determines if it should be mandatory to also enter the operator's employee number when reporting work using the employee number of a machine. This means that when the operator loads the employee number of the machine in the recording terminal, the operator must also enter his/her employee number in a separate field. Otherwise, it will not be possible to start, partial report, or stop work. The employee number of the machine is the reporting number while the operator's employee number is the signing number (the operator who reported the recording in the machine). This will also be displayed when adjusting work as well as in the recording log.

#### Indirect work code to start when releasing order-bound work
Here you select a code for the indirect work that should be started when releasing an ongoing order-bound work item in the Authorize/Adjust recording procedure. This code is used in cases where an employee has clocked-out and still has an order-bound work item in progress, and at the same time have the Only change alternative configured. You might have to release an order-bound work item to be able to give the order the status Historical, or to make an operation available to other employees. The indirect work will start for the clocked-out employee even though the employee might not have sufficient user rights to select this code for indirect work in the recording terminal.
