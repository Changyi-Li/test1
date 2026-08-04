### Depreciation – Calculation examples
Examples of the different methods can be found below.

#### Declining balance depreciation
Deprecation is made based on the residual value. The system calculates and records the same value every month during the year. The depreciation for each year is based on the residual value at the start of the year. The depreciation ends when the object reaches a value which is entered in the Depreciate to residual value field, in the Register fixed assets object procedure.
- Year of purchase: 2010
- Month of purchase: October
- Purchase value: 10000
- Depreciation percent: 25%
| Year | Year | Value | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Total dep. during year | Residual value |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | 1 | 10000 |   |   |   |   |   |   |   |   |   | 208.33 | 208.33 | 208.33 | 625.00 | 9375.00 |
| 2011 | 2 | 9375.00 | 195.31 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 195.3 | 2343.75 | 7031.25 |
| 2012 | 3 | 7031.25 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 146.48 | 1757.81 | 5273.44 |
| 2013 | 4 | 5273.44 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 109.86 | 1318.36 | 3955.08 |
| 2014 | 5 | 3955.08 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 82.40 | 988.77 | 2966.31 |
| 2015 | 6 | 2966.31 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 61.80 | 741.58 | 2224.73 |
| 2016 | 7 | 2224.73 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 46.35 | 556.18 | 1668.55 |
| 2017 | 8 | 1668.55 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 34.76 | 417.14 | 1251.41 |
| 2018 | 9 | 1251.41 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 26.07 | 312.85 | 938.56 |
| 2019 | 10 | 938.56 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 19.55 | 234.64 | 703.92 |
| 2020 | 11 | 703.92 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 14.66 | 175.98 | 527.94 |
| 2021 | 12 | 527.94 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 131.98 | 395.95 |

#### Declining balance + Straight-line depreciation
The depreciation is based on the residual value at the start, and moves over to straight-line depreciation when the value reaches the point where the straight-line depreciation is higher. The method is then changed to straight-line depreciation.
In this example, declining balance depreciation takes place in the first two years. The total yearly depreciation is higher than if it would have been straight-line. In year three, the depreciation method is changed to straight-line. The depreciation ends when the object reaches its lowest residual value.
- Year of purchase: 2022
- Month of purchase: February
- Purchase value: 450000.00
- Depreciation percent (Declining balance): 40%
- Depreciation percent (Straight-line): 20%
| Year | Opening value | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Total depreciation during the year | Residual value | Depreciation method |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 450000.00 |   | 15000.00 | 15000, | 15000, | 15000, | 15000, | 15000, | 15000, | 15000, | 15000, | 15000, | 15000, | 165000.00 | 285000.00 | Declining balance |
| 2023 | 285000.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 9500.00 | 114000.00 | 171000.00 | Declining balance |
| 2024 | 171000.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 90000.00 | 81000.00 | Straight-line |
| 2025 | 81000.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 7500.00 | 81000.00 | 0 | Straight-line |
| 2026 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |   |
