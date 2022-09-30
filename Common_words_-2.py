a=input().lower()
b=input().lower()
s=[]
for i in b.split():
    for j in a.split():
        if i==j:
            s.append(i)
for i in s:
    if s.count(i)>1:
        s.remove(i)
        s.remove(i)
print(len(s))