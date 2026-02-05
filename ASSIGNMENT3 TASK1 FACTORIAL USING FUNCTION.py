#  CALCULATE FACTORIAL USING A FUNCTION

n = int(input("Enter a number: "))
def factorial(number):
    factorial = 1   #starts from 1
    while number > 1:  #starts from 2
        factorial *= number
        number -= 1
    return factorial

print(f"Factorial of {n} is: {factorial(n)}")