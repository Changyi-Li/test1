### Deviation model rows

#### Sequence number
The sequence of the periods that have been defined in the model. There is no limit to how many sequence numbers you can define in a model.

#### Alert threshold – upper
Deviations that exceed (increasing requirements) this upper alert threshold will trigger a deviation alert. An empty value means that the threshold is not in use. The upper alert threshold can not be lower than the upper warning threshold, and vice versa.

#### Alert threshold – lower
Deviations that exceed (decreasing requirements) this lower alert threshold will trigger a deviation alert. An empty value means that the threshold is not in use. The lower alert threshold can not be higher than the lower warning threshold, and vice versa.

#### Warning threshold – upper
Deviations that exceed (increasing requirements) this upper warning threshold will trigger a deviation warning. An empty value means that the threshold is not in use.

#### Warning threshold – lower
Deviations that exceed (decreasing requirements) this lower warning threshold will trigger a deviation warning. An empty value means that the threshold is not in use.

#### Period type
Type of period. It can be Days or Weeks.

#### Period multiple
The multiple of the period type. It must be a positive integer. The period is defined as the combination of the period type and the period multiple. This means that if the period type is "Days" and the period multiple is 2, the period will be 2 days. This is the "bucket size" for which requirements are totaled and controlled for deviations.

#### Period length
The amount of periods that the model will contain. It must be a positive integer. For the last sequence number, the period length can be left empty. This will mean that the period length will be until the end date for the delivery schedules that are being compared.
