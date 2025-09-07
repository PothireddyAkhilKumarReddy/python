#using for loop
# n=int(input())
# b=0
# for i in range(2,n+1):
#     c=0
#     for j in range(2,i+1):
#         if i%j==0:
#             c=c+1
#     if c==1:
#         b=b+i
# print(b)
#using while loop
n=int(input())
b=0
while n>1:
    c=0
    for j in range(2,n+1):
        if n%j==0:
            c=c+1
    if c==1:
        b=b+n
    n=n-1
print(b)