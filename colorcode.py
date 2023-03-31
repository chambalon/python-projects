import random


COLORS_AVAILABLE=["R","G","B","Y","O","V"]
CODE_LENGTH=4
ATTEMPTS=10

def generate_color_code():
    computer_code=[]

    for _ in range(CODE_LENGTH):
        colors=random.choice(COLORS_AVAILABLE)
        computer_code.append(colors)
    return computer_code


def guess_color_code():
    while True:
        user_code=input("guess 4 color code(separated by space): ").upper().split(" ")

        if len(user_code)!=CODE_LENGTH:
            print(f"Invalid! enter{CODE_LENGTH} colors")
            continue

        for color in user_code:
            if color not in COLORS_AVAILABLE:
                print(F'invalid color:{color}.Try again')
                continue
        else:
            break
    return user_code


def compare(user_code,computer_code):
    computer_code_count_dict={}
    correct_pos=0
    incorrect_pos=0

    for color in computer_code:
        if color not in computer_code_count_dict:
            computer_code_count_dict[color]=0
        computer_code_count_dict[color]+=1

    for user_color, computer_color in zip(user_code,computer_code):
        if user_color==computer_color:
            correct_pos+=1
            computer_code_count_dict[user_color]-=1

    for user_color, computer_color in zip(user_code,computer_code):
        if user_color in computer_code_count_dict and computer_code_count_dict[user_color] > 0:
            incorrect_pos+=1
            computer_code_count_dict[user_color]-=1

    '''for color in user_code:
        if color in computer_code_count_dict and computer_code_count_dict[color]>0:'''

    return correct_pos,incorrect_pos


def game():
    print(f"Welcome! you get {ATTEMPTS} tries to guess the color code")
    print(f'available colors are:{COLORS_AVAILABLE}')

    computer_code=generate_color_code()

    for tries in range(1,ATTEMPTS+1):
        user_code=guess_color_code()
        correct_pos, incorrect_pos=compare(user_code,computer_code)

        #if user_code==computer_code:
        if correct_pos==CODE_LENGTH:
            print(f'you guessed it in attempt {tries} ')
            break

        print(f'correct positions={correct_pos} , incorrect positions={incorrect_pos}')

        print(10-int(tries), "attempts left")

    else:
        print("you ran out of tries, correct code was ", *computer_code)

if __name__ == "__main__":
    game()