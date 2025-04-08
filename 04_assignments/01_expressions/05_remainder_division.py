def main():
    dividend = int(input("Enter the number to be divided: "))
    divisor = int(input("Enter the number to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"The result of {dividend} divided by {divisor} is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
