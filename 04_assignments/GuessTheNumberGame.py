import random

def play_game():
    secret = random.randint(0, 99)
    print("I'm thinking of a number between 0 and 99.")

    guess = int(input("Enter your guess: "))

    while guess != secret:
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")
        guess = int(input("Try again: "))

    print("Congratulations! You guessed it:", secret)

if __name__ == '__main__':
    play_game()
