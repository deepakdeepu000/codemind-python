n=int(input())
a=list(map(int,input().split()))
s=[]
f=0
for i in range(0,n):
    if a.count(a[i])==1:
        s.append(a[i])
        f=1
if (f==0):
    print("-1")
else:
    print(max(s))