import json 

def getAvailableSlotList(EmpDict):
    availableSlots=[]
    startOfAvailable="9:00AM"
    for key in EmpDict:
        for date in EmpDict[key]:
            dateSlot=date
            for times in EmpDict[key][date]:
                slot = times.split('-')
                startTime = slot[0].replace(' ','')
                endTime = slot[1].replace(' ','')
                if(startTime=="9:00AM"):
                    pass
                elif (startOfAvailable!=startTime):
                    availableSlots.append(startOfAvailable+" - "+startTime)
                startOfAvailable = endTime
            if (startOfAvailable!="5:00PM"):
                availableSlots.append(startOfAvailable+" - "+"5:00PM")
    return availableSlots,dateSlot

def convertFileToDict(filePath):
    data = open(filePath,"r")
    empData =data.read() 
    #print(type(data))
    dictString=empData.replace("'",'"')
    empDict = eval(dictString) 
    return empDict

# returns true if time1 is earlier than time2; else returns false
def compareTime(time1, time2):
    list=time1.split(':')
    hr1 = list[0]
    min1 = list[1][-4:-2]
    mer1 = list[1][-2:] 
    list=time2.split(':')
    hr2 = list[0]
    min2 = list[1][-4:-2]
    mer2 = min2[-2:]
    if(mer1=="AM" and mer2=="PM"):
        return True
    elif(int(hr1)<int(hr2)):
        return True
    elif(int(hr1)==int(hr2) and int(min1)<int(min2)):
        return True
    return False   

#Returns difference in minutes: Here, time1 is earlier than time2
def getDurationInMintues(time1,time2):
    minutes =0
    list=time1.split(':')
    hr1 = int(list[0])
    min1 = int((list[1][-4:-2]))/60
    mer1 = list[1][-2:] 
    if(mer1=="PM" and not(hr1==12)):
        hr1+=12
    list=time2.split(':')
    hr2 = int(list[0])
    min2 = int(list[1][-4:-2])/60
    mer2 = list[1][-2:]
    if(mer2=="PM" and not(hr2==12)):
        hr2+=12 
    t1 = hr1+min1
    t2 = hr2+min2
    duration = t2-t1
    minutes = round(duration*60)
    return minutes


    
def addMinutes(startTime, duration):
    list=startTime.split(':')
    hr1 = int(list[0])
    min1 = int(list[1][-4:-2])
    mer1 = list[1][-2:] 
    min1 = min1+duration
    #Wrapping around the minutes, hours and meridian
    while(min1>=60):
        min1=min1-60
        hr1=hr1+1
    if(min1<10):
        minString = "0"+str(min1)
    else:
        minString =str(min1)
    if(hr1>=12):
        merFin="PM"  
    else:
        merFin = str(mer1)  
    while(hr1>12):
        hr1=hr1-1
    return(str(hr1)+":"+minString+merFin)




empDict1 = convertFileToDict("Employee1.txt")
empDict2 = convertFileToDict("Employee2.txt")

for key in empDict1:
    empName1 = key
for key in empDict2:
    empName2 = key
#print(empName1)
#print(empName2)

date1 ="0"
date2="0"
freeSlots1,date1 = getAvailableSlotList(empDict1)
freeSlots2,date2 = getAvailableSlotList(empDict2)


#print(str(freeSlots1))
#print(str(freeSlots2))

outputResultList=["Available slot\n",empName1+": "+str(freeSlots1)+"\n" ,empName2+": "+ str(freeSlots2)+"\n"]

# Make a dict of available slot and duration
dictDuration={}
if(date1==date2):
    for i in freeSlots1:
        tempList = i.split(' - ')
        s1=tempList[0].replace(' ','')
        e1=tempList[1].replace(' ','')
        for j in freeSlots2:
            tempList = j.split(' - ')
            s2= tempList[0].replace(' ','')
            e2=tempList[1].replace(' ','')
            #Overlapping
            if(compareTime(e1,s2) and compareTime(s2,e1)):           
                dictDuration[e1+" - "+s2]= getDurationInMintues(e1,s2)
        
        #Completely contained time slots
            elif(not(compareTime(s1,s2)) and not(compareTime(e2, e1)) and compareTime(s1,e1)):           
                dictDuration[s1+" - "+e1]= getDurationInMintues(s1,e1)
           # s1<=s2 and e2<=e1 and s2<e2
            elif(not(compareTime(s2,s1)) and not(compareTime(e1,e2)) and compareTime(s2,e2)):
            # dur = endTime2-startTime2
                dictDuration[s2+" - "+e2]= getDurationInMintues(s2,e2)
    #print(dictDuration)
            



# For slot duration input, 
# .5 is the lowest input possible 
# slots will be in multiples of 0.5. which means 0.5, 1, 1.5, 2...

    finalResult={}
    listFinal=[]
    slotDuration = input()
    outputResultList.append("Slot Duration: "+slotDuration+" hour(s)"+"\n")
    #print(type(slotDuration))
    flag=1
    minutesRequired = int(60*float(slotDuration))
    for key in dictDuration:
        if(flag==1 and dictDuration[key]==minutesRequired):
            flag=0
            listFinal.append(key)
        elif(flag==1 and dictDuration[key]>minutesRequired):
            flag=0
            startTime= key.split(' - ')[0]
            endTime = addMinutes(startTime,minutesRequired)
            listFinal.append(startTime + " - "+endTime)

    if(flag==1):
        outputResultList.append("no slot available")
    else:
        finalResult[date1]=listFinal
        #print(finalResult)
        outputResultList.append(str(finalResult))
else:
    outputResultList.append("no slot available")
    #print("no slot available")        

#print(type(slotDuration))

#Finally write the output into file
outputFile = open("output.txt","w") 
outputFile.writelines(outputResultList)
outputFile.close()