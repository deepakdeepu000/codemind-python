n=input()
s=''
for i in n:
    if i not in s:
        s+=i
if n==s:
    print("True")
else:
    print("False")