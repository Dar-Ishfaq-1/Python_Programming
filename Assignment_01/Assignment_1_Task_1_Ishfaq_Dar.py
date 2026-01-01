Num1 = input("Enter First Number : ")
Num2 = input("Enter Second Number : ")

operator = input("Enter 1 for +,  2 for -, 3 for * or  4 for /  : ")
if operator in  ['1', '2', '3', '4']:
    if operator == '1':
        print("The Addition is : ", int(Num1) + int(Num2))
    elif operator == '2': 
        print("The Subtraction is : ", int(Num1) - int(Num2))
    elif operator == '3': 
        print("The Multiplication is : ", int(Num1) * int(Num2))
    elif operator == '4': 
        print("The Division is : ", int(Num1) / int(Num2))   
else: 
    print("Invalid Operator")