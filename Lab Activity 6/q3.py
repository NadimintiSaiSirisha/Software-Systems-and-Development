inp = input()
res = inp.split(',') 
listtemp=[]
sum=0
for i in res:
    j=''.join(a for a in i if a.isalnum())
    #print(j)
    listtemp.append(j)
bigNames=list(filter(lambda s:s[0].isupper(),listtemp))
for name in bigNames:
    sum+=len(name)
print(sum)
print(bigNames)


