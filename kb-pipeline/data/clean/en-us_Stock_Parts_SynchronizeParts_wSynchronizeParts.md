## Synchronize parts
This procedure is used to synchronize parts and prices for parts from a sending company to one or several receiving companies in the system. The procedure is also used together with the Customer order transfer option.
For it to be possible to synchronize parts, you must first create a setup consisting of a connection to the receiving company and a transfer profile for part synchronization. You create these in the Connections and Transfer profiles procedures.
Then you create one or several schedules for synchronizations between companies via transfer profiles. These scheduled synchronizations can be made at different times or with different intervals.
For each schedule you select a transfer profile and a selection of parts to include in the synchronization as well as the data to be synchronized. You can configure the data to be synchronized both for New part (which only exists in the sending company) and for Existing part (which exists both in the sending and the receiving company).
The synchronization is one-way in the sense that data for the parts in the sending company will update the data in the receiving company.
It is also possible to create a two-way synchronization. This is done by creating a corresponding setup for synchronization of parts in the receiving company. This means both companies will be the sending and receiving for data of the parts.
Also see: [Limitations during synchronization of parts](LimitationsSynchronizeParts.htm).
