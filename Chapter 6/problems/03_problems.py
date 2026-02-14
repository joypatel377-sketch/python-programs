a = "Make a lot of money"
b = "buy now" 
c = "subscribe this"
d = "click this"

hi = input("Enter a message that you want to give:\t")

if(a in hi) or (b in hi) or (c in hi) or (d in hi):
    print("This message is a scam")
else:
    print("This message is not a scam")