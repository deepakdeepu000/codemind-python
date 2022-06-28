n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
p=0
for i in a:
    if i not in range(b,c+1):
        s.append(i)
        p=1
if p==1:
    print(max(s))
else:
    print("-1")