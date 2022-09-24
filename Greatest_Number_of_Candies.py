n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=max(l)
s=[]
for i in range(len(l)):
    if l[i]+k>=m:
        s.append(True)
    elif l[i]+k<m:
        s.append(False)
print(*s)