a = int(input("Enter a number:\n"))

for i in range(2,a):
    if(a%i)==0:
        
        print("The number is !prime")
        break

    else:
        print("The number is prime")
        break
