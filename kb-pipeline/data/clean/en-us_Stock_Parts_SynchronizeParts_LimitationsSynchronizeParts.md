### Limitations during synchronization of parts
The synchronization of parts between a sending company and a receiving company has certain limitations that are good to be aware of. These limitations are described here.

#### What type of data can be synchronized?
In the Fields to synchronize box in the procedure you find a list of the data which can be synchronized for existing parts and/or new parts that are created in the receiving company at the synchronization. Other data for the parts is not synchronized.

#### Delete parts
If you delete a part in the sending company, the part will not be deleted in the receiving company.

#### Rename part
If you give the part a new part number in the sending company, a new part with the new number will be created in the receiving company. This means that both the old part number and the new part number exist in the receiving company.
If the receiving company then creates a customer order with the old part number, a warning appears informing you that the part is missing in the sending company (where the part was renamed). You then have to manually change to the new part number on the order.

#### Translation of names
- If both companies have the same company language, the part name will be synchronized to the same language in the receiving company.
- If the companies have different language, the part's translated name in the sending company's company language will be synchronized to the receiving company.
-    
If no translation exists, the part name in the sending company’s company language will be synchronized. See the table below.
| Sending company (SV) | Translations | -> | Receiving company (EN) | Synchronized translation |
|---|---|---|---|---|
| Part number | 10001 |   | 10001 |   |
| Name (SV) | Plåtburk |   | Name (EN) | Tin |
| Name (EN) | Tin |   |   |   |
| Part number | 10002 |   | 10002 |   |
| Name (SV) | Kakburk |   | Name (EN) | Kakburk |
| Name (EN) | - |   |   |   |

#### Part status
If a selection has been made by Status, the following may occur:
1. All parts with status 3 will be synchronized from the sending company to the receiving company.
2. The status for part A is then changed to 4 in the sending company.
3. A new synchronization is made for all parts with status 3.
4. Part A in the receiving company still has status 3. This is because part A has been given status 4 in the sending company. This part will then not be included in the part selection that is synchronized.
