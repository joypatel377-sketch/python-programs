# if elif else ladder
a = int(input("Enter your age:\t"))

if(a>=18):
    print("You are above 18")
elif(a<0):
    print("Enter your correct age")
elif(a==0):
    print("Wrong age")
else:
    print("Enter a valid age")