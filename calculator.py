first_number = input("Enter the first number")
second_number = input("Enter the second number")
operator = input("Enter the operator")

n_first_number = int(first_number)
n_second_number = int(second_number)


if(operator == "+"):
    print(n_first_number+ n_second_number)
elif(operator == "-"):
    print(n_first_number - n_second_number)
elif(operator == "*"):
    print(n_first_number * n_second_number)
elif(operator == "/"):
    print(n_first_number / n_second_number)   
elif(operator == "%"):
    print(n_first_number % n_second_number)
else:
    print("valid number")

    