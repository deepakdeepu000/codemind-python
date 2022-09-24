def missing(l,n):
    for i in range(1,n+1):
        flag=1
        for j in range(0,n):
            if l[j]== i:
                flag=0
                break
        if flag==1:
            return i
n=int(input())
l=list(map(int,input().split()))
k=missing(l,n)
print(k)