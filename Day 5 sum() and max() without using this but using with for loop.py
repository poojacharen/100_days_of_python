# Python has lots of built-in functions to help us work with numbers. 
# One of them helps us calculate the sum (the total). eg: 

# student_scores = [180, 124, 165, 173, 189, 169, 146]
# total_score = sum(student_scores) 

# But how does sum() work behind the scenes? 
# The code is written by the people who developed Python, and it might look something like this:

# student_scores = [180, 124, 165] 
# sum = 0
# for score in student_scores:
#     sum += score   
# print(sum)

# Challenge: using Max() without using Max() :
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

largest_number = 0

for score in student_scores:
    if score > largest_number:
        largest_number = score
print(largest_number)
    
