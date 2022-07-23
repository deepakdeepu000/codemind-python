a=input()
s=[]
for i in a.split():
    s.append(len(i))
print(max(s))