#  CALCULATE FACTORIAL USING A RECURSION FUNCTION
"""
The assignment includes a user defined function to calculate the factorial of positive numbers.
The function is defined as factorial_rec with the argument 'number'
1. The first prompt is to enter an integer.
2. The first If block states
    i) to return 1 as the factorial of 1 or 0 because 0! = 1 and 1! = 1
    ii) to return None as the factorial of number < 0 iss invalid because factorial is not defined for
        negative numbers, and
    iii) to finally calculate the factorial using the recursion function if the entry is a positive number.
3. The second If block states
   i) To print an invalid message if the result is returned as None (for -ve numbers).
   ii) else, to print the string with the number and its factorial.

"""

n = int(input("Enter a number: "))  
def factorial_rec(number):
    if number == 0 or number == 1:  # because 1! = 1
        return 1
    elif number < 0:
        return None
    else:
        factorial_for = number * factorial_rec(number-1)
        return factorial_for

result = factorial_rec(n)
if result is None:
    print("Invalid entry! Only positive numbers allowed")
else:
    print(f"Factorial of {n} is: {result}")
