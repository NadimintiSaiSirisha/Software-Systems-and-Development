# treat employee ID as a string
# change employee not found

import json
# Testing for json dict
# JSON is a dictionary with index as string and values as lists of dictionaries

def getPath(orgData, empID, path, start, levelEmp,finish):
    for key in orgData:
        # get the level of the empId and append the path to list
        listEmp = orgData[key]
        for i in listEmp:
            x = i['name']
            if(x == empID and finish==0):
                if(start == 1):
                    levelEmp = key
                    start = 0
                path.append(empID)
                if('parent' in i):
                   return getPath(orgData, i['parent'], path, 0, "0",0)

def getOutputUtility(j,pathOfAllEmployees,maxlength):
    firstKey = list(pathOfAllEmployees.keys())[0]
    j = j+1 #j is now the position of the leader
    offset = j-maxlength
    leader = pathOfAllEmployees[firstKey][j]
    print("common leader: ", leader )
    for key in pathOfAllEmployees:
        level = offset+pathOfAllEmployees[key][0]-1
        print("Leader ", leader, " is ", level ," level(s) above ",key)

def getLeader(j, stop,firstKey):
    while(j >= 0 and stop ==0):
        x = pathOfAllEmployees[firstKey][j]
        #print("x: ",x)
        for key in pathOfAllEmployees:
            if(pathOfAllEmployees[key][j]!=x or key==pathOfAllEmployees[key][j]):
                stop=1
                break
        if (stop==0):
            j=j-1
    return j

def getOutput(pathOfAllEmployees, maxlength):
    j = maxLength
    stop=0
    firstKey = list(pathOfAllEmployees.keys())[0]
    j = getLeader(j,stop,firstKey)
    if(j==-1):
        print("Leader not found")
        exit()
    else:
        getOutputUtility(j,pathOfAllEmployees,maxlength)

with open('org.json') as f:
    orgData = json.load(f)
# print(type(data['L1'][0]))
# print(data['L1'][0]['name'])
inputstring = input().split(' ')
numberOfEmployees = int(inputstring[0])
pathOfAllEmployees = {}
maxLength=0
for i in range(numberOfEmployees):
    path=[]
    employeeID = inputstring[i+1]
    getPath(orgData,employeeID, path,1,"0",0)
    #print(employeeID," ",path)
    if(len(path)==1):
        print("Leader not found")
        exit()
    if(len(path)>maxLength):
        maxLength = len(path)
    path.insert(0,len(path))
    pathOfAllEmployees[employeeID] = path

for key in pathOfAllEmployees:
    dummyNum = maxLength - int(pathOfAllEmployees[key][0])
    for c in range(dummyNum):
        pathOfAllEmployees[key].insert(1,"#")

#print(pathOfAllEmployees,maxLength)
getOutput(pathOfAllEmployees, maxLength)