n=input()
a=n.lower()
k=a.split()
c=0
s=[]
for i in k:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    s.append(c)
print(s.count(min(s)))