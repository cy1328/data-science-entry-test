def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


#Answer
def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input 'lst' must be a list.")

    modified_list = []
    for item in lst:
        if item == find_val:
            modified_list.append(replace_val)
        else:
            modified_list.append(item)
    return modified_list


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

list1 = [1, 2, 3, 4, 2, 2]
find_value1 = 2
replace_value1 = 5

result1 = find_and_replace(list1, find_value1, replace_value1)
print(f"Original list: {list1}, Find: {find_value1}, Replace: {replace_value1}, Result: {result1}")

list2 = ["apple", "banana", "apple"]
find_value2 = "apple"
replace_value2 = "orange"

result2 = find_and_replace(list2, find_value2, replace_value2)
print(f"Original list: {list2}, Find: {find_value2}, Replace: {replace_value2}, Result: {result2}")