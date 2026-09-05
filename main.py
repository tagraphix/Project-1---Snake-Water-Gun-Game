# Snake, Water and Gun Game
'''
1 for snake
-1 for water
0 for gun
'''

import random #random module

print("Snake, Water, Gun")
input("Are you Ready? Press Enter to continue...")

computer = random.choice([-1, 0, 1]) #random.choice for choosing randomly
youstr = input("Enter your choice: ")
youDict =  {"s":1, "w":-1, "g":0}
reversedDict = {1:"Snake", -1: "Water", 0:"Gun"}

#add the input of user (i.e. youstr) in dictionary (i.e.youDict) and assign the value to you
you = youDict[youstr]

#By now we have 2 numbers (variables), you and computer

print(f"You chose {reversedDict[you]} \nComputer chose {reversedDict[computer]}")

if(computer == you):
    print("It's a draw!")

else: 
    if(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong!")