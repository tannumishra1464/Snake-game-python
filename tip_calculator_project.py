print("Welcome to the tip calculator!")
bill=int(input("What was the total bill? $"))
tip_percent=int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_persons=int(input("How many people to split the bill?"))
tip=(bill * 0.1)
bill_with_tip = bill + (bill * 0.1)
total_bill= (bill + (bill * 0.1)) / no_of_persons
bill_per_person=round(total_bill,2)
print(f"Each person should pay: $ {bill_per_person}")