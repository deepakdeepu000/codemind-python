n=int(input())
a=list(map(int,input().split()))
b=set(a)
for i in b:
    a={0,1}
    if i not in a:
        print("False")
        break
else:
    print("True")