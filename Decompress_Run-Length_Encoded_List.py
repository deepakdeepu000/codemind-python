n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if i==0:
        k=[l[i+1]]*(l[i])
    elif i % 2 == 0 and i != l[:-1]:
        k.extend([l[i+1]]*(l[i]))
print(*k)