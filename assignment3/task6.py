def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: You can't divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")

try:
    num = float(input("Enter numerator: "))
    denom = float(input("Enter denominator: "))
    print("Result:", divide_numbers(num, denom))
except ValueError:
    print("Please enter valid numeric values.")