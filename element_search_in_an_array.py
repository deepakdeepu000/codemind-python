a=int(input())
b=list(map(int,input().split()))
c=int(input())
s=0
for i in b:
    if i==c:
        s=1
if s==1:
    print("True")
else:
    print("False")
