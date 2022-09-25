def second(st):
    n=256
    c=[0]*n
    for i in range(len(st)):
        c[ord(st[i])]+=1
    f,s=0,0
    for i in range(n):
        if c[i]>c[f]:
            s=f
            f=i
        elif (c[i] > c[s] and c[i] != c[f] ) :
            s = i
    return chr(s)
n=input()
char=second(n)
if char!=NULL:
    print(char)
else:
    print(-1)