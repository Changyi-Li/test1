### Settings for source
Here you find a description of settings regarding import via Directory, FTP, or SFTP from a selected source.
Directory settings
Settings when the type of source is Directory.

#### Path
Here you enter the path to the directory from where the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. file should be imported.

#### File name
Here you enter the name of the file that should be imported.
FTP settings
Settings when the type of source is FTP.

#### FTP server
The address to the FTP server, for example. "ftp.company.com". You do not have to use "ftp://" at the beginning of the address.

#### Port
Here you enter the port for the FTP communication. The standard port is 21 (control channel for unencrypted FTP). This is selected by default. If you select Implicit (FTPS) as encryption method below, the port should be changed to 990 (control channel for implicit FTPS).

#### Connection mode
Passive (Auto) is the default option for FTP connection and file transfer. This option works best when connecting to modern FTP servers. The other options are Passive (PASV), Passive (PASVEX), and Active. PASV and PASVEX works best when connecting to older FTP servers. Behind a firewall that uses NAT, it is normally only the Passive alternatives that work.

#### Directory listing
Auto is the default option for directory listing. This option works best when connecting to modern FTP servers. The "Auto" option will primarily use MLSD and if that does not work, LIST will be used instead. The other available options are LIST, LIST -a, and NLST. LIST works best when connecting to older FTP servers, and LIST -a will also include hidden files. NLST works best when connecting to an older and unusual FTP server.

#### Encryption method
Select if the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The default alternative is None (FTP), that is, unencrypted FTP Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21.

#### User name
Here you enter the user name for the FTP account.

#### Password
Here you enter the password for the FTP account.

#### Path
Here you enter the path to the directory from where the EDI file should be imported. Can be left empty.

#### File name
Here you enter the name of the file that should be imported.
SFTP settings
Settings when the type of source is SFTP.

#### FTP server
Here you see/enter the host name or the IP address of the SFTP server.

#### Port
Here you enter the port for the SFTP communication. Use the SSH port.

#### Authentication
Here you select the authentication method that should be used for the SFTP connection. The following options are available:
- User name and password – Authentication using a user name and a password. This option will deactivate the Key file and Key file password fields.
- Public key – Authentication using the key in the selected key file.
- User name and password + Public key – Authentication using user name, password, and the key in the entered key file.

#### User name
Here you enter the user name for the SFTP account.

#### Password
Here you enter the password for the SFTP account.

#### Key file
Here you enter/select the file name, including the path, of the file containing the authentication key.
> Use Windows generated keys, for example, according to the following:
ssh-keygen -m PEM -t rsa -b 4096 -f .\your_key.pem

#### Key file password
Here you see/enter the key file password.

#### Host key's hash fingerprint
If you leave this field empty, it will automatically be updated with the host key's hash fingerprint when the source or target is tested. If you have entered an incorrect hash fingerprint or if the host has changed its public key, you will receive a validation warning when you test the source/target, or you will get a connection error if it is run. To adjust/correct this, you should first make sure you are not subject to a man-in-the-middle attack (MITM), then empty the field and click Test to test the source/target connection. This will update the host key's hash fingerprint.

#### Connection timeout
Using this setting, you decide how long the connection should attempt to be made before timing out. Default is 10 minutes.

#### Path
Here you enter the path to the directory from where the EDI file should be imported. Can be left empty.

#### File name
Here you enter the name of the file that should be imported.
* An attack where the attacker secretly intercepts and reads messages that are then forwarded to the correct recipient, possibly with modifications. The sender and recipient think they are communicating directly with each other, but everything passes through a third party who can read and manipulate the messages.
Handling

#### File in source path
Here you configure if the import file should be deleted or not after an EDI import has been made from the source.
Blackbox

#### Active
Here you determine if a so-called "blackbox" should be used. A blackbox is an external program that converts incoming EDI messages which to Monitor's format and imports them via the channel.

#### File name
Full path name to the blackbox's program file (.exe).
If the program is installed on the Monitor ERP server, you enter the local path. For example "C:\Program Files\Blackbox_folder\Blackbox_file.exe".
If the program is installed on another server, you enter the UNC path. For example "\\Other_server\Blackbox_folder\Blackbox_file.exe".
