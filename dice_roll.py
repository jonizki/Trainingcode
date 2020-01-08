from random import randint



def dice_number():
    diceroll = randint(1, 6)
    print(diceroll)


def roll_dice():
    user_input = input("input yes if u want to roll dice or no to stop: ")
    while user_input != "no":
        dice_number()
        user_input = input("input yes to continue rolling and no to stop: ")
        
    
roll_dice()