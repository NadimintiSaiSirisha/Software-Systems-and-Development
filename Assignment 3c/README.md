# SSD Assignment - 3(Part B): Python

Github repository link: https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a<br>
Branch for Part C: https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a/tree/PartC

## q1. py
* I modularised the `getOutput` function into `getLeader[Line 32]` and `getOutputUtility [Line 22]`  functions.

Output of `radon cc q1.py -na -a` :
![radon output for q1.py](https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a/blob/PartC/q1.png)

## q2. py
* I added `getMonthNumber [Line 12]` function to convert the monthnames into months with minimum complexity.<br>
Note: Give `""` in the commandline if the dates are in the form of: 10th September, 2020 or 10th Sep, 2020.

Output of `radon cc q2.py -na -a` :
![radon output for q2.py](https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a/blob/PartC/q2.png)

## q3. py
* I added the `getAvailableSlotListUtility [Line 6]` function to append the available slots to the list.
* I divided the `compareTime` function into `compareTimeUtility [Line 47]` (that compares the meridians) and `compareHourMin [Line 40]` (that compares the hours and minutes).
* I added `splitTimes [Line 143]` to split the slot (9:00AM - 9:30AM) into start time and end time (9:00AM, 9:30AM).
* I added `getMinTime [Line 149]` and `getMaxTime [Line 154]` to get the oldest and latest times respectively out of two input times given.

Output of `radon cc q3.py -na -a` :
![radon output for q3.py](https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a/blob/PartC/q3.png)