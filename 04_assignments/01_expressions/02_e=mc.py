C = 299_792_458  # speed of light in meters per second

def main():
    while True:
        user_input = input("Enter mass in kilograms (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            mass = float(user_input)
            energy = mass * C ** 2
            print(f"E = m * c^2")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"Energy = {energy} joules\n")
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == '__main__':
    main()
