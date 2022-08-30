n=input()
s=[]
a=n.split()
for i in a:
    s.append(len(i))
print(*s)