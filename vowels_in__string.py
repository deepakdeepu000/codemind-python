a=input()
b='aeiouAEIOU'
k=0
s=[]
for i in a:
    if i in b:
        s.append(i)
        k=1
if len(s)==0:
    print(-1)
else:
    f=[]
    for i in s:
        if i not in f:
            f.append(i)
    print(*f)