# 无人值守安装 Monitor ERP Windows客户端
本指导介绍了首次无人值守安装 Monitor ERP 通过 MSI包装的Windows客户端，例如通过系统 中心 配置 Manager (SCCM) 或 Intune。

## 准备工作
你应该已经通过Email已收到来自MONITOR 支持的超链接，你可以通过该链接下载MSI包装 MONITOR客户端准备Unattended.msi。
自 24.3版本释放以来， Monitor ERP 将否工作于搭载 32 位 Windows 操作系统的计算机（客户端）。这意味着你要么将系统升级到Windows 64位，要么变更为具有Windows 64位系统的计算机。

## 安装描述：
安装命令：
MONITOR客户端准备Unattended.msi /quiet INSTALLATION_FOLDER=%localappdata%\[文件夹名称] LICENSE_PATH="[文件路径]\ MONITOR认证- [系统名称].rsa" SERVER_ADDRESS=[服务器地址]
安装命令中的参数解释。
%localappdata% = 提供 Windows客户端通常安装的文件路径，即当前日程表图表:\ 用户\[användarnamn]\AppData\ 本地。
[文件夹名称] = Windows客户端的安装文件夹，例如MonitorG5Client。
[文件路径] =文件路径（例如 UNC文件路径），指向你已保存用于客户端安装的 .rsa文件的库位，例如 \\fileserver\shared_files。
[系统名称] = .rsa文件中的系统名称，例如 Perssons Mekaniska。
[服务器地址] =MONITOR服务器的IP 地址，例如 192.168.1.5。
以上面参数例如，安装命令如下：
MONITOR客户端准备Unattended.msi /quiet INSTALLATION_FOLDER=%localappdata%\MonitorG5Client LICENSE_PATH="\\fileserver\shared_files\ MONITOR认证- Perssons Mekaniska.rsa" SERVER_ADDRESS=192.168.1.5

## 更新 Monitor ERP Windows客户端
更新你想管理 Monitor ERP Windows客户端，例如 SCCM 或 Intune，时间安装之后，你第一个卸载客户端，然后按照上面重新安装。 Monitor ERP 服务器已已更新。
要卸载 Windows客户端，请使用以下命令：
msiexec /x {B446B7EF-EC5F-4D37-ACDD-87D707FBA5A9} / 数量
