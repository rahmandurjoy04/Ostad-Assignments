number1 = int(input("Please Enter first Number: "))
number2 = int(input("Please Enter second Number: "))
operator = input("Please Enter The Operator: ")
if operator == '+':
    print("The Added Value is ",number1+number2)
elif operator == '-':
    print("The Subtracted Value is ",number1-number2)
elif operator == '*':
    print("The Multiplied Value is ",number1*number2)
elif operator == '/':
    print("The Divided Value is ",number1/number2)
else:
    print('Invalid Operator!')