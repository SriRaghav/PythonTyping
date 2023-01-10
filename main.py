
# Python is a dynamically typed language which means type check happens only at runtime
# This means variable type can change over its lifetime

# In the below snippet, the variable 'a' is assigned to different types of values
# and python wouldn't complain about it

# No Type Hint
print("No Type Hint")

# String
a = "hello"
print(a)

# Integer
a = 1
print(a)

# Float
a = 1.1
print(a)

# Boolean
a = False
print(a)


# Python is a strongly typed language which means you can't perform operations on incompatible types
# For example, you can't add a string and an integer
a = "hello"
b = 1
#print(a + b)


# In Python 3.5, type hints were introduced
# Type hints are a way to annotate your code with the expected type of value the variable would hold
# Type hints are not enforced by the Python interpreter

# With Type Hint
print("With Type Hint")

a: int
b: str
c: float

a = 1
b = "helloworld"
c = 1.1

print(a, b, c)

# the below line would throw an error at runtime because 'a' is an integer and 'b' is a string
# you can't add a string to an integer

print(a + b)

