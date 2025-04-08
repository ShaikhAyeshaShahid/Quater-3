def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":  # Break if the user enters a blank line
            break
        
        num = int(user_input)  # Convert user input to an integer
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1  # If number is not in dict, add it with value 1
        else:
            num_dict[num] += 1  # If number is in dict, increment its count
    
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")  # Print counts

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
