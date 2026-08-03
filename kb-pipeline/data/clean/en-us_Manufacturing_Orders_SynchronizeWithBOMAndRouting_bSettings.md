### Settings

#### Pre-select
- Pre-select "Include" in Check – With this setting you decide if all rows should be pre-seleced to be included in the synchronization check, in the list at the top of the Synchronize tab.
- Pre-select "Include" in Update – With this setting you determine whether or not the "Include" box should be marked by default for all rows, to be included in the update under the Changes box, under the Synchronize tab.

#### Control of
- Operations – With this setting you decide if operations should be controlled/checked on manufacturing orders.
- Material – With this setting you decide if material should be controlled/checked on manufacturing orders.
- Tools – With this setting you decide if tools should be controlled/checked on manufacturing orders. This alternative is available if you have installed the Tools & Maintenance option.

#### Deleting of nodes with reported op.
The option called Replace planned qty with 0 makes it possible to replan nodes to 0. This can be done when a semi-finished product has been deleted in the BOM and routing, but reportings have already been made for the manufacturing order, which then prevents the node from being deleted. The following options are available:
- No – With this option you cannot delete nodes where reporting items exist.
- Always – With this option it is always possible to delete nodes, even though no reporting item has been undone.
- After "Undo reporting" – If you select this option it means that deletion of nodes is only possible to do after the reporting items have been undone.
