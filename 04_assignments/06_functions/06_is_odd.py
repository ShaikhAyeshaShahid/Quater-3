def main():
    for i in range(10, 20):
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int):
    return value % 2 != 0

if __name__ == '__main__':
    main()
