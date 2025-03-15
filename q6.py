def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


#Answer
def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

list1 = [3, 5, -1, 7, -2, 8]
result1 = find_first_negative(list1)
print(f"List: {list1}, First negative: {result1}")

list2 = [2, 10, 7, 0]
result2 = find_first_negative(list2)
print(f"List: {list2}, First negative: {result2}")