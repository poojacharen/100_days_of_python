bmi = 84 / 1.65 ** 2

# Number Manipulation
# Flooring a number : we can floor a num by removing all decimal places using the int() func which converts a floating point number(with dec places) into an integer(whole num)
print(bmi) # we get a floating number - output : 30.853994490...
# To floor a number we can use int
print(int(bmi)) # we get an integer - output : 30

# Rounding a number : However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.
print(round(bmi)) # rounds up or down depending on the first dec place - output : 31
# round(3.738492) # Becomes 4
# round(3.14159) # Becomes 3
# round(3.14159, 2) # Becomes 3.14 , here 2 is nothing but 2 decimal places, the output of this will return in a floating number
