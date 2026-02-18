def pattern(n):
    if n==0:

        ch = int(input("press for how much u want to do again 0 to stop"))
        if ch==0:
            return
        else:
            pattern(ch)
    

    print("*"*n)
    pattern(n-1)

pattern(4)
