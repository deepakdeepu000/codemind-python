a,b=map(int,input().split())
k=[]
for j in range(a):
    x=list(map(int,input().split()))
    k.append(sum(x))
print(max(k))