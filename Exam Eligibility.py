# The purpose of this is to check eligibility for taking the exam.

Exam = "UPSC" # Name of the exam

# Name of the candidate appearing for the exam.

name = input("What is your name? ")

# What is the age of the candidate

age = int(input("What's your age? "))

# If the candidate's age is 21 or older, they are eligible.

if age >= 21:  
     print("You are eligible for giving the " + Exam, "exam.")

# The candidate is not eligible to take this exam. However, they may qualify for other exams that match the age criteria.

elif age >=18 and age <=21:
     print("You are not eligible for this " + Exam, "exam, but alternatively can you fill other exam forms for whom the age criteria is below 21")
     
# The candidate is not eligible to appear in any of the exams

else:
    print("You are not eligible for giving the " + Exam, "exam, as you are below 18 and are not eligible.")

#Thank you, viewers! I am currently in the learning stage and may make some mistakes. Please let me know what improvements are needed. Once again, thank you for taking the time.
