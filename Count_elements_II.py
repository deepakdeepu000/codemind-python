n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
for i in list(set(a)):
    if b.count(i)==0:
        s.append(i)
for j in list(set(b)):
    if a.count(j)==0:
        s.append(i)
print(len(s))