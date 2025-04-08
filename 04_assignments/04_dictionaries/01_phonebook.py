def read_phone_numbers():
    phonebook = {}  # Create an empty phonebook dictionary

    while True:
        name = input("Enter a name (or press Enter to stop): ")  # Ask for name
        if name == "":  # Stop if the user presses Enter without a name
            break
        number = input("Enter the number for " + name + ": ")  # Ask for phone number
        phonebook[name] = number  # Store name and number in the phonebook

    return phonebook

def print_phonebook(phonebook):
    # Prints each name and number in the phonebook
    for name, number in phonebook.items():
        print(name + " -> " + number)

def lookup_numbers(phonebook):
    while True:
        name = input("Enter a name to lookup (or press Enter to stop): ")  # Ask for name to lookup
        if name == "":  # Stop if the user presses Enter without a name
            break
        if name in phonebook:  # If the name exists in the phonebook, show the number
            print(name + "'s number is: " + phonebook[name])
        else:  # If the name doesn't exist
            print(name + " is not in the phonebook.")

def main():
    phonebook = read_phone_numbers()  # Read the phonebook data
    print("\nHere is your phonebook:")
    print_phonebook(phonebook)  # Print the phonebook
    lookup_numbers(phonebook)  # Let the user lookup numbers

if __name__ == '__main__':
    main()
