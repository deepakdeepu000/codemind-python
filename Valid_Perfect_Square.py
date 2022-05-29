from math import sqrt
n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=int(sqrt(a))
    if b*b == a:
        print("True")
    else:
        print("False")