n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]>a[j]:
            c+=1
    print(c,end=" ")