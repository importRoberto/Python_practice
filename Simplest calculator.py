def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return complex(0, (-x) ** 0.5)
    else:
        return x ** 0.5

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"Square root of {num} = {sqrt(num)}")

        elif choice == '7':
            num = int(input("Enter number: "))
            print(f"Factorial of {num} = {factorial(num)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()