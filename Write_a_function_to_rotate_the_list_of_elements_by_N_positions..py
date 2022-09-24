n=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in range(0, a):  
    list1 = l[n-1];  
    for j in range(n-1,-1,-1):  
        l[j] = l[j-1];
    l[0] = list1;
for i in range(0,n):  
    print(l[i],end=" ")