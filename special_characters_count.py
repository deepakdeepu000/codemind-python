n=input()
a=n.lower()
c=0
k=' abcdefghijklmnopqrstuvwxyz0123456789'
for i in a:
    if i not in k:
        c+=1
print(c)