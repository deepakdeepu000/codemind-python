a=int(input())
b=list(map(int,input().split()))
k=sum(b)//a
s=0
for i in b:
    if k==i:
        s=1
if s==1:
    print("True")
else:
    print("False")
