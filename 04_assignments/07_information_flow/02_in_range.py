def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False
def main():
    num = input("Enter the number: ")
    low = input("Enter the low number: ")
    high = input("Enter the high number: ")
    print(in_range(num, low, high))

if __name__ == '__main__':
    main()