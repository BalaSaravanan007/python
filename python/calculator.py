

##Calculator Programme
def my_func(num1, operator, num2):
    if operator == "+":
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "*":
        return(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            return(num1 / num2)
        else:
            return("Error")
    else:
        return("Invalid Operator")

print(my_func(64467584,  "/", 956745))
