# What if we want to convert a piece of data into a diff datatype
# Type Conversion/Type Casting : We can convert data into different datatypes using special functions
print(int("123"))
print(int(123) + int(456))
print(bool(True))

# Task
# print("Number of letters in your name: " + len(input("Enter your name")))
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name")) # str
print(type(length_of_name)) # int
print("Number of letters in your name: " + str(length_of_name) )
