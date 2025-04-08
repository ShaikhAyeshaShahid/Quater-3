import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: {die1} and {die2} → Total: {total}")

def main():
    die1 = 100  # Local to main
    print(f"die1 in main() starts as: {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() ends as: {die1}")

if __name__ == '__main__':
    main()
