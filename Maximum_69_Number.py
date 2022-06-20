a=int(input())
c=0
d=0
m=0
while a!=0:
    b=a%10
    a=a//10
    m=m*10+b
while m!=0:
    e=m%10
    m=m//10
    if d==0:
        if e==6:
            e=9
            d+=1
    c=c*10+e
print(c)