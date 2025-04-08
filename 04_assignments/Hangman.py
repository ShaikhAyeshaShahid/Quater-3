import random
import string
from words import words  # Make sure you have this file with a list of words

def get_valid_word(word_list):
    word = random.choice(word_list).upper()
    while '-' in word or ' ' in word:
        word = random.choice(word_list).upper()
    return word

def display_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[lives]

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    print("="*40)
    print("HANGMAN".center(40))
    print("="*40)
    
    while len(word_letters) > 0 and lives > 0:
        print("\n" + display_hangman(lives))
        print(f"Lives remaining: {lives}")
        print("Used letters:", " ".join(sorted(used_letters)))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("\nCurrent word:", " ".join(word_list))

        user_letter = input("\nGuess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print(f"Wrong guess! '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You've already used that letter. Try again!")
        else:
            print("Invalid character. Please enter an English letter.")

    if lives == 0:
        print(display_hangman(0))
        print(f"You died! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")

if __name__ == "__main__":
    hangman()