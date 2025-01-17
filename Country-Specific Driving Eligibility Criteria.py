# This program determines a user's driving eligibility based on their age and country. The user selects a country from a predefined list (South Africa, Mexico, India, and France), and the program checks whether they meet the driving age requirements for that country.
# Driving Eligibility Checker

# List of supported countries
countries = ["South Africa", "Mexico", "India", "France"]

# Get user input
country = input(f"Select a country from {countries}: ")
user_age = int(input("Enter your age: "))

# Check driving eligibility based on country
if country == "South Africa":
    if user_age >= 17:
        print("You can drive in south africa.")
    else:
        print("You are not eligible to drive in this country.")

elif country == "Mexico":
    if user_age >= 18:
        print("You can drive in mexico.")
    elif user_age >= 16:
        print("You can drive with parental agreement.")
    elif user_age >= 15:
        print("You can drive with parental supervision.")
    else:
        print("You can't drive in mexico.")

elif country == "India":
    if user_age >= 18:
        print("You are eligible to drive in india.")
    elif 16 <= user_age < 18:
        print("You're eligible for driving a scooty with a learning license.")
    else:
        print("You're not eligible to drive in india.")

elif country == "France":
    if user_age >= 18:
        print("You can drive in france.")
    elif user_age >= 15:
        print("You can drive with parental supervision.")
    else:
        print("You can't drive in france.")

else:
    print("Sorry, driving eligibility data is not available for this country.")