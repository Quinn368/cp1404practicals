"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: It will occur when the value inputted is a non-numeric number
2. When will a ZeroDivisionError occur?
Ans: It will occur when the user inputted a zero value as a denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Enter a non-zero value.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
