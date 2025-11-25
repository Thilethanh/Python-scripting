
# def function_name (parameters):
#    statement(s)

def welcome(name):
    print("Hello " + name + ", Welcome to the jungle! ")

welcome("Jone")

# The return statement is used to exit a function.
# return [expression_list]

def return_value(a):
    if a >= 0:
        return a
    else:
        return -a


print(return_value(2))
print(return_value(-4))

# lambda functions is anoymous one-line function
# Used for short operations where defining a full  def function would be overkill
# lambda arguments: expression

# No name
# One expression only
# Returns the expression automatically

add = lambda x,y: x + y
print(add(3,5))

#   Equivalent
def Add(x,y):
    return x + y


# Sorting with a custom key
pairs = [(1, 3), (2, 1), (5, 2)]

pairs_sorted = sorted(pairs, key=lambda x: x[1])
print(pairs_sorted)   # [(2, 1), (5, 2), (1, 3)]

# Filtering data
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4, 6]

# Mapping data
nums = [1, 2, 3]
squared = list(map(lambda x: x*x, nums))
print(squared)  # [1, 4, 9]


# MODULES
# A file that contains Python code.
# Break larger program into small and organized one
# Define functions in the module and import them whenever needed.

"""
sample.py is the file name
def addition(num1, num2):
    result = num1 + num2
    return result


add.py is the name of a new file
import sample
sum = sample.addition (10, 20)
print (sum)
"""

