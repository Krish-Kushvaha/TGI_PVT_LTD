print("==== Simple Calculator ====")

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    answer = first + second
    print("Addition =", answer)

elif choice == "2":
    answer = first - second
    print("Subtraction =", answer)

elif choice == "3":
    answer = first * second
    print("Multiplication =", answer)

elif choice == "4":
    if second != 0:
        answer = first / second
        print("Division =", answer)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice")