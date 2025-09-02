"""array=[1,2,3,4]
n=5
pos=1
num=n
array.append(None)
for i in range(pos,len(array)):
    temp=array[i]
    array[i]=num
    num=temp
print(array)"""

import array
num=array.array('u',['a','b','c','d'])
n=num.pop()
print(n)
for i in range(len(num)):
    print(num[i])