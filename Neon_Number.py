n=int(input())
a=n*n
c=0
while a!=0:
    b=a%10
    a=a//10
    c=c+b
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")