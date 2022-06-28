n=int(input())
a=list(map(int,input().split()))
c=0
s=[]
for i in range(1,n+1):
    if a.count(i)==i:
        s.append(i)
        c=1
if c!=0:
    print(min(s),max(s))
else:
    print("-1")
    