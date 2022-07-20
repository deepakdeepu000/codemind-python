n=int(input())
a=list(map(int,input().split()))
c=[]
f=0
for i in a:
    if a.count(i)==1:
        c.append(i)
        f=1
if f==1:
    print(*c)
else:
    print("-1")
