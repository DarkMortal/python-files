operations = ['*', '+', '-', '/']

if __name__ == "__main__":
    num1 = ""
    num2 = ""

    while num1 == "":
        try:
            num1 = float(input("Enter first number: "))
        except Exception:
            print("Please enter a valid number")
            num1 = ""
    
    while num2 == "":
        try:
            num2 = float(input("Enter second number: "))
        except Exception:
            print("Please enter a valid number")
            num2 = ""

    inputOperation = ''
    while inputOperation not in operations:
        inputOperation = input("Enter a valid arithmatic operation: ")[0]

    if inputOperation == '*':
        print(f"Answer: {num1 * num2}")
    elif inputOperation == '+':
        print(f"Answer: {num1 + num2}")
    elif inputOperation == '-':
        print(f"Answer: {num1 - num2}")
    elif inputOperation == '/':
        print(f"Answer: {num1 / num2}")