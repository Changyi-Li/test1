### New technical architecture
G5 is designed in a three-tier architecture: client, application server, and database server. This is a difference compared to G4 which only has two layers containing a "fat" client working toward the database server.

#### Client
In G5 the client comes in two versions: Windows client and mobile client. These clients are "thin" clients which only handles the user interface. The mobile client is run in a regular web browser. It is also available as an app for IOS and Android and it can be downloaded from Apple App Store or Google Play Store. For the mobile client and app, a special web server is included.

#### Application server
The application server (the Monitor server) is the heart of the system. It contains all business logic which decides how everything works. By centralizing this in an application server it means that different types of clients can use the same functions, and it ensures that these functions are always performed in the same way. All business transactions are handled by the application server instead of having the programs working directly toward the database.
The application server also provides better opportunities to create tasks to run automatically on the server, without having a user to do anything in the client. For example you can schedule calculations such as the net requirement calculation.

#### Database server
The database server consists of a database manager SAP SQL Anywhere or Microsoft SQL server, which is run on the same computer as the application server.
