n=int(input())
a=list(map(int,input().split()))
c=0
l=0
for i in range(0,n):
    for j in range(i,n):
        if a[i]==a[j]:
            c+=1
    if c==1:
        s+=a[i]
    c=0
print(s)