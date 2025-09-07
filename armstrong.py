n=int(input())
a=0
b=0
c=n
flag=0
d=n
if(n<10):
    print('Armstrong number')
else:
    while(d>0):
        a=n%10
        flag=flag+1
        d=int(d/10)
    while(n>0):
        a=n%10
        b=b+(a ** flag)
        n=int(n/10)
    if(c==b):
        print('Armstrong number')
    else:
        print('Not a Armstrong Number')