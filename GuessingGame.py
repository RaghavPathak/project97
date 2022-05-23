import random
title = "Number Guessing game"
print(title)

pick = "Guess a number (Between 1 and 9)"
print(pick)

while chances < 5 
number = random.randint(1,9)
pick2 = int(input("enter your guess"))

if (pick2 > number):
    print("Guess a number lower than" + pick2)

elif (pick2 < number):
    print("Guess a number higher than" + number)

else:
    print("You Guessed it right!!")
