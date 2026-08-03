## Rules for prioritizing locations at withdrawal to manufacturing order
In Monitor ERP, the following rules apply regarding how locations are suggested and displayed during withdrawal to manufacturing order. The locations are prioritized and sorted according to the following rules.
If the system setting Apply pick location is activated and a pick location or a pick location for work center is selected, all reporting of non-traceable materials will be reported from the pick location, regardless of the balance.
1. Locations with cleared balance.
2. Project balance. (Part traceability is required)
3. Location that is a pick location for work center with high priority in the Work center A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register.
4. Location that is not a pick location for work center with high priority in the Work center register.
5. Location that is entered as pick location in the Part register.
6. Locations that are not entered as pick location for work center in the Part register.
7. Locations that are entered as pick location for work center in the Part register.
8. Locations with low priority that are entered as pick location for work center in the Work center register.
9. Locations with low priority that are not entered as pick locations in the Work center register.
If there are many options within one of the above categories, the following applies:
1. Priority entered on work center in the Part register. (ascending)
2. Best-before date (if it has been activated) The closest best-before date will be consumed first.
3. Last arrival date. For locations with the same or no priority, the locations will be sorted by age in ascending order. The oldest Last arrival date will be consumed first.
4. The location’s ID (if the part has been arrival reported to multiple locations simultaneously).
You can read more here: [Clearance of part and location](PartAndLocationClearance.htm)
