a,b=map(int,input().split())
for i in range(1,b+1):
    c=i*b
    if c%a==0:
        print(c)
        break