def get_user_info():
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    email = input("Please enter your email: ")
    
    return first, last, email

def main():
    user_details = get_user_info()
    print("Here is the information you provided:", user_details)

if __name__ == "__main__":
    main()
