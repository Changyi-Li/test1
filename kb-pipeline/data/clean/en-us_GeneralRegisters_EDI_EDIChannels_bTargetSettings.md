### Settings for target
Here you find a description of settings regarding export via Directory, FTP, or SFTP to a selected target.
Directory settings
Settings when the type of target is Directory.

#### Path
Here you enter the path to the directory to which the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. file should be exported.

#### File name
Here you enter file name and file extension of the file that is being exported. The file name can contain variables according to the table below called Variables in file name.
FTP settings
Settings when the type of target is FTP.

#### FTP server
The address to the FTP server, for example. "ftp.company.com". You do not have to use "ftp://" at the beginning of the address.

#### Port
Here you enter the port for the FTP communication. The standard port is 21 (control channel for unencrypted FTP). This is selected by default. If you select Implicit (FTPS) as encryption method below, the port should be changed to 990 (control channel for implicit FTPS).

#### Connection mode
Here you select if FTP connection and file transfer should be Active or Passive. Passive is selected by default. Behind a firewall that uses NAT, only Passive works.

#### Encryption method
Select if the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The default alternative is None (FTP), that is, unencrypted FTP Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21.

#### User name
Here you enter the user name for the FTP account.

#### Password
Here you enter the password for the FTP account.

#### Path
Here you enter the path to the directory to which the EDI file should be exported. Can be left empty.

#### File name
Here you enter file name and file extension of the file that is being exported. The file name can contain variables according to the table below called Variables in file name.
SFTP settings
Settings when the type of target is SFTP.

#### FTP server
Here you see/enter the host name or the IP address of the SFTP server.

#### Port
Here you enter the port for the SFTP communication. The SSH port.

#### Connection mode
Here you select if FTP connection and file transfer should be Active or Passive. Passive is selected by default. Behind a firewall that uses NAT, only Passive works.

#### Encryption method
Select if the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The default alternative is None (FTP), that is, unencrypted FTP Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21.

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

#### Path
Here you enter the path to the directory to which the EDI file should be exported. Can be left empty.

#### File name
Here you enter file name and file extension of the file that is being exported. The file name can contain variables according to the table below called Variables in file name.
Handling

#### File in target path
Here you select if the existing export file should be deleted or if data should be added to the same file after the EDI import has been made to the target.

#### Use temporary file extension
Applies to FTP and SFTP. Here you determine if a temporary file extension should be used in the file name while the file transfer is in progress. When the file transfer is completed, the regular file extension is set according to the File name above. Temporary file extensions are used if the receiver uses a program that regularly checks and loads files via the path where you have exported the file on the FTP server. To avoid this program loading a semi-finished file during a file transfer in progress.

#### Temporary file extension
Applies to FTP and SFTP. Here you enter the temporary file extension (for example "tmp") when you have selected Yes in the setting above. You do not have to enter a period (.) in the beginning of the file extension.
Blackbox

#### Active
Here you determine if a so-called "blackbox" should be used. This is an external program which converts EDI messages that are exported from Monitor ERP via the channel to other formats.

#### File name
Full path name to the blackbox's program file (.exe).
If the program is installed on the Monitor ERP server, you enter the local path. For example "C:\Program Files\Blackbox_folder\Blackbox_file.exe".
If the program is installed on another server, you enter the UNC path. For example "\\Other_server\Blackbox_folder\Blackbox_file.exe".
Variables in file name
In the File name field under Directory settings and FTP settings, you can enter variables according to the table below.
| Variable | Explanation |
|---|---|
| {date} | Today's date |
| {datetime} | Today's date and time |
| *, {i} | Consecutive number |
| {yy} | Year with two digits |
| {yyyy} | Year with four digits |
| {MM} | Month (01-12) |
| {WW} | Week number (starting Monday) |
| {dd} | Day (01-31) |
| {HH} | Hour (24 hours) |
| {hh} | Hour (12 hours) |
| {mm} | Minute (01-59) |
| {ss} | Second (01-59) |
| {K} | Time zone |
| {company_number}, {ftgnr} | Company number |
> A tooltip is shown when you hover over the file name in the field, displaying how the file name is formatted using entered variables.
