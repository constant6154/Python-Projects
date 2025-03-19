
import math
import random
import time
upper = int(input("Enter upper bound:"))
lower = int(input("Enter lower bound:"))
count = 0
flag = False
random.seed(time.time())
x = random.randint(lower,upper)
chances = math.ceil(math.log2(upper-lower+1))
print(f"\n\tYou've only {chances} chances to guess the integer!\n")
while count < chances:
    count += 1
    guess = int(input("Guess a number: "))
    if guess == x:
        print(f'Congo you guessed the right number {guess} in {count} attempts!')
        flag = True
        break
    elif guess < x :
        print("Too small")
    else :
        print("Too large")

if not flag:
    print(f"The number was {x}")
    print("Better luck next time!")