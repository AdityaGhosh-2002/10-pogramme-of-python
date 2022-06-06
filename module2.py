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
nums = input ("enter the credit card number")
a =""
for i in range(len(nums)-4):
        a = a+"*"
for i in range((len(nums)-4),len(nums)):
        a=a+nums[i]
print(a)





