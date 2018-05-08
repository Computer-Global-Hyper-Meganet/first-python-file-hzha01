firstNumber = int(input("Please input a number:"))
secondNumber = int(input("Please input another number:"))

operation = input("What would you like to do?").lower()

if operation == "divide":
    print(firstNumber/secondNumber)
if operation == "multiply":
    print(firstNumber*secondNumber)
if operation == "add":
    print(firstNumber+secondNumber)
if operation == "subtract":
    print(firstNumber-secondNumber)

    
