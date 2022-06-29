def rev(a):
    c=0
    while a:
        b=a%10
        a=a//10
        c+=1
    return c
a=int(input())
b=list(map(int,input().split()))
c=[]
count=0
for i in b:
    d=rev(i)
    c.append(d)
m=min(c)
for i in b:
    if rev(i)==m:
        count+=1
print(count)