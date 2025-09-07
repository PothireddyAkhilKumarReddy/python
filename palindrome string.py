# # slicing
# n=input()
# print(n==n[::-1])
# without slicing
n=input()
a=len(n)
i=0
flag=0
while a>0:
    if(n[a-1]==n[i]):
        i=i+1
        flag = flag + 1
    a = a - 1
if(flag==len(n)):
    print('palindrome')
else:
    print('not palindrome')