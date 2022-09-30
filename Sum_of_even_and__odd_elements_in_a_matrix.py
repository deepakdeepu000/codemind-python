n,x=map(int,input().split())
s=0
k=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        if m[i]%2==0:
            s+=m[i]
        else:
            k+=m[i]
print(s,k)