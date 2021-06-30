## Formats:
# 10th September, 2020
# 10th Sep, 2020
# 10/9/2020
# 10-9-2020
# 10.9.2020

#The dates will always be valid

import sys

def replaceMonthName(dmy):
    monthName = dmy[1]
    if(monthName=="Jan" or monthName=="January"):
        dmy[1] = '1'
    if(monthName=="Feb" or monthName=="February"):
        dmy[1] = '2'
    if(monthName=="Mar" or monthName=="March"):
        dmy[1] = '3'
    if(monthName=="Apr" or monthName=="April"):
        dmy[1] = '4'
    if(monthName=="May" or monthName=="May"):
        dmy[1] = '5'
    if(monthName=="Jun" or monthName=="June"):
        dmy[1] = '6'
    if(monthName=="Jul" or monthName=="July"):
        dmy[1] = '7'
    if(monthName=="Aug" or monthName=="August"):
        dmy[1] = '8'
    if(monthName=="Sep" or monthName=="September"):
        dmy[1] = '9'
    if(monthName=="Oct" or monthName=="October"):
        dmy[1] = '10'
    if(monthName=="Nov" or monthName=="November"):
        dmy[1] = '11'
    if(monthName=="Dec" or monthName=="December"):
        dmy[1] = '12'


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
    day1= int(date1[0])
    month1= int(date1[1])
    year1= int(date1[2])
    day2= int(date2[0])
    month2= int(date2[1])
    year2=int(date2[2])
    if(year2<year1 or (year2==year1 and month2<month1) or (year2==year1 and month2==month1 and day2<day1)):
        return (fromStartOfTime(date1)- fromStartOfTime(date2))
    else:
        # Date1 is latest, Date2 is oldest
        return (fromStartOfTime(date2)- fromStartOfTime(date1))

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
