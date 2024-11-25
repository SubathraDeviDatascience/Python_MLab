try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input, please enter a number")