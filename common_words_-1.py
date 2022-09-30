a=input().lower()
b=input().lower()
s=[]
for i in a.split():
    for j in b.split():
        if i==j:
            s.append(i)
print(len(s))