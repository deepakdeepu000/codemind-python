n,k=map(int,input().split())
a=list(map(int,input().split()))
c=s=0
for i in range(n):
    for j in range(i,n):
        c+=a[j]
        if c==k:
            s+=1
        if c>k:
            break
    c=0
print(s)
