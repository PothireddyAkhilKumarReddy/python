n=int(input())
a=0
b=0
while(n>0):
    a=n%10
    if(a==2 or a==3 or a==5 or a==7):
        b=b+a
    n=int(n/10)
print(b)