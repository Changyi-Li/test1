### Location selection and filtering formula

#### Planning formula
The formula is made up of the different measurements and weights for the entered location and part. The formula compares the sizes of the location with the size of the part. Here, you are able to customize a rule so that there is a tolerance level for the maximum size of the location. E.g., if a certain type of part should be able to be picked off a pallet without pulling the pallet out of the pallet rack. Then you should leave sufficient space on the maximum height. The planning formula will give a "true/false" answer to the question "Will the part fit on the shelf?". You can find these planning formulas in the Planning formulas procedure in the General registers module.
The following variables can be used in planning formulas in the locations filter for putaway:
| Code | Name | Updated in procedure |
|---|---|---|
| LCAP | Location’s max. load | Locations |
| LMAXH | Location’s max. height | Locations |
| LMAXL | Location’s max. height | Locations |
| LMAXW | Location’s max. width | Locations |
| LMINH | Location’s min. height | Locations |
| LMINL | Location’s min. length | Locations |
| LMINW | Location’s min. width | Locations |
| PACKH | Height of the packaging | Part register |
| PACKL | Length of the packaging | Part register |
| PACKW | Width of the packaging | Part register |
| PACKWGT | Weight of the packaging | Part register |

#### Selection criteria
The location selection can be combined with a selection criteria on location and putaway strategy if so needed. E.g., a part should always be stored in section "B". You can in that case create a filter to always look for a location in that specific segment.

#### Putaway strategy
In the putaway strategy, the order in which the locations are suggested is decided. The most suitable option is shown first, which is going to be the location/s where the material is put
It’s recommended that you sort as per the coordination system which is set for the basic type, e.g., if you want to load/fill from the floor up, you enter increased sorting on "level".
Another sorting term which can be worth noting is Route sorting. Route sorting will configure a sorting method for all location for the planned "route" which makes it easier for the person doing the picking, that all locations are in the correct picking order if the location name is different from what is best logistically.
If it is a part which has a refill location, you can decide that the refill location should be restocked if the current balance is below the entered refill quantity.
If the part has an arrival location which is to be used, this can be taken into account so that the arrival goes primarily to the arrival location. If the part is in the arrival location and should be moved with the help of the Move stock balance procedure, the system will suggest another location.
> Please note! You can create multiple putaway strategies to get the desired flexibility and functionality
