import json
import glob

flag = 1

def getAvailableSlotListUtility(startOfAvailable,times,availableSlots):
    slot = times.split('-')
    startTime = slot[0].replace(' ', '')
    endTime = slot[1].replace(' ', '')
    if(startTime == "9:00AM"):
        pass
    elif (startOfAvailable != startTime):
        availableSlots.append(startOfAvailable+" - "+startTime)
    startOfAvailable = endTime
    return startOfAvailable

def getAvailableSlotList(EmpDict):
    availableSlots = []
    startOfAvailable = "9:00AM"
    for key in EmpDict:
        for date in EmpDict[key]:
            dateSlot = date
            for times in EmpDict[key][date]:
                startOfAvailable = getAvailableSlotListUtility(startOfAvailable,times,availableSlots)
            if (startOfAvailable != "5:00PM"):
                availableSlots.append(startOfAvailable+" - "+"5:00PM")
    return availableSlots, dateSlot


def convertFileToDict(filePath):
    data = open(filePath, "r")
    empData = data.read()
    # print(type(data))
    dictString = empData.replace("'", '"')
    empDict = eval(dictString)
    return empDict

# returns true if time1 is earlier than time2; else returns false

def compareHourMin(hr1,hr2,min1,min2):
    if (int(hr1) < int(hr2)):
        return True
    elif(int(hr1) == int(hr2) and int(min1) < int(min2)):
        return True
    return False

def compareTimeUtility(mer1,mer2,hr1,hr2,min1,min2):
    if(mer1 == "AM" and mer2 == "PM"):
        return True
    elif(mer1 == "PM" and mer2 == "AM"):
        return False
    return compareHourMin(hr1, hr2, min1,min2)

def compareTime(time1, time2):
    listTime = time1.split(':')
    hr1 = listTime[0]
    min1 = listTime[1][-4:-2]
    mer1 = listTime[1][-2:]
    listTime = time2.split(':')
    hr2 = listTime[0]
    min2 = listTime[1][-4:-2]
    mer2 = listTime[1][-2:]
    return compareTimeUtility(mer1,mer2,hr1,hr2,min1,min2)


# Returns difference in minutes: Here, time1 is earlier than time2


def getDurationInMintues(time1, time2):
    minutes = 0
    list = time1.split(':')
    hr1 = int(list[0])
    min1 = int((list[1][-4:-2]))/60
    mer1 = list[1][-2:]
    if(mer1 == "PM" and not(hr1 == 12)):
        hr1 += 12
    list = time2.split(':')
    hr2 = int(list[0])
    min2 = int(list[1][-4:-2])/60
    mer2 = list[1][-2:]
    if(mer2 == "PM" and not(hr2 == 12)):
        hr2 += 12
    t1 = hr1+min1
    t2 = hr2+min2
    duration = t2-t1
    minutes = round(duration*60)
    return minutes


def addMinutes(startTime, duration):
    list = startTime.split(':')
    hr1 = int(list[0])
    min1 = int(list[1][-4:-2])
    mer1 = list[1][-2:]
    min1 = min1+duration
    # Wrapping around the minutes, hours and meridian
    while(min1 >= 60):
        min1 = min1-60
        hr1 = hr1+1
    if(min1 < 10):
        minString = "0"+str(min1)
    else:
        minString = str(min1)
    if(hr1 >= 12):
        merFin = "PM"
    else:
        merFin = str(mer1)
    while(hr1 > 12):
        hr1 = hr1-1
    return(str(hr1)+":"+minString+merFin)


listFiles = glob.glob("EmployeeSlots/*.txt")
noOfFiles = len(listFiles)
empDict = []
for i in listFiles:
    # list of dictionaries for each employee
    empDict.append(convertFileToDict(i))

datePrev = "0"
freeSlots = []  # list of free slots for each employee
names = []
for i in range(noOfFiles):
    names.append(list(empDict[i].keys())[0])
    f, date = getAvailableSlotList(empDict[i])
    #print("date for i: ", date)
    freeSlots.append(f)
    if(datePrev != "0" and datePrev != date):
        flag = 2
    datePrev = date
    #print("flag after comparing dates:", flag)


outputResultList = ["Available slot\n"]
for i in range(noOfFiles):
    outputResultList.append(names[i]+": "+str(freeSlots[i])+"\n")
print(outputResultList)


# Make a dict of available slot and duration
# dictDuration={}

def splitTimes(timeslot):
    tempList = timeslot.split(' - ')
    s = tempList[0].replace(' ', '')
    e = tempList[1].replace(' ', '')
    return s,e

def getMinTime(time1, time2):
    if(compareTime(time1,time2)):
        return time1
    return time2

def getMaxTime(time1,time2):
    if(compareTime(time1,time2)):
        return time2
    return time1

def getIntersection(freeSlots1, freeSlots2):
    result = []
    s = ""
    e = ""
    for i in freeSlots1:
        s1,e1 = splitTimes(i)
        for j in freeSlots2:
            s2,e2 = splitTimes(j)
            #Get maximum of s1 ans s2
            s = getMaxTime(s1,s2)
            # Get minimum of e1 and e2
            e = getMinTime(e1,e2)
            if (compareTime(s,e)):
                result.append(s+" - "+e)
    return result


# For slot duration input,
# .5 is the lowest input possible
# slots will be in multiples of 0.5. which means 0.5, 1, 1.5, 2...
freeSlots1 = freeSlots[0]
for i in range(1, noOfFiles):
    freeSlots2 = getIntersection(freeSlots1, freeSlots[i])
    freeSlots1 = freeSlots2
dictDuration = {}
for i in freeSlots1:
    s, e = i.split(' - ')
    dictDuration[i] = getDurationInMintues(s, e)

finalResult = {}
listFinal = []
slotDuration = input()
outputResultList.append("Slot Duration: "+slotDuration+" hour(s)"+"\n")
# print(type(slotDuration))

minutesRequired = int(60*float(slotDuration))
for key in dictDuration:
    if(flag == 1 and dictDuration[key] == minutesRequired):
        flag = 0
        listFinal.append(key)
    elif(flag == 1 and dictDuration[key] > minutesRequired):
        flag = 0
        startTime = key.split(' - ')[0]
        endTime = addMinutes(startTime, minutesRequired)
        listFinal.append(startTime + " - "+endTime)

if(flag == 2):
    outputResultList.append("no slot available because dates don't match")
elif (flag == 1):
    outputResultList.append("no slot available")
else:
    finalResult[date] = listFinal
    # print(finalResult)
    outputResultList.append(str(finalResult))

 # Finally write the output into file

outputFile = open("output.txt", "w")
outputFile.writelines(outputResultList)
outputFile.close()
