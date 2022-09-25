a=input()
k=input()
c,f=0,0
for i in a:
    if i==k:
        c+=1
        f=1
if f==1:
    print(c)
else:
    print(-1)