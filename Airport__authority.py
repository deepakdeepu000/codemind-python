def prize(a,n,t):
    c=0
    for i in a:
        c+=1
        if (i>t):
            c+=1
    return c
n=int(input())
w=[]
for i in range(n):
    n=int(input())
    w.append(n)
t=int(input())
print(prize(w,n,t))