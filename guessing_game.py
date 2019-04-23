"""
Python Web Development
Project 1 - Number Guessing Game
--------------------------------
"""
import random

min_numb = 0
max_numb = 20
messages = ["Your number is bigger than max",
            "It's lower",
            "It's higher",
            "Your number is smaller than minimun"]


def start_game():
    number_to_guess = random.randint(min_numb, max_numb)
    try:
        user_input = int(
            input("Pick a number between {} and {}\n> ".format(min_numb, max_numb)))
    except ValueError:
        user_input = False

    attemps = [user_input]

    while number_to_guess != user_input:
        attemps.append(user_input)
        display_message(user_input, number_to_guess)
        try:
            user_input = int(input("\nTry another number:\n> "))
        except ValueError:
            user_input = False

    print("\u2714  You got it!\nIt took you: {} tries\n".format(len(attemps)))
    return len(attemps)


def display_message(number, pivot):
    if not number:
        print("\u274C  Your input is not a number, try again")
    elif number > max_numb:
        print(messages[0])
    elif number > pivot:
        print(messages[1])
    elif number >= min_numb:
        print(messages[2])
    else:
        print(messages[3])

def select_highscore(new_score, last_score):
    if new_score < last_score:
        return new_score
    else:
        return last_score
    
if __name__ == '__main__':
    print("""\n--------------------------------------------\n \u2B50   Welcome to the Number Guesing Game! \u2B50\n--------------------------------------------\n""")
    score = start_game()

    while True:
        answer = input("Would you like to play again? [y]es/[n]o: ")
        if answer.lower() == 'n':
            break
        elif answer.lower() != 'y':
            print("Your input is not correct \U0001F4A9 \n")
        else:
            print("\n\n----------------------------\n \U0001F3C5   The HIGHSCORE is {} \U0001F3C5 \n----------------------------\n".format(score))
            score = select_highscore(start_game(), score)

            
