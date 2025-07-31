# Simple Calculator

# Ask for the first number
num_1=int(input("Enter the first number:"))
# Ask for the second number
num_2=int(input("Enter the second number:"))
# Ask for the operation
operation=input("Enter operation (+,-,*,/):")
# Perform the calaulation baseed on chosen operation
if operation == "+":
    result=num_1+num_2
    print(f"Result:{num_1}+{num_2}={result}")
elif operation=="-":
    result=num_1-num_2
    print(f"Result:{num_1}-{num_2}={result}")
elif operation=="*":
    result=num_1*num_2
    print(f"Result: {num_1}*{num_2}={result}")
elif operation=="/":
    if num_2!=0:
        result=num_1/num_2
        print(f"Result:{num_1}/{num_2}={result}")
    else: print("ERROR:DIVISION BY ZERO IS NOT ALLOWED")
else:print("INVALID OPERATION!! PLEASE CHOOSE +,-,*,/")