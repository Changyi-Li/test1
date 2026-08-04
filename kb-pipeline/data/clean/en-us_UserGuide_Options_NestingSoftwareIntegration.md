# Nesting Software Integration
Nesting Software Integration is an option for Monitor G5 that allows you to transfer information between Monitor and a nesting system. This enables better production planning and makes it easier to keep track of material consumption.

#### Technology
The Nesting Software Integration is installed as two services on your Monitor server; one for the mobile client, and one for the integration. The mobile client is internal, and used to configure various settings for the integration.
The communication between Monitor and the nesting program takes place via XML files.

#### Export
The integration recognizes when an operation is created for a selected production group/s, and sends an order file to the receiving nesting system. The operator will then see this operation in their list of tasks in the nesting system. You can also export operations manually using BAP – Business adaptation plugins.
If the quantity or date is changed on the operation in Monitor, the information is sent over and updates the operation in the nesting system as well. If the operation is removed in Monitor, it will also be removed in nesting program.
The following fields can be exported from Monitor:
- The operation’s report number
- The manufacturing order’s report number
- Planned start date
- Planned finish date
- The manufactured part’s number and name
- The material’s part number and name
- The current part revision
- The drawing number
- The material’s batch number
- The customer in Monitor
- The customer’s order number in Monitor.

#### Import
When a nest has been cut, the nesting system reports back to Monitor, and reports to every operation included in the nest. You can also update the BOM and routing for the manufactured part with information from the nest.
If the material reported differs from that which is actually used, upon integration the import will reset the original material requirement, set up a new one with the new material, and then report. This can happen when different part numbers occur for the same type of material, for example, different sizes.
The following can be reported:
- Quantity
- Unit time
- Setup time
- Material usage per detail
- The material's unit
- BatchA batch is the set of components/products manufactured at the same time and made from the same original material. (Material)
- Material waste

#### Part import
It is possible to import part data from the nesting program and then create/update parts in Monitor, as well as create/update operations and material rows in the BOM and routing for the part.
This provides more accurate pre-calculations, which thereby leads to a better overview of production and costs.
The part data that can be imported is as follows:
- Part number and name
- Unit time
- Setup time
- The material's part number
- Material per detail
- Here you can see the unit of the material.
It’s also possible to import data for punching/bending, if it can be exported by the nesting system.

#### Nesting program supported at present
| Supplier | Address | Contact | Information |
|---|---|---|---|
| Bystronic BySoft CAM | [Link](https://www.bystronic.se/se/Produkter/programvara/BySoft-CAM.php) | Chris Waters | Software Specialistchris.waters@bystronic.com | To be able to fully use the functionality in the integration, the Plant Manager module in BySoft CAM is required. It is possible to use part import without Plant Manager. In this case, the Part Nester module is required. |
| TRUMPF TruTops Boost | [Link](https://www.trumpf.com/sv_SE/produkter/mjukvara/programmeringssystem/trutops-boost/) |   |   |
| Hexagon RADAN Radnest (MAZAK) | [Link](https://www.radan.com/combination/radanradnest) |   |   |
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
