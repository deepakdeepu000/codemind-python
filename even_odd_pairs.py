a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
s=''
p=''
l=''
for i in b:
    if i%2==0:
        s+=str(i)
for i in b:
    if i%2!=0:
        p+=str(i)
for i in s:
    print(i,end=' ')
    for j in range(c,len(p)):
        l+=str(p[j])
        print(p[j],end=' ')
        break
    c+=1
for i in p:
    if i not in l:
        print(i,end=' ')
if a%2!=0:
    print("0",end=' ')