a=input()
l=a
b=''
for i in a:
    b+=i
v='aeiou'
for i in v:
    if i not in b:
        print(False)
        break
else:
    print(True)