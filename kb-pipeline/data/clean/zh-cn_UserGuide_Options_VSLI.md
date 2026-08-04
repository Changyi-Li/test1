![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Options/VSLI.png)

# WMS集成
你可以添加WMS集成选项 Monitor ERP。通过使用它，你可以在MONITOR和垂直仓储升降机的控制系统（WMS）在中间创建链接。这使得仓储和挑选更加有效。

#### 它是如何工作的？
WMS集成可以识别何时进行库存事务。然后，订单文件从MONITOR已发送到垂直仓储升降机的控制系统(WMS)，用户就可以开始完成的工作，而不必人工的输入应该已拣货的每个组件。
如果接收垂直仓储升降机和WMS处理已已发送订单的变更，则如果订单行重新计划，则任务将已更新 Monitor ERP。
如果 WMS 支持库存盘点，则会已导入该数据，并进行库存盘点 Monitor ERP
当为客户订单已拣货组件时，订单行可以直接已交货，或者余额可以从WMS的库位移动到 Monitor ERP 到线边库.在后一种案件下，必须进行交货报告 Monitor ERP。
对于采购订单，你可以到货登记订单行直接到达垂直仓储升降机的库位。
瑞典语视频，第 1组件：
瑞典语视频，第 2组件：
英语视频，第 1组件：
英语视频，第 2组件：

#### 支持的事务：
- 客户订单交货报告
- 采购订单到货报告
- 仓库订单交货及到货报告
- 计划外库存变动
- 库存盘点
- 根据工单挑选物料
- 自工单至仓库
可以根据需求集成中的特别功能。

#### 支持的 WMS
今天，该集成支持以下 WMS：
- 韦兰兹压缩商店 [https://www.welandsolutions.com/cs/](https://www.welandsolutions.com/cs/)
- TCPlus WMS (构造函数) [https://www.constructormachines.se/lagerautomater-software/tcplus-wms/](https://www.constructormachines.se/lagerautomater-software/tcplus-wms/)
- 能量 拣货 全球 （卡迪斯） [https://www.kardex-remstar.com/en/storage-retrieval-systems/software-solutions-alt/power-pick-global.html](https://www.kardex-remstar.se/se/lagerautomat/software-solution/power-pick-global.html)

#### 技术
WMS集成是你作为服务安装在MONITOR服务器或垂直仓储升降机的 WMS 上的软件，这意味着该程序将在背景运行。
在中间的通信 Monitor ERP 垂直仓储升降机的WMS采用XML文件。
有兴趣下班更多？请联系人我们的销售部门 [表格](https://www.monitorerp.com/contact-us/)。
> 此选项有单独的在线帮助站点，请点击 [这里](https://help.monitor.se/sv/MONITOR_G5_WMS/Content/Topics/GettingStarted.htm) 来访问它。
