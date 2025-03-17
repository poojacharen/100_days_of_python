# Tip Calculator Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_tip = tip / 100
total_tip = bill * percentage_tip
total_bill = bill + total_tip
per_person_bill = total_bill / people
final_price = round(per_person_bill, 2)
print(f"Each person should pay: ${final_price}")
