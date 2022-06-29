a,b=map(int,input().split())
n=list(map(int,input().split()))
n1=list(map(int,input().split()))
b=[]
for i in range(0,a):
    if n[i] in n1 and n[i] not in b:
        b.append(n[i])
print(*b)
        

    
