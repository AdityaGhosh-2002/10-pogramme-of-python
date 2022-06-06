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

if __name__ == '__main__':
    a,b,i,j,c = 0,0,0,0,0
    print("the lower boundary of the range:", end="")
    a=int(input())
    print(a)

    print("the upper boundary of the range:", end="")
    b=int(input())
    print(b)

    print("the prime numbers in the range between", a, "and", b, "are:", end ="")

    for i in range(a, b+1):
        if( i == 1):
            continue
        c = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                c = 0
                break

        if (c == 1):
            print(i, end = " ")

