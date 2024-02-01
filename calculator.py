def add(m, n):
    return m + n

def subtract(m, n):
    return m - n

def multiply(m, n):
    return m * n

def divide(m, n):
    return m / n


print("Select an operation You want to carry out.")
print("1.For Doing Addition")
print("2.For Doing Subtraction")
print("3.For Doing Multiplication")
print("4.For Doing Division")

while True:

    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    
        next_calculation = input("Do you want to do next calculation? (yes/no): ")
        if next_calculati1on == "no":
          break
    else:
        print("Invalid Input")
