## Calculate weight
This procedure is used to calculate net weights for multiple structure parts at a time. Manufactured and fictitious parts are included in the list by default, but you can also include purchased parts.
The net weight of a structure part in the list is calculated as the total of its included (incorporated, underlying) parts' net weights. These are the parts that are included in the material rows list in the BOM and routing procedure.
You can also choose to recalculate the net weights for the parts in underlying levels, before their net weights are added together to the total net weight of the structure part. A fixed net weight can be configured for parts. For those parts the net weight will not be recalculated.
You can also enter different terms. This way you will only include the underlying parts which have those terms selected on material rows, in the calculation.
Tools on material rows will not be included in the net weight calculation (applies when the Tools & Maintenance option is installed).
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
