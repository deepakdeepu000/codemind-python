def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))
n=int(input())
for i in range(1,n+1):
    s=1
    a=int(input())
    s=fact(a)
    print(s) 