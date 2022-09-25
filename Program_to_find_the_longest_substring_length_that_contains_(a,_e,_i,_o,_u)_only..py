n=input()
a='aeiou'
s=[]
c,c1=0,0
for i in n:
    if i in a:
        c+=1
    if i not in a:
        if c1<c:
            c1=c
        c=0
if c1<c:
    c1=c
print(c1)


    