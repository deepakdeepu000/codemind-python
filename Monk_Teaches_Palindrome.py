x=int(input())
for i in range(x):
    n=input()
    k=n
    c=0
    s=''
    for i in k[::-1]:
        c+=1
        s+=i
    if s==n:
        print("YES",end=" ")
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")
    
    