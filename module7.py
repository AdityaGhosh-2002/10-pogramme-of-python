#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adity
#
# Created:     05-06-2022
# Copyright:   (c) adity 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
y = []
p = int(input("the number of entry:"))
for i in range(p):
    q = int(input("enter the numbers:"))
    y.append(q)

print("original list :" + str (y))

x=0
max=0
for i in y:
    if(y.count(i)>max):
        x=i
        max=y.count(i)
print(x)

