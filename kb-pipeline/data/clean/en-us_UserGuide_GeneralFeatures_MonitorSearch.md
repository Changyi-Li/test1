### Monitor search
In the Monitor search field (Ctrl + F), on the title bar, you can search for records in the entire system.
> Please note! The search is performed in the company language.
A search is made for records that begin with the phrase you are searching for. If, for example, you type "123" you’ll get matches on all records that begin with "123", regardless of if it is an order number, part number, customer number, agreement number, account number, etc.
You can also search for records in a certain register by entering the register name (in English, but without the spaces) and a colon as a search phrase before what you are searching for. For example, to search for "123” in the customer order register, type "customerorder:123” in the search field.
The table below shows a list of the registers in which you can search for records using the method described above.
| Register | Search phrase |
|---|---|
| Part | part: |
| Customer | customer: |
| Supplier | supplier: |
| Customer order | customerorder: |
| Purchase order | purchaseorder: |
| Manufacturing order | manufacturingorder: |
| Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. | workcenter: |
When you have performed a search, rows containing all matches will be shown in a result window (see below). Up to 1,000 rows of matches can be shown. In the result window you have the opportunity to filter records by all data, basic data, order, supplier invoice, case, and/or voucher. You can also filter by when the records were created; anytime, today, last week, or last year. You can also filter by who created the records: anybody or you.
It is also possible to move columns in the list in the result window by dragging and dropping a column heading in between two other column headings. You can also double-click a record in the list and click on the Go to button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to open the record in the related procedure. Using the button Copy to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/button_copy.png) you copy all records in the list to Monitor's Clipboard for further use in other list procedures.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/MonitorSearchResult.png)](../../../Resources/Images/UserGuide/MonitorSearchResult.png)

#### Search using wildcards
| Expression | Explanation | Examples |
|---|---|---|
| * | Will find all words starting with the letters before the asterisk. You can use the asterisk (*) in all positions except for as the starting letter. | ca* would result in the search hits car, cabin, cabinet, but not railcar or side car. |
| ? | Will replace the letter for the specific position. | f?ll would result in fall, full, and fill. |
> Please note that rows with matches in the result window are ranked and sorted based on three criteria: Relevance – If the phrase you search for results in a perfect match, this will be ranked higher than if the phrase is only a part of the text in which a match is returned. Data type – For a part, the part number and name are ranked higher than all other fields. For a customer it is customer number and name which are ranked the highest. Role affiliation – For example, if you belong to the role Seller, customers and customer orders will be ranked higher, and if you belong to the role Purchaser, suppliers and purchase orders will be ranked higher. The purpose of this ranking and sorting is to emphasize such data which is more likely for you to search for. The number of hits will be the same regardless of these criteria. They only affect the sorting. The search indexing is updated every 10th minute to include new changes.
