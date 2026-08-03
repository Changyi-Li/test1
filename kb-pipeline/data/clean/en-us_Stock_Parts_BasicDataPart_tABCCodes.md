### ABC codes
ABC ABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts" etc.
ABC codes are used in the Volume value analysis procedure in order to calculate and analyze the parts' volume value.

#### ABC code
In this column you can enter the code, it consists of one letter. You can add new codes or edit existing codes. The pre-defined codes in the table below is included in new systems:
| ABC code | Type |
|---|---|
| A | According to selected unit |
| B | According to selected unit |
| C | According to selected unit |
| X | Price is missing |
| Y | Annual volume is missing |
| Z | Unclassified |
> Please note! The last ABC code of the Unclassified type, cannot be deleted.
There can only be one code of the type Price is missing as well as of the type Annual volume is missing.

#### Basic safety time
Here you can enter the basic safety time in number of work days. The basic safety time is used to create a safety stock in number of days per ABC code. The stock level calculation will be simplified if there are basic safety times for the ABC codes.

#### Limit %
Here you enter the limits in percent that apply to each ABC code. The total of the percentage values must be 100. Otherwise, it is not possible to save.

#### Amount limit
Here you can enter the amount limit for the volume value of the ABC code. When the amount limit is reached, the ABC code will be set for the part.

#### Amount limit exception for purchased parts
Here you can enter an amount limit exception that applies to purchased parts. The amount entered in this field overrides the value entered in the Amount limit field.

#### Type
Here you can select among the following types:
- According to selected unit – Classification is made according to percentage or amount limit.
- Price is missing – Gathers parts with annual volume greater than zero but where price is missing.
- Annual volume is missing – Gathers parts that have a price but where the annual volume is zero.
- Unclassified – New, previously unclassified parts, as well as parts where both annual volume and price are missing.
These types can then be selected for the list types Classification in the Volume value analysis procedure.

#### Stock count interval
Here you can enter a default stock count interval in months, for parts with this ABC code. However, the stock count interval can be overridden per part in the part register.
