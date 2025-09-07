n = int(input())
b=0
c=0
if(n<9):
    print(n)
else:
    while(n > 0):
        a = n % 10
        b=b+a
        n = int(n / 10)
    if(b>9):
        while(b>0):
            a=b%10
            c=c+a
            b=int(b/10)
        print(c)
    else:
        print(b)
