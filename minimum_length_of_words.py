a=input()
s=[]
b=a.split()
for i in b:
    s.append(len(i))
print(min(s))