n=int(input())
for i in range(n):
    n=int(input())
    k=input()
    f=0
    for j in range(len(k)):
        if k.count(k[j])==1:
            print(k[j])
            f=1
            break
    if f==0:
        print(-1)