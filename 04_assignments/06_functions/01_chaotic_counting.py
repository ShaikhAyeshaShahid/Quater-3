import random

DONE_LIKELIHOOD = 0.3  # You can adjust this value for likelihood of stopping

def chaotic_counting():
    count = 1
    while count <= 10:
        if done():
            print(f"Stopped early at number {count}!")
            return
        print(f"Counting: {count}")
        count += 1

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("Let's start counting! I'll stop either when I reach 10 or if I feel like stopping.")
    chaotic_counting()
    print("I am done with the counting!")

if __name__ == "__main__":
    main()
