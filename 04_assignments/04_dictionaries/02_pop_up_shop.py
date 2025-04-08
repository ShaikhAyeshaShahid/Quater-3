def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    
    for fruit_name, price in fruits.items():
        amount = int(input(f"How many {fruit_name}s would you like to buy? Price: ${price}: "))
        total_cost += price * amount
    
    print(f"Your total is: ${total_cost}")

if __name__ == '__main__':
    main()
