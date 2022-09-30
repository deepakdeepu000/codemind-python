n=int(input())
s=[0]*(n*n)
a=[]
b=[]
for i in range(2):
    for j in range(n):
        k=list(map(int,input().split()))
        if i==0:
            for m in k:
                a.append(m)
        if i==1:
            for g in k:
                b.append(g)
for k in range(n*n):
    if k%n==(n-1):
        print(abs(b[k]-a[k]))
    else:
        print(abs(b[k]-a[k]),end=' ')