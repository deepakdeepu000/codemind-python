n=input()
s=[]
k=0
f=0
for i in n.split():
    s.append(i)
for i in s:
    k+=ord(min(i))
    f+=ord(max(i))
print(f-k)
    