n,x=map(int,input().split())
k=[]
for j in range(n):
    m=list(map(int,input().split()))
    k.append(sum(m))
print(sum(k))