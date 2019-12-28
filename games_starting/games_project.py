import random

money = 100

#Write your game of chance functions here
def flip_of_coin(amount):
    bet = input("Say your bet (head or tails): ")
    if amount <= 0:
        print("you must bet some quantity!")
        return 0
    else:
        num = random.randint(1,2)
        if num == 1:
            result = 'head'
        else:
            result = 'tails'
        if bet == result:
            print("you won {}!!".format(amount))
            return amount
        else:
            print("you lose {}!!".format(amount))
            return -amount

def cho_han(amount):
    guess = input("Type in your guess (even or odd):");
    if amount <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    result = dice1 + dice2
    if result%2 == 0:
        result = 'even'
    else:
        result = 'odd'
    if result == guess:
        print("you guessed right!!")
        return amount
    else:
        print("you guessed wrong!!")
        return -amount
    
def higher_cards(amount):
    if amount <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0
    
    s = input("type in the seed:")
    mine = random.randint(1, 13)
    random.seed(s)
    their = random.randint(1,13)
    
    if mine > their:
        print("You won! Your card is higher.")
        return amount
    elif mine < their:
        print("You lost! Your card is shorter")
        return -amount
    else:
        print("It's a tie!")
        return 0
def roullete(amount):
    if amount <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0
    
    guess = input("type in the your guess (number between 0  and 36):")
    guess_parity = int(guess) % 2
    result = random.randint(1, 37)
    print("the result of the roullete was: " + str(result) + "!!!")
    if guess_parity  == result % 2 :
        if guess != result and guess != 0 and guess != 37:
            print("Congratulations! You guessed the parity!")
            return amount
        elif guess is result and guess != 0 and guess != 37:
            print("Congratulations! You guessed the number!")
            return amount * 35
    else:
        print("You lost!")
        return -amount
        
    
    
        

#Call your game of chance functions here
money += flip_of_coin(10)
print("you have " + str(money) + " left.")
money += cho_han(2)
print("you have " + str(money) + " left.")
money += higher_cards(5)
print("you have " + str(money) + " left.")
money += roullete(10)
print("you have " + str(money) + " left.")


