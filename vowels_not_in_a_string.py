n=input()
c=0
s=''
for i in n:
    if i in 'aeiouAEIOU':
        s+=i
l='aeiou'
for i in l:
    if i not in s:
        c+=1
        print(i,end=' ')
if c==0:
    print(c)