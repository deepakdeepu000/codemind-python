n=int(input())
s=0
p=1
while n>0:
    b=n%10
    n=n//10
    s=s+b
    p=p*b
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
    