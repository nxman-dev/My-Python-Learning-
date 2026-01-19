# Simple Calculator Program
# Supports +, -, *, /
# Handles division by zero


num1 = int(input("Enter 1st number: ")) 
op = input("Enter operator: ")
num2 = int(input("Enter 2nd number: ")) 


#Sum
if(op == '+'):
    print(num1 + num2)

#Difference
elif(op == '-'):
    print(num1 - num2)

#Division
elif(op == '/'):
    if(num2 == 0):
        print("Cant divide by zero")
    else :
        print(num1 / num2)

#multiplication
elif(op == '*'):
    print(num1 * num2)

else :
    print ("Invalid operator")