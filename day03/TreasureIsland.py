print("Welcome to Treaure Island.\nYour mission is to find the treausure.")
print("")

first_choice = input("You come across a fork in the road.\nDo you want to go left or right?\nType 'right' or 'left ")
if(first_choice == "left"):
    print("")
    second_choice = input("You come across a river.\nDo you want to swim acorss or wait?\nType 'swim' or 'wait' ")
    if(second_choice == "wait"):
        print("")
        third_choice = input("You come acress a door that has three colored buttons.\nType a button to press.\nred, yellow or blue? ")
        if(third_choice == "red" or third_choice == "blue"):
            print("")
            print("You fell into a pit.\nGame Over")
        elif(third_choice == "yellow"):
            print("")
            print("You found the treasure!\nYou Win!")
        else:
            print("")
            print("You choose not to press any button and leave.\nGame Over")
    else:
        print("You attempt to swim and are attacked by a gator.\nGame Over")
else:
    print("You fell into a hole.\nGame Over")