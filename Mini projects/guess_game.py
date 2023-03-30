import random

num_high=input("enter highest value")
if num_high.isdigit() :
    num_high=int(num_high)
else:
    print("enter a number")
    quit()

number=random.randint(0,num_high)
guess=0

while True:
    guess+=1
    num_guess=input("make a guess ")

    if num_guess.isdigit() :
        num_guess=int(num_guess)
    else:
        print("enter a number")
        continue

    if num_guess==number :
        print("correct")
        break

    elif num_guess<number :
        print("your guess were below the number")
    else:
        print("your guess were above the number")

print("you have got it in", guess, "guessess")
