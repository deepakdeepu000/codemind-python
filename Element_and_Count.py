n=int(input())
a=list(map(int,input().split()))
c=0
s=''
for i in a:
    if str(i) not in s:
        for j in a:
            if i==j:
                s+=str(i)
                c+=1
        print(i,c,end=' ')
    c=0
   