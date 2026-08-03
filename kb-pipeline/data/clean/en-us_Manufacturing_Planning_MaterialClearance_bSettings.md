### Settings

#### Include
With this setting you decide if only Material, only Tools, or if both Material and tools should be included in the clearance.

#### Suggest how orders/parts/operations should be cleared
With this setting you decide how orders, parts, and operations should suggested for clearance depending of the material availability, via the different list types. The options are: With all material available, With some material available, or Do not suggest. The setting determines if the Clear checkbox should be marked by default for these rows in the Clearance status box under the Clearance tab.

#### Show material rows
This setting determines whether all the material or only material with shortage, should be displayed by default in the Material rows box under the Clearance tab. In that box it is also possible to afterwards decide if all materials or only materials with shortage should be shown. This is done using the setting Show.

#### The material's unit
This setting determines the unit that will be displayed on the material rows: the unit used at material withdrawal for the manufacturing order, or the material's standard unit. This setting will apply to all quantity/balance fields.

#### Include included order oriented M-parts
With this setting you determine if the included manufactured parts on the nodes in the order structure should be included in the clearance or not. However, the part's own included parts are always included in the clearance, regardless of this setting.

#### Optimize full clearance
When you activate this setting it means that if a material that is needed for order X is cleared but some other material for order X is not available, the material in question will be released for other orders that will be completely/fully cleared. If there are several other orders that need the same material, they are prioritized according to the following main principle: 1) operation priority, 2) requirement date, 3) order priority, 4) order ID. If there are no other orders that would become completely cleared if the material for order X is released, the clearance remains and the order is placed in section 2) Some material available in the Clearance status box under the Clearance tab.
