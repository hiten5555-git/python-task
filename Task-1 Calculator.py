import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def exponentiate(x, y):
    return x ** y

def main():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Quit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(x, y))
            elif choice == '2':
                print("Result:", subtract(x, y))
            elif choice == '3':
                print("Result:", multiply(x, y))
            elif choice == '4':
                print("Result:", divide(x, y))
            elif choice == '5':
                print("Result:", exponentiate(x, y))
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid input")
            print()

main()
