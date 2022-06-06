#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adity
#
# Created:     03-06-2022
# Copyright:   (c) adity 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def repeat(x):
    a = len(x)
    b = []
    for i in range(a):
        k = i + 1
        for j in range(k,a):
            if (x[i] == x[j]) and (x[i] not in b):
                b.append(x[i])
    return b

y = []
p = int(input("the number of entry:"))
for i in range(p):
    q = int(input("enter the numbers:"))
    y.append(q)

print(repeat(y))