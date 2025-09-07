n=int(input())
even=0
odd=0
for i in range(2,n+1):
    if(n%i==0):
        if(n%2==0):
            even=even+1
        else:
            odd=odd+1
if(even==1):
    print('even prime')
elif(odd==1):
    print('odd prime')
else:
    print('not prime')