## Formats:
# 10th September, 2020
# 10th Sep, 2020
# 10/9/2020
# 10-9-2020
# 10.9.2020

#The dates will always be valid

import sys

def getMonthNumber(monthname):
        return {
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9,
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
    }[monthname]

def replaceMonthName(dmy):
    monthName = dmy[1]
    dmy[1] = getMonthNumber(monthName[0:3])

def convertToListFormat(dateString,format):
    dmy =[]
    date=[]
    if ('/' in dateString):
        date = dateString.split('/')
        if(format =="mm/dd/yyyy"):
            dmy = [date[1],date[0],date[2]]
        else:
            dmy=date
    elif ('-' in dateString):
        date = dateString.split('-')
        if(format=="mm-dd-yyyy"):
            dmy = [date[1],date[0],date[2]]
        else:
            dmy=date
    elif ('.' in dateString):
        date = dateString.split('.')
        if(format=="mm.dd.yyyy"):
            dmy = [date[1],date[0],date[2]]
        else:
            dmy=date
    else:
        dateString = dateString.replace(',','')
        #dateString = dateString.split(' ')[0][:-2]
        dmy = dateString.split(' ')
        dmy[0] = dmy[0][:-2]
        replaceMonthName(dmy)
    #print(dmy)
    return dmy

def getNumberOfLeapYears(year,month):
    if (month <= 2):
        year = year-1
    return (year//4) - (year//100) + (year// 400)

def fromStartOfTime(date):
    totalDaysInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    numberOfYearsDays = year*365
    numberOfMonthsDays=0
    for i in range(month-1):
        numberOfMonthsDays+=totalDaysInMonth[i]
    numberOfYearsDays+=getNumberOfLeapYears(year,month)
    totalDays= day+numberOfMonthsDays+numberOfYearsDays
    #print (totalDays)
    return totalDays

# This function makes sure that date1(latest)>date2(oldest) and then calculates the difference
def getDifference(dateString1, dateString2,format):
    date1 = convertToListFormat(dateString1,format)
    date2 = convertToListFormat(dateString2,format)
    return abs(fromStartOfTime(date1)- fromStartOfTime(date2))

format = sys.argv[1]
dateInputFile = open("date_calculator.txt","r+")
date1 = dateInputFile.readline().rstrip('\n')
date2 = dateInputFile.readline()
dateInput1 = date1.split(':')[1].lstrip()
dateInput2 = date2.split(':')[1].lstrip()

dateInputFile.close()


result = getDifference(dateInput1,dateInput2,format)
resultToWriteInFile="Date Difference: "+str(result)+" Day(s)"

outputFile = open("output.txt","w")
outputFile.write(resultToWriteInFile)
outputFile.close()
print(resultToWriteInFile)
# convertToListFormat("10th Sep, 2020")

# convertToListFormat("10/9/2020")
# convertToListFormat("10-9-2020")
