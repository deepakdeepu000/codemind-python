n=int(input())
a=n
s=0
if n<0:
    n=n*(-1)
while n!=0:
    b=n%10
    n=n//10
    s=s*10+b
if a>0:
    print(s)
else:
    print(s*(-1))