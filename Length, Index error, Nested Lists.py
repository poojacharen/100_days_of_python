states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

# Length of List
#You can get the length of a list (number of items in the list) or
# the length of a string (number characters in the string) by using the len() function.

print(len(states_of_america))

# Index Error
# When you try to access an item that is not in the range of the List,
# you will get an IndexError. e.g.

fruits = ["Apple", "Orange", "Banana"]
print(fruits[3])
# After running the above code, we will get an index error saying : list index out of range
# Because we have asked to print something its not in the list, we only have 0,1,2 in the fruits.

# Nested Lists
# You can put Lists inside other Lists, this becomes something called a "Nested List" or
# a "2D List". e.g.

# dirty_dozen = ["Cherry", "Cucumber", "Kale", "Apple", "Pear", "Spinach"]
# In the above code we have both fruits and vegetables listed in the same variable
# we can split it separately like

fruits = ["Cherry", "Apple", "Pear"]
vegetables = ["Cucumber", "Kale", "Spinach"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# the lists output looks like : [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinach"]] 
# You could also represent the list in 2D format like this:
# ["Cherry", "Apple", "Pear"]
# ["Cucumber", "Kale", "Spinach"]
