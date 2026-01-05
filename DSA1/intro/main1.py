def find_minimum(nums):
    # If the list is empty, return None
    if not nums:
        return None

    # Set minimum to positive infinity
    minimum = float("inf")

    # Iterate through the list
    for num in nums:
        if num < minimum:
            minimum = num

    # Return the smallest value found
    return minimum


"""
In the context of computer science, 
an algorithm is a finite sequence of well-defined, 
computer-implementable instructions. In short, an algorithm is:
- Defined: there is a specific sequence of steps that performs a task
- Unambiguous: there is a "correct" and "incorrect" interpretation of the steps
- Implementable: it can be executed using software and hardware
"""
