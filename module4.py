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

def strdbl(x) :
    outstr = ""
    for i in x:
        outstr += i*2
    return outstr

k = input("enter the string:")
print(strdbl(k))