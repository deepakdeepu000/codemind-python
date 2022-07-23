a=input()
b=input()
for i in range(0,len(a)):
    if a[i]==b:
        print(True)
        print(i)
        break
else:
    print(False)