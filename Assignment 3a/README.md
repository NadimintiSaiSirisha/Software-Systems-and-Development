# SSD Assignment - 3(Part A): Python

Github repository link: https://github.com/NadimintiSaiSirisha/2020201044_Assignment3a

## q1. py
* This program finds common leader of any two employees in an organization. It also gives the level of the leader from each employee, if the leader is present.
* The input is given in the file `org.json` which is present in the same folder as the program.
* Format of `org.json`:<br>
{
    "L0": [
        { "name": "001" }
    ],
    "L1": [
        { "name": "002", "parent": "001" },
        { "name": "003", "parent": "001" }
    ],
    "L2": [
        { "name": "004", "parent": "002" },
        { "name": "005", "parent": "003" },
        { "name": "006", "parent": "003" }
    ],
    "L3": [
        { "name": "007", "parent": "004" },
        { "name": "008", "parent": "004" },
        { "name": "009", "parent": "004" },
        { "name": "010", "parent": "006" },
        { "name": "011", "parent": "006" }
    ]
}
* The employees' IDs are given in a space-seperated format:<br>
<EmpId1> <EmpId2>

* The output consists of three lines if the leader is found:<br>
<Leader_ID> <br>
(Leader_ID) is  (levels)  levels above (EmpId1) <br>
(Leader_ID) is  (levels)  levels above (EmpId2) <br><br>
Example input:<br>
002 005<br>
Example output:<br>
001<br>
001 is  1  levels above  002<br>
001 is  2  levels above  005<br>

* The output consists of a single line 'Leader not found' if the common leader is not present for the pair of employees and/or if the employee is not present in the organization.<br><br>
Example input:<br>
010 111
Example output:<br>
Leader not found 

## q2. py
* This program finds the difference between given dates.
* The input is present in the file `date_calculator.txt` that must be present in the same folder as the program.
* date_calculator has the two input dates in the format:<br>
Date1: (Date1)<br>
Date2: (Date2)
* These input dates can be in the following formats:<br>
`10th September, 2020`<br> 
`10th Sep, 2020` <br>
`10/9/2020` <br>
`10-9-2020`<br>
`10.9.2020` <br>
*  The output will be stored in the file `output.txt` in the format:<br>
Date Difference: (numberDifference) Day(s)
* Example:<br>
`date_calculator.txt`:<br>
Date1: 10th September, 2020<br>
Date2: 11th September, 2020<br>
`output.txt`:<br>
Date Difference: 1 Day(s)
* The date difference is calculated using Gregorian calendar.
* The dates are assumed to be valid, i.e. dates like `29th February, 2019` are not allowed.

## q3. py
* This program takes the files `Employee1.txt` and `Employee2.txt` as inputs that contain the busy slots of each employee in ditionary format.
* These files must be present in the same directory as the running program.
* Only one date per employee file is a valid input.
* This program searches for all free slots for the given two employees and reserve the first available common slot. 
* If no common slot is available or if the dates given for the employees are different, then it prints `no slot available`. 
* The duration of the slot required is taken by the user from the console. The format of the slot duration is 0.5 ,1, 1.5,... where these numbers are taken in hours.
* The time must be given in the form: 9:00AM and NOT 09:00AM. Single digit hour must not have zero. The output also is given in the same format in case of single-digit hour.
* The output is stored in `output.txt` file in the same folder. 
* Example 1:<br>
`Employee1.txt`:<br>
{'Sai': {'5/10/2020':['10:00AM - 11:00AM', '12:30PM - 1:00PM', '4:00PM - 5:00PM']}}<br>
`Employee2.txt`<br>
{'Siri': {'5/10/2020':['10:30AM - 11:30AM', '12:00PM - 1:00PM', '1:00PM - 1:30PM',
'3:30PM - 4:30PM']}}<br>
Input of slot duration from user:<br>
1.5<br>
`output.txt`:<br>
Available slot<br>
Sai: ['9:00AM - 10:00AM', '11:00AM - 12:30PM', '1:00PM - 4:00PM']<br>
Siri: ['9:00AM - 10:30AM', '11:30AM - 12:00PM', '1:30PM - 3:30PM', '4:30PM - 5:00PM']<br>
Slot Duration: 1.5 hour(s)<br>
{'5/10/2020': ['1:30PM - 3:00PM']}<br>
* Example 2:<br>
`Employee1.txt`:<br>
{'Sai': {'5/10/2020':['10:00AM - 11:00AM', '12:30PM - 1:00PM', '4:00PM - 5:00PM']}}<br>
`Employee2.txt`<br>
{'Siri': {'5/10/2020':['10:30AM - 11:30AM', '12:00PM - 1:00PM', '1:00PM - 1:30PM',
'3:30PM - 4:30PM']}}<br>
Input of slot duration from user:<br>
4<br>
`output.txt`:<br>
Available slot<br>
Sai: ['9:00AM - 10:00AM', '11:00AM - 12:30PM', '1:00PM - 4:00PM']<br>
Siri: ['9:00AM - 10:30AM', '11:30AM - 12:00PM', '1:30PM - 3:30PM', '4:30PM - 5:00PM']<br>
Slot Duration: 4 hour(s)<br>
no slot available