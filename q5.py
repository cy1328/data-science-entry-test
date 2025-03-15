def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3


#Answer
def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")

    # Check if divisor is zero
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

    # Check divisibility
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the given scenarios

# Scenario 1
result1 = check_divisibility(num=10, divisor=2)
print("Is 10 divisible by 2?", result1)

# Scenario 2
result2 = check_divisibility(num=7, divisor=3)
print("Is 7 divisible by 3?", result2)