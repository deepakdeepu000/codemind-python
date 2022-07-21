x = int(input())
a = list(map(int,input().split()))
c=0
for i in range(2,x):
    if a[i-1]+a[i-2]==a[i]:
       c=1
    else:
        c=0
        break
if c==0:
    print('no')
else:
    print('yes')