def add_many_numbers(numbers) -> int:
    return sum(numbers)

def main():
    numbers = [1, 2, 3, 4, 5]  
    sum_of_numbers = add_many_numbers(numbers)  
    print(sum_of_numbers)  

if __name__ == '__main__':
    main()
