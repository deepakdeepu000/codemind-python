n=input()
k=n.split()
c=0
s=[]
for i in k:
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    s.append(c)
    c=0
print(max(s))