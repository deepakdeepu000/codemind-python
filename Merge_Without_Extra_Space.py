n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    s=sorted(k+l)
    print(*s)
    