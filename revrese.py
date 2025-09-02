n="691array_1.py"
res=""
count=0
dic={"1":"1","0":"0","8":"8","6":"9","9":"6"}
for i in range(len(n)-1,-1,-1):
    if n[i] in dic:
        res+=dic.get(n[i]) 
    else:
        count=1
        break
if count==0 and res==n:
    print("True")
else:    
    print("False")