import math

def main():
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))

    bc = math.sqrt(ab**2 + ac**2)
    print(f"The length of the hypotenuse BC is: {bc}")

if __name__ == '__main__':
    main()
