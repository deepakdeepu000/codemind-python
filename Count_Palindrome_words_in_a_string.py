import string
n=input()
s=n.split()
c=0
for i in s:
    b=i[::-1]
    if i.lower()==b.lower():
        c+=1
print(c)
