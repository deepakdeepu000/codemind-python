a=str(input())
c=0
for i in a:
    if i>=chr(48) and i<=chr(57):
        c+=int(i)
print(c)