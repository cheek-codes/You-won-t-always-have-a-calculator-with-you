# define the functions add, sub, mult, div
def add(a, b):
    answer = a + b
    print (f"\n{a} + {b} = {answer}\n")

def sub (a, b):
    answer = a - b
    print (f"\n{a} - {b} = {answer}\n")

def mult (a, b):
    answer = a * b
    print (f"\n{a} * {b} = {answer}\n")

def div (a, b):
    answer = a / b
    print (f"\n{a} / {b} = {answer}\n")

# Welcome user
print("Welcome to \"you won't always have a calculator with you\" where you can do some two number math task")


# while loop to continue the program until the user wants to exit
while True:
    # print options to the user
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    # ask user what they want to do
    choice = str(input("Choose your letter: ")).capitalize()
    if choice == "A":
        print ("Addition")
        # ask for values
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        # call the functions
        add(a, b)
    # Rinse and Repeat    
    elif choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mult(a, b)
    elif choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == "E":
        print ("\nThanks for using \"you won't always have a calculator with you\" two number calculator! Good bye \n")
        quit()
    else:
        print ("\nPlease enter valid choice \n")