x = int(input())
a = list(map(int,input().split()))
s=0
for i in range(1,x-1,2):
    if (a[i-1]<a[i] and a[i]>a[i-1]):
        s+=1
    else:
        print('-1')
        s=0
        break
if s!=0:
    print(s)