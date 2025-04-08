def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock > 0:
        print(f"This fruit is in stock! Here is how many: {stock}")
    else:
        print("This fruit is not in stock.")

def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    if fruit == 'banana':
        return 5
    if fruit == 'pear':
        return 1000
    return 0

if __name__ == '__main__':
    main()
