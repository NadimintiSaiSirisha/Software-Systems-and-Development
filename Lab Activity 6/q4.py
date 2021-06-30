inp = input()
res=''
listInp = inp.split(',')
for i in listInp:
    dec = int(i,2)
    if (dec%5==0):
        res+=i+','
res=res[:-1]
print(res)