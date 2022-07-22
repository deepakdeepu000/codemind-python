a,b=map(int,input().split())
n=list(map(int,input().split()))
n1=list(map(int,input().split()))
c=[]
for i in range(0,a):
    if n[i] in n1 and n[i] not in c:
        c.append(n[i])
print(len(c))