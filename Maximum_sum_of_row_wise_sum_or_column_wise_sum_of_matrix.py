a,b=map(int,input().split())
k=[0]*(b)
s=[]
for j in range(a):
    x=list(map(int,input().split()))
    s.append(sum(x))
    for i in range(b):
        k[i]=k[i]+x[i]
print(max(s+k))