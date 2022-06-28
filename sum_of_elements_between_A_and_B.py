n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
p=0
for i in a:
    if i in range(b,c+1):
        s+=i
        p=1
if p==1:
    print(s)
else:
    print("-1")