import random
'''
0 for gun
1 for snake
2 for water

'''

comp = random.choice([0,1,2])

youstr = input("Enter your choice from : \n")
youdict = {"s": 1,
           "w":2,
           "g":0}
revdict = {1:"Snake",
           2:"Water",
           0:"Gun"}
you= youdict[youstr]

print(f"you chose {revdict[you]}\nComputer chose {revdict[comp]}")

if(comp==you):
    print("Its a Draw")

else:
    if(comp==0 and you==1):
        print("You Lose")
    elif(comp==0 and you==2):
        print("You Win")
    elif(comp==1 and you==0):
        print("You Win")
    elif(comp==1 and you==2):
        print("You lose")
    elif(comp==2 and you==1):
        print("You Win")
    elif(comp==2 and you==0):
        print("You lose")
    