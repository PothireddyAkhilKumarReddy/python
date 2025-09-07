# with factorial function
# import math
# n=int(input())
# a=n
# b=0
# c=0
# d=0
# while(n>0):
#     b=n%10
#     c=math.factorial(b)
#     d=d+c
#     n=int(n/10)
# if a==d:
#     print('strong')
# else:
#     print('not strong')

#without factorial function
n=int(input())
a=n
b=0
d=0
while(n>0):
    b=n%10
    c = 1
    for i in range(1,b+1):
        c=c*i
    d=d+c
    n=int(n/10)
if a==d:
    print('strong')
else:
    print('not strong')