n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if i%2==0:
        c+=a[i]
for i in range(0,n):
    if i%2!=0:
        s+=a[i]
print(abs(c-s))