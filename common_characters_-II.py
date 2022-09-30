
a=input().lower()
b=input().lower()
s=[]
for i in a:
    if i==' ':
        continue
    if i in b and i not in s:
        s.append(i)
for i in b:
    if i==' ':
        continue
    if i in a and i not in s:
        s.append(i)
print(len(s))
        