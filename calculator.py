num1 = int(input("Enter a Number: "))
oper = input("Enter an operation: ")
num2 = int(input("Enter another number: "))

if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1/num2)
elif oper == '**':
    print(num1**num2)
else:
    print("ERROR")