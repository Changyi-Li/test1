## Connections
In this procedure you add connections to other companies in the system if you want to see stock balances for parts in other companies, apply part synchronization, and apply customer order transfer. The Customer order transfer is an option.

#### Stock balances in other companies
To be able to see stock balances in other companies, you create the connections in the company in which you want to see the balances from other companies.

#### Part synchronization
When performing part synchronization, you can update data for parts from one company (sending company) to other companies (receiving company). You create the connections for part synchronization in the sending company. In the Synchronize parts procedure you can synchronize parts between the companies. This procedure is necessary for customer order transfer.

#### Customer order transfer
When using the customer order transfer, customer order become transferred from a sales company to a production company. Then you create a connection in the sales company for the production company. This connection is transferred by the system to the production company via a transfer profile (see below), making it possible for the production company to connect to the sales company in order to transfer updates made to customer orders, order confirmations, changes and delivery of customer orders, back to the sales company.

#### How to add a connection
When you have added a row for a connection you must start by clicking the button called Load company from remote server ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) to see the companies on the remote server and to be able to select one of the companies in the Remote company field to be a receiving company or production company.
Connections that you have created will later be used in transfer profiles which you create in the Transfer profiles procedure.
