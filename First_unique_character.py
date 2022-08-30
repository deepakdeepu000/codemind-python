n=input()
s=n.lower()
e=[]
k=''
d="abcdefghijklmnopqrstuvwxyz"
f=0
for i in s:
    if s.count(i)==1:
        if i in d:
            e.append(i)
            f=1
            break
if f==1:
    print(*e)
else:
    print(-1)