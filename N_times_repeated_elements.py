n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
s=[]
for i in range(1,n+1):
    if a.count(i)==b:
        c=1
        s.append(i)
if c==1:
    print(*s)
else:
    print("-1")