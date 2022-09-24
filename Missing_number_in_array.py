def missing(a):
    n=len(a)
    k=(n+1)*(n+2)/2
    s=sum(a)
    return k-s
n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    print(int(missing(b)))
    