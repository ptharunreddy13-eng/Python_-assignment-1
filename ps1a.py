# Part A: House Hunting
# Name:Tharun P

# Get inputs from user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
# give information
down_payment = 0.25 * total_cost
annual_return = 0.04
current_savings = 0
months = 0
monthly_salary = annual_salary / 12
# Loop until we have enough money
while current_savings < down_payment:
    # Monthly investment return
    current_savings += current_savings * (annual_return / 12)
    # Monthly saving from salary
    current_savings += monthly_salary * portion_saved
    # Count month 
    months += 1
# result
print("Number of months:", months)