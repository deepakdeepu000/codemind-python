n,x=map(int,input().split())
s=0
for i in range(n):
    m=list(map(int,input().split()))
    for j in range(len(m)):
        if j==i or j==(n-i-1):
            s=s+m[j]
print(s)