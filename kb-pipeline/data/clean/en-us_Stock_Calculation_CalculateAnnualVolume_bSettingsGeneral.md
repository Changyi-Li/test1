### Settings – General

#### Save to
Does not apply to the Loading list type. With this setting you decide what you want to save to: Annual volume or to Annual volume, current pace. The latter option is only displayed if you have activated the Show annual budget, annual volume, and order quantity with current pace system setting.

#### Number of decimals
The default option here is 2 decimals. It is possible to use between 0 and 8 decimals.

#### Cost factors
Applies to the list types: Loading, Simulation. Here you select the costs for operations that should be included in the calculation. The costs that are selected in the system setting Default cost factors will here be shown as default.

#### Include transport cost
Applies to the list types: Calculate annual volume – Detailed, Loading, Simulation. With this checkbox you decide if transport cost should be included. If you have checked this box, there will be as many freights as there are setup costs.

#### Include SO mark-up
Applies to the list types: Calculate annual volume – Detailed, Explosion, Simulation. With this checkbox you determine if SO mark-up (storage overhead mark-up) should be included in the calculation.

#### Include SO mark-up
Applies to the list types: Calculate annual volume – Detailed, Loading, Simulation. With this checkbox you determine if SC mark-up (subcontract cost mark-up) should be included in the calculation. For subcontracts, only costs will be displayed. Setup costs and Unit costs are calculated in a similar way as for other operations, taking the order quantity into consideration. If you have selected to include SC mark-up, it will be added according to each part's own mark-up.

#### Fallback quantity
Does not apply to the list types: Update annual volume and Reset annual volume. If order quantity is missing for a part, you can here enter a fallback quantity that will be used instead when calculating.

#### Consider maximum quantity
Applies to the list types: Calculate annual volume – Detailed, Explosion, Loading, Simulation. Here you decide if the maximum quantity should override the order quantity, that is, if the maximum quantity is lower and not zero.

#### Show unchanged zero records
Applies to the Update annual volume list. Here you decide if you want to show parts with zero in quantity as both old and new quantity.

#### Show zero records
Applies to the list types: Update annual volume, Explosion, Loading. With this setting you decide if parts which get 0 (zero) as result, should be displayed and be possible to update.

#### Pre-select "Include"
Does not apply to the Simulation list type. This setting determines whether or not the “Include” box should be checked by default for all rows.

#### Include exploded structure
Applies to the Loading list type. If there is an annual volume on a part that is contained in a different structure, Monitor ERP will calculate the loading time twice for this part. Once for the annual volume for the part, and once for the loading time of the entire structure for the main part. This will result in a higher loading than necessary. This setting determines how this will be handled.
The setting is deactivated by default, so unless you activate it, the structure will not be exploded and only the main parts will be shown. Loading is only calculated for the top level.
If the setting is activated, the structure will be exploded and loading will be calculated for all levels in the structure.
