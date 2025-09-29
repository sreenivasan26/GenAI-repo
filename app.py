try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 + num2
    print(f"The sum is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
