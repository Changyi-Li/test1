# WMS Integration
WMS Integration is an option you can add to Monitor ERP. By using it you can create a link between Monitor and the vertical storage lift's control system (WMS). This enables effective storage and picking.

#### How does it work?
The WMS Integration recognizes when stock transactions are to be made. An order file is then sent from MONITOR to the vertical storage lift's control system (WMS), and the user gets a complete job to start instead of manually having to enter each part that should be picked.
If the receiving vertical storage lift and WMS handle changes of orders already sent, the task will be updated if the order row is replanned in Monitor ERP.
If the WMS supports stock count, this data will be imported and the stock count will also take place in Monitor ERP
When parts are being picked for a customer order, the order rows can be delivered directly, or the balance can be moved from the WMS's location in Monitor ERP to a pick location. In the latter case, a delivery report must be made in Monitor ERP.
For purchase orders you can arrival report order rows directly to the vertical storage lift's location.
Video in Swedish, part 1:
Video in Swedish, part 2:
Video in English, part 1:
Video in English, part 2:

#### Supported transactions:
- Delivery reporting of customer order
- Arrival reporting of purchase order
- Delivery and arrival reporting of stock order
- Unplanned stock movement
- Stock count
- Picking of material for manufacturing order
- Transfer to stock from manufacturing order
Special functions in the integration can be developed on demand.

#### Supported WMS
Today the integration supports the following WMS:
- Welands Compact Store [https://www.welandsolutions.com/cs/](https://www.welandsolutions.com/cs/)
- TCPlus WMS (Constructor) [https://www.constructormachines.se/lagerautomater-software/tcplus-wms/](https://www.constructormachines.se/lagerautomater-software/tcplus-wms/)
- Power Pick Global (Kardex Remstar) [https://www.kardex-remstar.com/en/storage-retrieval-systems/software-solutions-alt/power-pick-global.html](https://www.kardex-remstar.se/se/lagerautomat/software-solution/power-pick-global.html)

#### Technology
WMS Integration is software you install as a service on your Monitor server or on the vertical storage lift's WMS, which means the program will run in the background.
The communication between Monitor ERP and the vertical storage lift's WMS takes place using XML files.
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
> This option has its own online help site, please click [here](https://help.monitor.se/sv/MONITOR_G5_WMS/Content/Topics/Home.htm) to access it.
