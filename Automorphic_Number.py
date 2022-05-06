n=int(input())
a=n
d=n*n
c=0
f=0
g=0
i=0
while n!=0:
    b=n%10
    n=n//10
    c+=1
while d!=0:
    e=d%10
    d=d//10
    f+=1
    g=g*10+e
    if f==c:
        break
while g!=0:
    h=g%10
    g=g//10
    i=i*10+h
if i==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

