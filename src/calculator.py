def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,
}

def user_interface():
    num1 = int(input("Enter a number: "))
    operator = input("Enter the operator ( + , - , * , / ): ")
    num2 = int(input("Enter the second number: "))

    print(f"The result of {num1} {operator} {num2} is {operations[operator](num1, num2)}")


if __name__ == "__main__":
    user_interface()