# Figure out how to pick a random name from the list of friends

# 1st method
# List of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

# select a random item
friends_list = random.choice(friends)

print(friends_list)

# 2nd method
friend_name = random.randint(0, 4)

print(friends[friend_name])
