n=input().lower()
k=input().lower()
for i in k.split():
    for j in n.split():
        if i==j:
            print(i,end=" ")