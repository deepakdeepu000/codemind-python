n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
f=0
t=0
sum=0
for i in a:
    for j in a:
        if i==j:
            c+=1
    if i == c:
        s.append(i)
        f=1
    c=0
if f==1:
    x=set(s)
    for i in x:
        sum+=i
        t+=1
    print("%.2f"%(sum/t))
else:
    print("-1")