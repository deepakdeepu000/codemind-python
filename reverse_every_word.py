a=input()
s=[]
b=a.split()
for i in b:
    s.append(i[::-1])
print(*s)