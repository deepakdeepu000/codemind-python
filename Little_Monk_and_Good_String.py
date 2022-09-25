n=input()
k,c=0,0
for i in n:
    if i in 'aeiou':
        k+=1
    else:
        if c<k:
            c=k
        k=0
if c<k:
    c=k
print(c)