### General reporting

#### Report material using standard unit
With this setting you decide if the parts' standard unit (default unit) should apply when reporting material. Otherwise the unit configured for each part to be used for Material withdrawal for manufacturing order will be selected. This is configured by clicking the Usage button in the Units box in the Part register procedure.

#### Exclude from automatic reporting of material
This setting is only available if you have activated the system setting Automatic withdrawal of material. With this setting you can make an exception for the work center regarding the automatic withdrawal of material when reporting an operation.

#### Exclude from automatic reporting of tools
This system setting only applies if you have installed the Tools & Maintenance option. This setting is available if the system setting Automatic reporting of tools is activated. With this setting you can make an exception for the work center regarding the automatic withdrawal of tools when reporting an operation.

#### Exclude from reporting of material at start of operation
This setting is only available if you have activated the system setting Suggest withdrawal of material at start of operation. If you activate this setting, an exception will be made for the work center regarding withdrawal of material so it will be made when the operation is reported.

#### Exclude from reporting of tools at start of operation
This setting is only available if you have activated the system setting Suggest withdrawal of tools at start of operation. If you activate this setting, an exception will be made for the work center regarding withdrawal of tools so it will be made when the operation is reported. This only applies to systems with the Tools & Maintenance option.

#### Automatic reporting of quantity and time
By activating this setting, the work center's operations will be reported automatically when the subsequent operation is being reported. The work center's operation will be reported with the same quantity as in the subsequent operation's reporting, including rejected quantity in the subsequent operation. For example if the subsequent operation reports 9 pieces and rejects 1 piece, then this operation will get 10 pieces reported. Deleting of remaining quantity is also reported in the same way. The time that will be reported is the planned time for the reported quantity. When status for the preceding work centers is checked in the Priority planning, Pool planning, Priority plan list, or Recording terminal procedures, the work centers with this setting activated, will be ignored and the status will instead be loaded from the closest preceding operation for which this setting is not activated.

#### Limit quantity for automatic material withdrawal
This determines how automatic reporting of material is managed if you use automatic reporting of material. If an automatic reporting should be carried out is determined by the Automatic withdrawal of material system setting and the Exclude from automatic reporting of material setting above. If an automatic withdrawal should be carried out, the part setting for automatic withdrawal must also allow for it.
- No, always acc. to qty reported for operation – the planned quantity will always be reported for the quantity that has been reported for the operation, regardless of whether the material has previously been reported manually. This can be used, e.g., if you do not pick material and the BOM and routing contains an error, manual reporting that does not interfere with the automatic reporting is allowed.
- Yes, not greater than what is planned for operation qty – manual reporting will be deducted from the automatic reporting. In all other respects, reporting is carried out as per above. This can be used, e.g., when the warehouse picks some of the material, but other material is reported when the operation is reported.
- Yes, not greater than planned qty on M-order – reporting stops when the remaining quantity of the M-order is zero. This alternative can be used if you use Extra % for material in the BOM and routing. For example, if you have 10% wastage (Extra %) and have planned to produce 100 parts from sheet-metal but were able to produce 103 parts.
- Yes, not greater than available balance – reporting is done automatically for the first alternative, but stops when the available balance is zero. (This alternative is mainly used for Machine integration when reporting is done outside of Monitor ERP. This means that operators are unable to correct validations when reporting. If the available balance is incorrect it can result in a lower quantity than planned being reported.)
> Alternative 3 should be used with caution, as automatic reporting of material stops when the conditions have been met.
