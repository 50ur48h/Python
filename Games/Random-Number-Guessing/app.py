from random import randint
import logo

def print_logo():
    print(logo.logo)

def generate_random_number():
    return randint(0,100)

def set_difficulty():
    attempt = 10
    level = int(input("Select number for level:\n1. Easy\n2. Hard\nLevel = "))
    if level == 2:
        attempt = 5
    return attempt

def check_answer(Guess, answer):
    if Guess == answer:
        print("Congratulations! You Guess It Corret.")
        return "won"
    else:
        if Guess in range(answer-5, answer):
            print("You are very close. Think high.")
        elif Guess in range(answer, answer+5):
            print("You are very close. Think less.")
        elif Guess in range(answer-10, answer):
            print("You are close. Think high.")
        elif Guess in range(answer, answer+10):
            print("You are close. Think less.")
        elif Guess < answer-10:
            print("You are too low.")
        elif Guess < answer+10:
            print("You are too high.")
        return "loose"
    

def main():
    print_logo()
    answer = generate_random_number()
    attempts = set_difficulty()
    print(f"You have {attempts} attempts to guess the correct number.")
    Guess = int(input(f"Guess a number between 0 and 100 = "))
    attempts -= 1
    while attempts > 0:
        status = check_answer(Guess, answer)
        if status == "won":
            break
        else:
            Guess = int(input(f"You have {attempts} attempts remaining.\nGuess another number = "))
        attempts -= 1


main()