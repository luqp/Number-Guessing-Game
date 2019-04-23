# Number Guessing Game

import random
min_number = 0
max_number = 20
messages = ["You got it! \U0001F3C6",
            "Your number is larger than max",
            "Your number's higher",
            "Your number's lower",
            "Your number is smaller than minimun"]


def start_game():
    number_to_guess = random.randint(min_number, max_number)
    user_input = None
    attemps = []

    while number_to_guess != user_input:
        if len(attemps):
            messages = "\nTry another number:\n> "
        else:
            messages = "Pick a number between {} and {}\n> "
        user_input = get_user_guest(messages, number_to_guess)
        attemps.append(user_input)

    print("It took you: {} tries\n".format(len(attemps)))
    return len(attemps)


def get_user_guest(message, number_to_guess):
    try:
        user_number = int(input(message.format(min_number, max_number)))
    except ValueError:
        print("Your input is not a number \u274C")
        user_number = None
    else:
        if user_number == number_to_guess:
            print(messages[0])
        elif user_number > max_number:
            print(messages[1])
        elif user_number > number_to_guess:
            print(messages[2])
        elif user_number >= min_number:
            print(messages[3])
        else:
            print(messages[4])

    return user_number


def select_highscore(new_score, last_score):
    if new_score < last_score:
        return new_score
    else:
        return last_score


if __name__ == '__main__':
    print("\n", "-" * 43, "\n"
          " \u2B50   Welcome to the Number Guesing Game! \u2B50"
          "\n", "-" * 43, "\n")

    score = start_game()

    while True:
        answer = input("Would you like to play again? [y]es/[n]o: ")

        if answer.lower() == 'n':
            break
        elif answer.lower() != 'y':
            print("Your input is not correct \u274C\n")
        else:
            print("\n", "-" * 26, "\n"
                  " \U0001F3C5   The HIGHSCORE is {} \U0001F3C5".format(score),
                  "\n", "-" * 26, "\n")
            score = select_highscore(start_game(), score)