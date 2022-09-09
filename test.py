# python mini calculator
#+ - * / only

# function for add two numbers
def add(x, y):
    return x + y

# function for subtract two numbers
def subtract(x, y):
    return x - y

# function for multiplies two numbers
def multiply(x, y):
    return x * y

# function for divide two numbers
def divide(x, y):
    return x / y

#select the operation
print("Select the operation type : ")
print("1. + Add")
print("2. - Subtract")
print("3. * Multiply")
print("4. / Divide")

while True:
    #get input from the user
    choice = input("Enter Your Choice : 1 or 2 or 3 or 4 :")

    #validate the choice
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter Number One: "))
        num2 = float(input("Enter Number Two: "))

        if choice == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))

        if choice == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))

        if choice == '3':
            print(num1, " * ", num2, " = ", multiply(num1, num2))

        if choice == '4':
            print(num1, " / ", num2, " = ", divide(num1, num2))

        # check the user wants to continue calculation
        # continue the while loop if answer is yes
        # break the while loop if answer is no
        next_calculation = input("Do you want to continue the calculation (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
