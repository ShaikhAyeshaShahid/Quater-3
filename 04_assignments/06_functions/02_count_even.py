def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print("Even numbers:", count)

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or press enter to stop): ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    return numbers

def main():
    numbers = get_numbers()
    count_even(numbers)

if __name__ == '__main__':
    main()
