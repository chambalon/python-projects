import random

user_score=0
computer_score=0

options_list= ["rock", "paper", "scissors"]

while True :
    user_selection= input("enter rock/paper/scissors or q for quit: ").lower()
    if user_selection=="q" :
        break
    if user_selection not in options_list :
        continue

    random_num=random.randint(0,2)
    # rock-1, paper-2, scissors-3 

    computer_selection=options_list[random_num]

    print("computer picked" + computer_selection)

    if user_selection=="rock" and computer_selection=="scissors" :
        print("you won")
        user_score+=1
    elif user_selection=="paper" and computer_selection=="rock" :
        print("you won")
        user_score+=1
    elif user_selection=="scissors" and computer_selection=="paper" :
        print("you won")
        user_score+=1
    else:
        print("you lost")
        computer_score+=1

print("you won", user_score, "times")
print("computer won", computer_score, "times")