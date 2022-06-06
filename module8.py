#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adity
#
# Created:     06-06-2022
# Copyright:   (c) adity 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sum_str(x):
    sum_digits = 0
    for i in x:
        if i.isdigit() == True:
            p = int(i)
            sum_digits = sum_digits + p
    return sum_digits

print(sum_str(input("enter the string:")))
