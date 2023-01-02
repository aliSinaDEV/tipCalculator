print("welcome to the tip calculator.")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? %10, %12 or %15? %"))
split_bill_by = int(input("How many people to split the bill? "))

total_tip = tip_percentage / 100 * total_bill
final_bill_for_eachOne = (total_bill / split_bill_by) + (total_tip/split_bill_by)

print(f"Each person should pay: ${round(final_bill_for_eachOne,2)} \n")
