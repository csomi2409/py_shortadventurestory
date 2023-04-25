import time                         #Module for using sleep to help the users in reading the whole text

def mushroom():                     #Function which handles the full mushroom loops and if statements
    print("You stumbled upon some mushrooms.")
    time.sleep(0.5)
    mushrooms = [" A) You find red mushrooms\n",    #The 2 options put in a list
                 "B) You find brown mushrooms"]
    
    print(mushrooms[0], mushrooms[1])               #Printing these 2 options

    #Ask the user which option would they choose and putting it in a variable. Turns it into lowercase using '.lower()'
    time.sleep(0.5)
    second = str(input("\nWhich type of mushroom do you choose?(color)\n")).lower()

    while second == 'red' or 'brown':               #While loop for checking if the user has put in the correct form of answer
        if second == 'red':                         #IF statement checks if the user has put in the RED option
            red_mushrooms = [" A) You leave it\n",
                            "B) You eat it"]
            print(red_mushrooms[0],red_mushrooms[1])
            time.sleep(1)
            red_second = str(input("What do you do with it?\n")).lower()

            while red_second == 'a' or 'b':         #While loop for checking A or B
                if red_second == 'a':
                    time.sleep(0.5)
                    print("\nYou've got some knowledge. You always leave red mushrooms alone!\n\nYou return to the camp.")
                    break
                elif red_second == 'b':
                    time.sleep(0.5)
                    print("\nYou died, because the mushrooms were poisonous.\n\nThanks for playing!")
                    break
                else:
                    time.sleep(0.3)
                    red_second = str(input("Please enter A or B as an answer!\n")).lower()      #Asks again if not A or B
            return red_second                       #Returns the previously asked input
        
        
        elif second == 'brown':
            brown_mushrooms = [" A) You leave it.",
                            "B) You eat it."]
            print(brown_mushrooms[0], brown_mushrooms[1])
            time.sleep(1)
            brown_second = str(input("What do you do with it? ")).lower()

            while brown_second == 'a' or 'b':
                if brown_second == "a":
                    time.sleep(0.5)
                    print("You return to the fireplace, but you lost 20 HP from feeling hungry.")
                    break
                elif brown_second == "b":
                    time.sleep(0.5)
                    print("You don't feel bad because it was delicious. You return to the camp.")
                    break
                else:
                    time.sleep(0.3)
                    brown_second = str(input("Please input A or B as an answer!\n")).lower()
            return brown_second

        else:
            time.sleep(0.3)
            print("Please input the color of the mushrooms!")
            mushroom()
        return

def cave():
    print("You took all your courage and started the journey!\n\nYou stumbled upon a long-lost plane.\n")
    time.sleep(1)
    plane = [" A) Look for supplies.\n",
             "B) Walk past it."]
    print(plane [0], plane[1])
    time.sleep(0.5)
    second = str(input("What do you do in this situation?\n")).lower()

    if second == 'a':
        time.sleep(0.5)
        print("You've found medicine but no food, you are still starving. You return to the camp.")
    elif second == 'b':
        time.sleep(0.5)
        print("You've got slaughtered by a bear on your journey.\n\nThanks for playing!")
    return

#############   First lines what the user sees  ###################
###################################################################

print("Hello Player.")

print("I welcome you in a multiple choice Adventure game, where you need to survive and get past each obstacle.")

print("\nLet's start the game...\n")

print("You woke up in the middle of an unknown forest.\n")

print("The forest is just waking up, the sun shines and you start to get hungry.\n")

print("You start to plan different kind of routes for yourself...\n")

###################################################################

food = [" A) Go into the forest and search for mushrooms.\n",
        "B) Go to the lake and try fishing with your knife.\n",
        "C) Take the journey to the hill with the risk of starvation.\n\n"]
print(food[0],food[1],food[2])

first = str(input("Where do you go?\nA)Forest\nB)Lake\nC)Journey\n")).lower()

if first == 'a':                            #In the first if statement I use 2 multiple choice questions
    print("\nThe mushrooms..")
    time.sleep(0.4)
    print("Surely they are a great idea.")
    time.sleep(2)
    mushroom()
elif first == 'b':                          #In the second if statement I use .sleep from the time function for longer periods 
    print("\nHmm.. The lake should be a great idea.")
    time.sleep(10)
    print("\nPatience....")
    time.sleep(3)
    print("\nTHERE CATCH IT!!!")
    time.sleep(0.5)
    print("\nIt looks like you got lucky and caught a fish. You return to the camp.")

else:                                       #In the third if statement I use only one multiple choice question
    print("\nYou are a brave person i see...")
    time.sleep(0.5)
    print("\nBe ready...")
    time.sleep(4)
    cave()

