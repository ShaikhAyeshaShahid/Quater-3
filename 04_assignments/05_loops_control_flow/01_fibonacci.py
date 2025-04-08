MAX_TERM_VALUE = 10000

def main():
    curr = 0
    next = 1
    while curr < MAX_TERM_VALUE:
        print(curr, end=' ')
        temp = curr + next
        curr = next
        next = temp

if __name__ == '__main__':
    main()
