# ps1b.py
# Part B: Saving with a Raise
# Inputs
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
# Constants
down_payment = 0.25 * total_cost
annual_return = 0.04
# Initial values
current_savings = 0
months = 0
# Loop until down payment reached
while current_savings < down_payment:
    monthly_salary = annual_salary / 12
    # Add investment return
    current_savings += current_savings * (annual_return / 12)
    # Add monthly savings
    current_savings += monthly_salary * portion_saved
    months += 1
    # Salary raise every 6 months
    if months % 6 == 0:
        annual_salary = (annual_salary +(annual_salary*semi_annual_raise))
# Output
print("Number of months:", months)