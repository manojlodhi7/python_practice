from array import *
from numpy import *
# import array as ar
# for x in range(1,21,1):
#     if (x % 3 != 0 and x % 5 !=0):
#         print(x)
# 
# 
# print("--------------------------")
# 
# for x in range(10,31,1):
#     if (x % 3 == 0 or x % 5 ==0):
#         continue
#     print(x, end =" ")
#     
#     
# print("--------------------------")
# print(math.sqrt(66))

vals = array("i", [1,2,88,3,5,7])

for i in vals:
    print(i)
    
print("--------------------------")

newArray = array(vals.typecode, (a*2 for a in vals))
for i in range(len(vals)):
    print(vals[i])
print("--------------------------")
for i in newArray:
    print(i)
    



print("--------------------------")