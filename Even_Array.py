n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%2==0:
        c+=1
if len(a)==c:
    print("True")
else:
    print("False")