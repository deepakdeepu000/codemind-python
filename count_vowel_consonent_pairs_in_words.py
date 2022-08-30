n=input()
k=n.lower()
g=k.split()
m=0
a="aeiou"
for i in g:
    l=len(i)
    s=1
    n=0
    for j in range(l):
        if i[j] in a and i[0-s] not in a or i[j] not in a and i[0-s] in a:
            n+=1
        s+=1
    m+=n
print(m//2)
