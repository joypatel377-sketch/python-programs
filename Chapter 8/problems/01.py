def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c
    
a = int(input("enter a number:\t"))
b = int(input("enter a number:\t"))
c = int(input("enter a number:\t"))

print(great(a,b,c))