n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in a:
    if i not in range(b,c+1):
        print(i,end=" ")
        s=1
if s==0:
    print("-1")