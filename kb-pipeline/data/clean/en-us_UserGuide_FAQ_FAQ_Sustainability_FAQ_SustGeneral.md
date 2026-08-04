### FAQ – General questions Sustainability (Sustainability by Monitor)
Here you find answers to questions asked by our customers at our webinars about sustainability.
Is the sustainability functionality (Sustainability by Monitor) included as standard?
Yes, this is standard functionality included as of version 23.6 of Monitor ERP. There is no extra charge for this functionality.
Do I have to download the data myself for emission factors or is it possible to connect via API to load the data automatically?
Currently, you download the data yourself and import it via the Import sustainability data procedure. We are looking at solutions via API.
Is the reliability index something you come up with yourself or are there any guidelines for this?
You determine the reliability index and how you want to use it yourself. The reliability index is there so you can evaluate how reliable you believe the information source where you have found your sustainability data to be. If you, for example, received data directly from the supplier, the data should be considered reliable. The number is entered with decimals within the interval 0-1.
Is it only CO2e that will be required in the upcoming legislation?
Other greenhouse gases must be converted to CO2e when you create sustainability reports according to the reporting standard, ESRS (European Sustainability Reporting Standards), as of 2026.
We have a product where the emission factor changes per month. How is this handled in Monitor?
New calculations can be made monthly if the calculation basis is changed. So far, there isn’t support for handling factors per batch or the like, but this type of functionality might be added in the future. If it is a purchased part with a variable factor, you can save the factor per arrival in the log.
Is it possible to register data for, e.g., 2020, 2021 and 2022, to see the development of the overhead?
Yes, in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Sustainability procedure, you can enter emission data for previous years.
Is there a simple checklist of which fields in Monitor should be filled in for the calculation to work as intended?
There are warnings shown in the sustainability calculation which can be used as a basis for knowing which data is "missing" and should be added.
Where can I find the company's total emission for the year?
The company's total annual emission is shown in the Basic data – Sustainability procedure.
What should we include in process and what should go into overhead? Should tools, process chemicals, etc. go as overhead or should they be included in the process?
There are two factors for the centers in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register. One for Power and one for Other emissions so you can add LPG etc. as an other emission. Everything that you do not enter under the Expenses tab is regarded as overhead.
Which rights are needed to access the Sustainability menu?
You need to have user rights to Pre-calculation in the Manufacturing module and also the right to Modify the part in the Stock module to get access to the sustainability functionality. You determine the user rights in the Users procedure.
Can I use data only from Scope 1 and 2 or does Scope 3 also need to be updated? (I am currently only using Scope 1 and 2.)
You can start with Scope 1 and 2, but the calculation will not be complete if you leave out Scope 3.
What do I do if there are several demanders/authorities for the same material?
You can link multiple demanders/authorities in the Part register procedure under the Sustainability tab, in the Reporting requirements box.
