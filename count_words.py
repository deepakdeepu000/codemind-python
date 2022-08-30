n=input()
k=n.lower()
s=[]
c=0
a='aeiou'
b='bcdfghjklmnpqrstvwxyz'
for i in k.split():
    s.append(i)
for i in s:
    if i[0] in a and i[-1] in b:
        c+=1
print(c)

    
    