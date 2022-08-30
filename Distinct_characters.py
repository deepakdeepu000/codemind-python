n=input()
s=n.lower()
e=[]
k=''
d="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if s.count(i)==1:
        if i in d:
            e.append(i)
e.sort()
for i in e:
    k+=i
print(k)