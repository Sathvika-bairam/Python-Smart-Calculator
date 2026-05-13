# Simple Calculator with History in Python

history = []

while True:
    print("\n----- Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Calculator Closed")
        break

    elif choice == "5":
        print("\n--- Calculation History ---")

        if len(history) == 0:
            print("No history available")
        else:
            for item in history:
                print(item)

    elif choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"

        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"

        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"

        elif choice == "4":

            if num2 == 0:
                operation = "Error! Division by zero"
            else:
                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"

        print("Result:", operation)

        # Save operation in history
        history.append(operation)

    else:
        print("Invalid Choice")
