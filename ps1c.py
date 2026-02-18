# ps1c.py
# Part C: Finding the Right Amount to Save
# name:Tharun P
# Collaborators: None
# Input
starting_salary = float(input("Enter the starting salary: "))
# Constants
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
r = 0.04
semi_annual_raise = 0.07
months = 36
# Bisection search setup
low = 0
high = 10000
steps = 0
epsilon = 100
best_rate = None
# Check if possible with 100% saving
current_savings = 0
annual_salary = starting_salary
monthly_salary = annual_salary / 12
for i in range(months):
    current_savings += current_savings * (r / 12)
    current_savings += monthly_salary * 1.0
    if (i + 1) % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
        current_savings = 0
        annual_salary = starting_salary
        monthly_salary = annual_salary / 12
        for i in range(months):
            current_savings += current_savings * (r / 12)
            current_savings += monthly_salary * rate
            if (i + 1) % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_salary = annual_salary / 12
        if abs(current_savings - down_payment) <= epsilon:
            best_rate = rate
            break
        elif current_savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1
    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)