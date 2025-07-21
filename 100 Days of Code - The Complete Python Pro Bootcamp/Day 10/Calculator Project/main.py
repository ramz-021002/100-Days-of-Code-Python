import art
def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1*n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return float(n1/n2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    to_continue = True
    number1 = int(input("Enter a number:\n"))

    while to_continue:
        for o in operations:
            print(o)
        operation = input("Enter the operation you want from the above operations: ")
        number2 = int(input("Enter a number:\n"))
        result = operations[operation](number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type n to start a new calculation.")
        if choice == 'y':
            number1 = result
        else:
            to_continue = False
            print("\n"*20)
            calculate()

print(art.logo)
calculate()