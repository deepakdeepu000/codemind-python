x=input()
c,s,k=0,0,0
while c < len(x):
    if x[c]=='z':
        s+=1
    elif x[c]=='o':
        k+=1
    c+=1
if (2*s==k):
    print("Yes")
else:
    print("No")
        