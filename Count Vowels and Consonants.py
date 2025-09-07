n=input()
c=0
for i in range(0,len(n)):
    if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
        c+=1
print('vowels: ',c)
print('consonents: ',len(n)-c)