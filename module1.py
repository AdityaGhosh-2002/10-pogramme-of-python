#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adity
#
# Created:     02-06-2022
# Copyright:   (c) adity 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def sorta (nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


n= int(input("length of list:"))
nums = []
for m in range (n):
    element = input("enter the element:")
    nums.append(element)

k= input("the name of the value:")
if k == "asc" :
    sorta(nums)
    print(nums)
elif k == 'desc':
    sorta(nums)
    nums.reverse()
    print(nums)
else : print(nums)



