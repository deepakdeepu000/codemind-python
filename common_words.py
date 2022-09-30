n=input()
k=input()
n=n.lower()
k=k.lower()
a=n.split()
b=k.split()
s=[]
if len(a)>len(b):
    for i in a:
        if i in b and i  not in s:
            s.append(i)
else:
    for i in b:
        if i in a and i not in s:
            s.append(i)
print(*s)
