a = int(input("Enter your Maths marks:\t"))
b = int(input("Enter your ETC marks:\t"))
c = int(input("Enter your PPS marks:\t"))

x = ((a+b+c)/300)*100

if(x>=40 and a>=33 and b>=33 and c >=33):
    print("You are pass",x)
else:
    print("You are Fail",x)

