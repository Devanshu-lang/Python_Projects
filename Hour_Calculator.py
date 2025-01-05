# This calculator is built to calculate the reamining hours left in a day and 5 days working week.
# This time hour calculator considered and built for weekdays calculation

import time

# Ask to user that how many hours do you sleep
Sleep = float(input("How many hours do you sleep? "))

# Ask the user for eating hours.
Eat = float(input("How many hours you generally spend for breakfast, lunch and dinner? "))

# Ask the user that how many hours S.he works. 
Work = float(input("How many hours do you work per day including commute? "))

# Ask the user that how many hours S.he spend on social media
Social = float(input("How many hours do you spend on social media? "))

# Ask the user that how many many hours S.he generally spend on learning skills
learning = float(input("How many hours do you spend on learning skills? "))

Total_Hours = 24 # Total Hours in a day

Week_Hours = 120 # 24 * 5 working days

sum = Eat + Work + Sleep + Social + learning # Number of hours spend in a day.

final_sum = Total_Hours - sum # Formula is 24 - hours spent.

Sum_multiply = final_sum * 5 # Remaining hours in a day * 5 working days

Week_Hours_Sum = final_sum * 5 # Formula is 120(24*5) - hours spent in working days

time.sleep(2)
print("The remaning hours left in a day is " + str(final_sum)) #Hours left in a day.
time.sleep(2)
print("In working days you have total " + str(Week_Hours_Sum) + " left in a week") #Hours left in a week.