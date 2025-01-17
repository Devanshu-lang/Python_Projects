# Project 1: Exam Eligibility Checker

Description:This simple program allows candidates to check their eligibility for appearing in the UPSC exam based on their age. It provides tailored messages for different age groups and ensures that candidates understand their eligibility status for the specified exam.

Features:

Asks for the user's name and age.

Determines if the user meets the minimum age criteria of 21 for the UPSC exam.

Provides alternative suggestions for users aged between 18 and 21.

Displays a message for ineligible candidates below 18 years.

Usage:Run the program and follow the prompts to enter your name and age. The program will output your eligibility status for the UPSC exam.

Code Explanation:

Exam Name: The program defines Exam as "UPSC."

User Input: Collects name and age from the user.

Eligibility Logic:

Age 21 and above: Eligible for the UPSC exam.

Age between 18 and 21: Not eligible for UPSC but might qualify for other exams.

Age below 18: Not eligible for any exams due to age restrictions.

User-Friendly Messages: The program displays clear messages based on the user's age.

# Project 2: Time Management Calculator

Description:This program helps users calculate the remaining hours available in a day and a standard 5-day workweek after accounting for essential activities like sleep, eating, work, social media, and skill learning.

Features:

Collects input for daily time spent on various activities.

Calculates the remaining hours in a day after deducting the time spent on those activities.

Extends the calculation to show remaining hours for a 5-day workweek.

Provides insights into how users can better manage their time.

Usage:Run the program and follow the prompts to enter the hours you spend on sleep, meals, work, social media, and learning. The program will display the remaining hours available in a day and for a 5-day workweek.

Code Explanation:

Inputs:

Sleep: Hours spent sleeping.

Eat: Hours spent eating.

Work: Hours spent working (including commute).

Social: Hours spent on social media.

Learning: Hours spent learning new skills.

Total Hours in a Day: Set as 24.

Weekly Hours: Calculated as 24 * 5 = 120.

Calculations:

sum: Total hours spent on activities in a day.

final_sum: Remaining hours in a day (24 - sum).

Sum_multiply: Remaining hours multiplied by 5 for the workweek.

Output: Displays the remaining hours for a day and a 5-day week.

# Project 3: Driving Eligibility Checker

Description:This program determines a user's driving eligibility based on their age and selected country. The user picks a country from a predefined list (South Africa, Mexico, India, and France), and the program checks whether they meet the driving age requirements for that country.

Features:

Asks the user to select a country from a given list.

Collects the user's age as input.

Evaluates driving eligibility based on country-specific rules.

Provides different messages based on age requirements and driving conditions.

Displays an error message if data for the country is not available.

Usage:Run the program and enter the requested details. The program will output whether the user is eligible to drive in the selected country.

Code Explanation:

Supported Countries: South Africa, Mexico, India, and France.

User Input: Collects the selected country and age.

Eligibility Rules:

South Africa: Eligible to drive at 17+.

Mexico:

18+: Can drive.

16-17: Can drive with parental agreement.

15: Can drive with parental supervision.

India:

18+: Eligible to drive.

16-17: Can drive a scooty with a learning license.

France:

18+: Can drive.

15-17: Can drive with parental supervision.

Error Handling: Displays a message if the country is not in the supported list.

How to Run These Projects

Prerequisites:

Python 3.x installed on your system.

Basic understanding of Python and terminal usage.

Execution Steps:

Save the code as a .py file (e.g., exam_eligibility.py, time_calculator.py, or driving_checker.py).

Run the file in a Python IDE or using the command line:

python exam_eligibility.py

python time_calculator.py

python driving_checker.py

Follow the Prompts:

Enter the requested information when prompted.

Read the results displayed on the screen.

Suggestions and Feedback

These projects are beginner-friendly and demonstrate practical applications of Python. Feel free to suggest improvements or report issues on the GitHub repository.

Thank you for your support! 😊

![Driving_age_Flowchart](https://github.com/user-attachments/assets/32f15a5d-9978-44bb-a759-a5b23e6e26e7)
