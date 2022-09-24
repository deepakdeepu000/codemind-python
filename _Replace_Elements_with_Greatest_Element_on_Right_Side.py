n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-1):
    max=0
    for j in range(i+1,n):
        if max<l[j]:
            max=l[j]
    print(max,end=' ')
print(-1)