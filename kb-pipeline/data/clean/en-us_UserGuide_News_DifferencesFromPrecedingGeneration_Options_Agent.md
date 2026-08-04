### Agent
The Agent is an option in G5 and is available to customers who in G4 has the Monitor Agent as supplement. There are two procedures belonging to the Agent: Agent tasks and Monitoring tasks. Compared to the functionality in G4, this option's functionality is similar.
All lists and the majority of the calculation procedures can be done using Agest tasks. More procedures are added continuously. Monitoring tasks can be created for balance changes, activities, operations, and arrival reporting. More options for monitoring will be added here as well.

#### Agent tasks
- One difference is that you in G5 schedule the Agent tasks directly in the procedure and they are run by the application server. In G4 the task was run by scheduled task in Windows. This means that an agent server is no longer required.
- A setting has been added where you determine if empty lists should be exported/sent in Agent tasks.

#### Monitoring tasks
- Monitoring tasks in G5 react to the actual change which is being monitored, instead of as in G4 where a check was constantly made to see if a change had been made. This way, a monitoring task in G5 will not negatively affect the performance.
