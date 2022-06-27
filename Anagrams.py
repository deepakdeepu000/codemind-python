n=input()
b=input()
a=n.lower()
c=b.lower()
if sorted(a)==sorted(c):
    print("True")
else:
    print("False")