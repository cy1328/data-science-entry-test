def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


#Answer
def swap(x, y):

    if type(x) not in (int, float) or type(y) not in (int, float):
        return -1

    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")

print(swap(x="Apple", y=10))
swap(x=9, y=17)