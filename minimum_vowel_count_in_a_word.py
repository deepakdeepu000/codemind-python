a=input()
b=a.split()
d=[]
c=0
for i in b:
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    d.append(c)
    c=0
print(min(d))