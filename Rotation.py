a  = int(input())
for _ in range(a):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    s = k%n
    print(*(l[n-s:]+l[:n-s]))