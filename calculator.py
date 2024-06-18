num1 = float(input("enter the frist number :"))
operator=input("enter the operator : ")
num2=float(input("enter the second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
else :print("please print a valid operator")