# MATH MODULE FOR CALCULATION
# CALCULATE - SQUARE ROOT, NATURAL LOGARITHM(log base e), SINE (in radians)
"""
1. user prompted to enter a number
2. the number is checked for 0 or negative.
3. If zero or negative number is entered, invalid message for square root
   and logarithm is displayed.
4. Else, the square root  and logarithm is calculated and displayed.
5. the sine(radians) is calculated and displayed.


"""
import math
Given_number = float(input("Enter a number: "))
if Given_number <= 0:
    print("Invalid input! Square root and logarithm not defined for negative numbers.")
else:
    square_root = math.sqrt(Given_number)
    print(f"Square root: {square_root}")
    natural_logarithm = math.log(Given_number)  # natural log base e
    print(f"Logarithm: {natural_logarithm}")

sine_rad = math.sin(Given_number)
print(f"Sine: {sine_rad}")
