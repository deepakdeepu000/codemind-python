n=int(input())
a=0
while n!=0:
    b=n%10
    n=n//10
    if b>a:
        a=b
print(a)