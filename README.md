# hvac-control


# schedule
- Need to have a 7 day scheduler. Has no date its a monday to sunday scheduler  
- An event which falls on the set date
- Need to be able to add a recurring event with an option to trigger on next working day.


### recurring/holiday event logic

A recurring is like christmas day, so the 25th of Dec (no year is set) so the schedule will trigger on the date of the 25th of december indefinitely
If the `next_working_day` is set to true and christmas day falls on a Saturday then the schedule will also trigger on the following Monday
Logic will need to be added in the case if there is also another public holiday on the Sunday to roll over to the tuesday aswell
