# EXCEPTION DEMO

"""
Answer the following questions:
1.    When will a ValueError occur?
Ans.  ValueError will occur when a non-number is entered.

2.    When will a ZeroDivisionError occur?
Ans.  ZeroDivisionError will occur if 0 is entered.

3.    Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans.  yes, i can.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator mustn't be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
