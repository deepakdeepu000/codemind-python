n=input()
s=[]
for i in n.split():
    s.append(i)
for i in s:
    print(abs(ord(min(i))-ord(max(i))),end=" ")