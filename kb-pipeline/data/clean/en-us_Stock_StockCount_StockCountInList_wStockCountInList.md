## Stock count in list
In this procedure you can create stock count basis and report stock count of multiple parts.
You first create a stock count basis for the parts that are to be inventoried/stock counted. This is done by using the Create stock count basis list type. The stock count basis is assigned a stock count number and can also be named.
With this list printed as a basis, you then perform the physical stock count. After that you report the result using another list type called Manage stock count. This will update the parts' stock balances. In the same list type you see the stock count bases which have not yet been fully reported and you can go ahead and report these or delete them. A stock transaction log and a stock count difference will be created for each part.
If a part is available in more than one location, then it is possible to have multiple stock count bases for the part. Once you have loaded the basis you can uncheck Select for the locations you do not want to include.
> If you are applying stock count approval you should use this procedure and you should limit the user rights to the Stock count procedure via the Property management.
When you create a stock count basis, it is possible to analyze the suitability of stock count for the parts by activating the Analyze suitability setting. If you choose the Sorted by suitability presentation, that setting will be activated by default. Suitability is shown in the list using a scale of 1–4. Read more about what suitability 1–4 means in the [settings](bSettingsStockCountList.htm) for the list. The parts are sorted as follows:
1. Suitability
2. Number of locations on part
3. Total balance of the part
4. Part number
> If you apply Stock count interval (entered on the ABC ABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. code in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure), you select by ABC code to load the parts which should be stock counted on a certain interval.
Under stock count
If a part has been given the status Under stock count with saved balance, the reported balance will be adjusted with the difference between the saved and the current balance. This is done in order to consider any transactions that may have taken place between the physical stock count and the registration/reporting of the stock count. However, no transactions are allowed to take place between the time when the balance is saved and the physical stock count is completed. If the part has a stock count status, it will be reset once the stock count is saved.
Read more about [Stock Count](../../../UserGuide/Using/StockCount/StockCount.htm) under Using Monitor in the online help function.
Report stock count by using Excel
It is possible to export a stock count basis from Create stock count basis, the Documents tab, and perform the stock count by filling out a .csv file.
The reporting is done via Excel and you import the .csv file back to the list called Manage stock count.
It is important that the only thing modified in the .csv file is the column for stock counted quantity. If you make changes to other columns or if you add rows, the import file will be corrupt.
Make sure that Excel will not perform any type of automatic conversion of the file whe you open it for reporting.
List types

#### Create stock count basis
In this list you create the basis of parts to stock count based on your selection of parts and locations. The list has a number of different presentations with ascending sorting by part number, location, the part's main location, part name, or corresponding descending sorting. The list also has a sorting according to sorting order by location (route sorting), as well as a sorting according to suitability for stock count.

#### Manage stock count
This list is used to report the result of the performed stock count, and to continue reporting on the bases not yet fully reported. You can also reprint stock count bases, and delete stock count bases.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
Export settings
Under Export settings in the backstage of the procedure, you can choose Column limiter and Decimal limiter for export and import of stock count basis (.csv) to/from Excel.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
