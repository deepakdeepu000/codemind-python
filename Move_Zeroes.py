n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i!=0:
        k.append(i)
for i in a:
    if i==0:
        k.append(i)
print(*k)
