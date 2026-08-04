## Unattended installation of the Monitor ERP Windows client
This instruction describes the first-time unattended installation of the Monitor ERP Windows client via the installation file for the client.

### Preparations
The installation file can be found on your Monitor server in the latest version in the Monitor server folder, example of path: “C:\Program Files \Monitor ERP System AB\MONITOR Server\MONITOR Client Setup.exe”.

### Installation in Powershell:
Installation command:
$installationFolder = ”[Installation folder for Monitor ERP Windows client.]"
$licensePath = "[Path (e.g. a UNC path) to the license file.]"
$serverAddress = "[Monitor ERP server’s IP address.]"
$arguments = "-q INSTALLATION_FOLDER="$installationFolder" LICENSE_PATH="$licensePath" SERVER_ADDRESS="$serverAddress"
Start-Process -FilePath "[Path to the installation file Monitor Client Setup.exe]" -ArgumentList $arguments -Wait -NoNewWindow
With the above example of parameters, the installation command can be used as follows:
$installationFolder = "$env:localappdata\MonitorERPClient"
$licensePath = "C:\MONITOR Certificate - Perssons Mekaniska.rsa"
$serverAddress = "192.168.1.5"
$arguments = "-q INSTALLATION_FOLDER=$installationFolder LICENSE_PATH=$licensePath SERVER_ADDRESS=$serverAddress"
Start-Process -FilePath "C:\Monitor Client Setup.exe" -ArgumentList $arguments -Wait -NoNewWindow

### Installation in the command line interface (Windows)
Installation command:
“[Path to the installation file Monitor Client Setup.exe]” /quiet
INSTALLATION_FOLDER=”[Installation folder for Monitor ERP Windows client.]"
LICENSE_PATH="[Path (e.g. a UNC path) to the license file.]"
SERVER_ADDRESS="[Monitor ERP server’s IP address.]"
With the above example of parameters, the installation command can be used as follows:
“C:\MONITOR Client Setup.exe” quiet 
INSTALLATION_FOLDER="C:\Users\Administrator\AppData\Local\MonitorG5Client” 
LICENSE_PATH="C:\MONITOR Certificate - Perssons Mekaniska.rsa" 
SERVER_ADDRESS="192.168.1.5"
> Please note! If incorrect syntax is used, only a Logs folder will be created in the installation folder. Please ensure that quotation marks are used in the correct places in the command.

### Updating the Monitor ERP Windows client
If you want to manage updates of the Monitor ERP Windows client via a tool for endpoint management, e.g., Intune, you must first uninstall and then re-install the client as outlined above every time the Monitor ERP Server has been updated. Alternatively, you can give users read and write permission to the installation point to automatically update the Monitor ERP Windows client. When installing via Intune with the LocalSystem account, you need to ensure that the following folder exists and is available throughout the installation: C:\Windows\System32\config\systemprofile\Desktop.
To uninstall the Monitor ERP Windows client, use the following command:
"Monitor Client Setup.exe" /uninstall /quiet
