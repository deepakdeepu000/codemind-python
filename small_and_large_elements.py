n=input()
s=[]
for i in n.split():
    s.append(i)
l=[]
k=[]
for i in s[0]:
    l.append(i)
for i in s[-1]:
    k.append(i)
print(min(l),max(k))