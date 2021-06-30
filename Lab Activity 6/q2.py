import string 
  
str =input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet: 
    if char not in str.lower(): 
        flag=0
        break
    else:
        flag=1
if(flag):
     print("YES")
else:
    print("NO")