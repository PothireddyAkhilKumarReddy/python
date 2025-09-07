n=int(input())
m=int(input())
a=min(n,m)
for i in range(1,a+1):
    if int(n%i)==0 and int(m%i)==0:
        hcf=i
print('hcf: ',hcf)
a=int((n*m)/hcf)
print('lcm: ',a)