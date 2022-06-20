a=int(input())
m=a
s=''
while a!=0:
    c=a%10
    a=a//10
    s+=str(c)
p=''
for i in s:
    if i not in p:
        p+=str(i)
c=0
for i in p:
    c=c*10+int(i)
d=0
while c!=0:
    e=c%10
    c=c//10
    d=d*10+e
if d==m:
    print("Unique Number")
else:
    print("Not Unique Number")