# Defining a new Function
# def <function name>():
#     print("Hello")
#     # Do something else
#     # Do something else ...

# Calling a Function : Calling a function just means triggering the function.
# We can call a function at any point in our code in Python.
# <function name>()
# Putting everything together.
# eg:

# Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello " + name) # Inside the function

# Outside the function
print("Hello")
get_user_name() # Calling the function
