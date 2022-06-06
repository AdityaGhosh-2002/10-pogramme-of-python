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

a=int(input("input the first number"))
b=int(input("input the second number"))
c = ""
k=input("the name of the mathematical operator:")
if k == "+" :
    c = a+b
elif k == "-" :
    c = a-b
elif k == "/" :
    c = a/b
elif k == "." :
    c = a*b

print(c)
