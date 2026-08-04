## Volume value analysis
This procedure is used to analyze parts with ABCABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. code and volume value based on price an annual volume. You can also classify parts and update the parts' ABC codes in this procedure. Parts can be classified as follows:
- According to volume value %
- According to no. of parts %
- According to amount limits on volume value.

#### ABC codes
Parts with different volume values are classified using ABC codes. All ABC codes that are used must be registered in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure. You can manually register ABC codes for parts in the Part register and Part list procedures, but in this procedure the ABC codes are calculated and suggested based on the parts' volume value.
The purpose of the ABC codes is to capture as large a volume value as possible with as few parts as possible. Before you start the run, you can adjust the suggested limit values for the different classifications.
For example, the parts of the ABC code that applies for high value parts should represent 80% of the volume value, 10% of another ABC code represents parts with a little lower value, 5% of a third, 3% of a fourth and 2% of a fifth ABC code. Another way is to use amount limits during the calculation. Example: Parts with a volume value greater than 100,000 becomes A-parts. Parts with a volume value between 50,000-100,000 becomes B-parts.
During calculation, the program strives to classify parts using these shares or amount limits of the volume value as close as possible to these limit values. This is made by sorting the list by volume value in descending order. Then the rows' accumulated value is calculated. This accumulated value is then used during the classification in percent. At the same time, the program suggests the right ABC codes for the parts, based on their current volume value.
This way you can easily identify the parts that represent the largest share or portion of the volume value. Those are the parts that either have a high value, or a large annual volume, or a combination of these. ABC codes can be used as a selection term in most lists in the system. They are useful when dividing parts based on how important it is to actively working with the part.
List types

#### Show volume value
In this list you see the parts' volume value based on their annual volume and price. No new classification can be made in this list.

#### Show volume value grouped by ABC code
In this list you see the volume value grouped by ABC code based on the parts' annual volume and price. No new classification can be made in this list.

#### Classification
This list is used to classify parts according to ABC code.

#### Classification grouped by ABC code
This list is used to classify parts according to ABC code. The list is grouped by ABC code.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
