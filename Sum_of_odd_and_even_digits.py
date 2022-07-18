n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if i%2==0:
        c+=a[i]
    else:
        s+=a[i]
if (abs(c-s)==0):
    print("YES")
else:
    print("NO")