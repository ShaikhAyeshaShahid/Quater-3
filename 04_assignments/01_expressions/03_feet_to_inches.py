INCHES_PER_FOOT = 12

def main():
    feet = float(input("How many feet would you like to convert to inches? "))
    inches = feet * INCHES_PER_FOOT
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == '__main__':
    main()
