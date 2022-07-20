def findmajority(a, n):
    mc = 0
    i = -1
    for i in range(n):
        c = 0
        for j in range(n):
            if(a[i] == a[j]):
                c += 1
        if(c > mc):
            mc = c
            b = i
    if (mc > n//2):
        print(a[b])
n=int(input())
a=list(map(int,input().split()))
findmajority(a,n)
    