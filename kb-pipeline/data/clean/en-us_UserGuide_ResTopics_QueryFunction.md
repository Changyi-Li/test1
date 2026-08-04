### The Query function
How do I use the Query function?

#### The query function is available from version 24.7. The function receives two parameters, a date and a [timezone](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones?view=windows-11) (Timezone).
SafeGetLocalTime(DateColumn, 'Timezone')
Below you can see an example of how the Query function works:

#### What happens if null is sent as a timezone?
If null is sent as a timezone parameter to the query function, the database server's timezone will be automatically assigned.
Does the query function affect performance?
> For SQL Anywhere performance is affected when the query function is applied to the DateTime data type. For 28 million DateTime dates, roughly 3 minutes are added to the response time. Other database engines are affected minimally by the Query function.

#### What data types are used by the Query function?
Input
- Output
Copy
```
SELECT OrderDate FROM monitor.CustomerOrderSELECT monitor.SafeGetLocalTime(OrderDate, null) FROM monitor.CustomerOrderSELECT monitor.SafeGetLocalTime(OrderDate, 'W. Europe Standard Time') FROM monitor.CustomerOrder
```

#### DateTimeOffset
DateTime
Date

#### DateTime
DateTime

#### Converting to local time (DateTime)
| When can the query function be added in adaptations or integrations? | The Query function will work for date regardless of whether the current or updated data type is being used. This means that the Query function can proactively be used in order to make it easier when changing over to the updated data type. |
|---|---|
| DateTimeOffset | DateTime |
| Date | DateTime |
| DateTime | Converting to local time (DateTime) |

#### When can the query function be added in adaptations or integrations?
The query function will work for dates regardless of whether they have the current or updated data type. This means that the query function can be used proactively to make it easier for when the dates are updated.

#### What know-how and rights are needed to be able to update adaptations or integrations?
To update adaptations or integrations you need access to its SQL and know how to write SQL queries.

#### When can integrations or adaptations be adjusted?
Adjustments to SQL queries for adaptations and integrations can be made from version 24.7.
SQL queries for customized documents and reports can be adjusted while being used. Please note that the change is applied as soon as you save. For other adaptations and integrations, the business needs to decide whether SQL queries can be adjusted while being used.

#### How can we get help to update an adaptation or integration that does not have a Support and Update Agreement?
An adaptation or integration that does not have a Support and Update Agreement can be updated by our adaptations department. You can contact them on [adaptation@monitor.se](mailto:adaptation@monitor.se) and enter your contact information and a description of the background and purpose of the adaptation or integration. You will then be contacted by a member of the adaptation department that has created a quote of how much it will cost to upgrade the adaptation and the price of a Support and Update Agreement for the adaptation in question. Regular delivery times apply.

#### How long do the updates take?
Update time vary depending on multiple factors such as the size of the database and the number of databases to be updated. We recommend planning for the process taking longer than usual.
Hopefully this information will help make changing over to the new versions as easy as possible.
