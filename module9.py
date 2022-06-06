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

def sorta (nums1):
    nums =[int(x) for x in nums1]
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    var = ''
    for z in range(len(nums)):
        var =var + str(nums[z])
    print(var)
    return 0

popu=input("enter the string:")

sorta(popu)



