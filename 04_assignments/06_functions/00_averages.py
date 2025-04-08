def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    average = find_average(number1, number2)
    
    print("The average is:", average)

if __name__ == "__main__":
    main()
