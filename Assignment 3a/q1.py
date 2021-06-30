# treat employee ID as a string
# change employee not found

import json
# Testing for json dict
# JSON is a dictionary with index as string and values as lists of dictionaries

def getPath(orgData, empID, path, start, levelEmp):
    for key in orgData:
        # get the level of the empId and append the path to list
        list = orgData[key]
        for i in list:
            if(i['name'] == empID):
                if(start == 1):
                    levelEmp = key
                    start = 0
                path.append(empID)
                if('parent' in i):
                    getPath(orgData, i['parent'], path, 0, "0")
                else:
                    return levelEmp
    return levelEmp

def getOutput(path1, path2):
    for i in range(len(path1)):
        for j in range(len(path2)):
            if(path1[i] == path2[j] and path1[i] != empId1 and path2[j] != empId2):
                leader = path1[i]
                print(leader)
                print(leader, "is ", i, " levels above ", empId1)
                print(leader, "is ", j, " levels above ", empId2)
                return
    print("Leader not found")

with open('org.json') as f:
    orgData = json.load(f)
# print(type(data['L1'][0]))
# print(data['L1'][0]['name'])
empId1, empId2 = input().split(' ')
path1 = []
path2 = []
levelEmp1 = getPath(orgData, empId1, path1, 1, "0")
levelEmp2 = getPath(orgData, empId2, path2, 1, "0")
# print(path1,levelEmp1)
# print(path2,levelEmp2)
getOutput(path1, path2)
