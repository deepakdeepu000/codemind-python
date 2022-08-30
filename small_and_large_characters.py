n=input()
s=[]
for i in n.split():
    s.append(i)
for i in s:
    print(min(i),max(i),end=" ")