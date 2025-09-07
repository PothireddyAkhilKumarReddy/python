n=int(input())
a=n
for i in range(1,n+1):
    for j in range(1,a+1):
        print(j,end=" ")
    a=a-1
    print()