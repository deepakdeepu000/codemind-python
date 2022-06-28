a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
l=0
p=''
s=''
for i in range(0,a):
    for j in range(0,a):
        if b[i]==b[j]:
            c+=1
    if c==b[i]:
        l+=1
        s+=str(b[i])
    c=0
if l==0:
    print("-1")
else:
    for i in s:
        if i not in p:
            p=p+i
    for j in p:
        print(j,end=' ')