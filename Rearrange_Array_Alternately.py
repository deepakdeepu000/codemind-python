def rearrange(a, n):
    temp = n*[None]
    s, l = 0, n-1
    flag = 1
    for i in range(n):
        if flag == 1:
            temp[i] = a[l]
            l -= 1
        else:
            temp[i] = a[s]
            s += 1
        flag = 1-flag
    for i in range(n):
        a[i] = temp[i]
    print(*a)
n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    rearrange(b,a)