a=str(input())
l=len(a)
s=''
c=0
for i in a[::-1]:
    c+=1
    if i!=' ':
        s+=str(i)
    if i==' ' or c==l:
        print(s[::-1],end=' ')
        s=''