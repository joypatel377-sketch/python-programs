a = int(input("Enter a Number:\t"))
b = int(input("Enter a Number:\t"))
c = int(input("Enter a Number:\t"))
d = int(input("Enter a Number:\t"))

if(a>b and a>c and a>d):
    print("a is the greatest:\t",a)
elif(b>a and b>c and b>d):
    print("b is the greatest:\t",b)
elif(c>b and c>a and c>d):
    print("c is the greatest:\t",c)
elif(d>b and d>c and d>a):
    print("d is the greatest:\t",d)
else:
    print("Sahi Number daal bsdk:\t")
