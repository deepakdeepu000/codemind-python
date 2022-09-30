a,b=map(int,input().split())
k=[0]*b
for j in range(a):
    x=list(map(int,input().split()))
    for i in range(len(x)):
        k[i]=k[i]+x[i]
for i in k:
    print(i,end=' ')