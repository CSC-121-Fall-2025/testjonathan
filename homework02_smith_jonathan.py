#!/usr/bin/env python3
"""
Homework Assignment 2: Python Basics & GitHub Introduction
Student Name: [Jonathan Smith]
Student ID: [1062370]
Date: [9/9/2025]
Course: CSC 121 - Introduction to Python and Data Science

INSTRUCTIONS: 
- Replace [Your Full Name], [Your Student ID], and [Submission Date] above
- Complete each section below
- Keep all section headers and question numbers exactly as shown
- Add your answers/code after each question
- Do not delete any section markers or question numbers
"""

# ============================================================================
# SECTION 1: BASIC UNDERSTANDING (50 points)
# ============================================================================

print("=== SECTION 1: BASIC UNDERSTANDING ===")

# Question 1 (5 points)
# What is a variable in Python?
# a) A number that changes
# b) A container that stores data values  
# c) A type of function
# d) A way to print text
# 
# Your answer:
question_1_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 1 answer:", question_1_answer)

# Question 2 (5 points)
# Which of these is a string data type?
# a) 25
# b) 3.14
# c) "Hello World"
# d) True
#
# Your answer:
question_2_answer = "c"  # Replace with your answer (a, b, c, or d)
print("Question 2 answer:", question_2_answer)

# Question 3 (5 points)
# What will this code print?
# name = "Alice"
# age = 20
# print("My name is", name, "and I am", age, "years old")
#
# a) My name is Alice and I am 20 years old
# b) My name is name and I am age years old
# c) name Alice age 20
# d) This code will cause an error
#
# Your answer:
question_3_answer = "a"  # Replace with your answer (a, b, c, or d)
print("Question 3 answer:", question_3_answer)

# Question 4 (5 points)
# Which variable name follows Python naming rules?
# a) 2student
# b) student-name
# c) student_name
# d) student name
#
# Your answer:
question_4_answer = "c"  # Replace with your answer (a, b, c, or d)
print("Question 4 answer:", question_4_answer)

# Question 5 (5 points)
# What data type is the number 3.75?
# a) Integer
# b) Float
# c) String
# d) Boolean
#
# Your answer:
question_5_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 5 answer:", question_5_answer)

# Question 6 (5 points)
# True or False: In Python, you need to put quotes around variable names 
# when using them in print statements.
#
# Your answer:
question_6_answer = "False"  # Replace with True or False
print("Question 6 answer:", question_6_answer)

# Question 7 (5 points)
# What is a GitHub repository?
# a) A type of Python variable
# b) A place to store and manage your code files
# c) A way to print information
# d) A data type
#
# Your answer:
question_7_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 7 answer:", question_7_answer)

# Question 8 (5 points)
# What does "commit" mean in GitHub?
# a) To delete a file
# b) To save changes to your repository with a message
# c) To create a new repository
# d) To download files
#
# Your answer:
question_8_answer = "b"  # Replace with your answer (a, b, c, or d)
print("Question 8 answer:", question_8_answer)

# Question 9 (5 points)
# True or False: You need to install special software on your computer 
# to create a GitHub repository.
#
# Your answer:
question_9_answer = "False"  # Replace with True or False
print("Question 9 answer:", question_9_answer)

# Question 10 (5 points)
# What should you include when creating a commit message?
# a) Your password
# b) Random letters and numbers
# c) A brief description of what you changed
# d) Your full name and address
#
# Your answer:
question_10_answer = "c"  # Replace with your answer (a, b, c, or d)
print("Question 10 answer:", question_10_answer)

# ============================================================================
# SECTION 2: APPLICATION (50 points)
# ============================================================================

print("\n=== SECTION 2: APPLICATION ===")

# ----------------------------------------------------------------------------
# Part A: Python Programming (25 points)
# ----------------------------------------------------------------------------

print("\n--- Part A: Python Programming ---")

# Task 1: Personal Information Program (15 points)
print("\nTask 1: Personal Information Program")

# REQUIREMENTS:
# 1. Create variables for the following information about yourself:
#    - first_name (your actual first name as a string)
#    - last_name (your actual last name as a string)
#    - age (your actual age as an integer)
#    - favorite_color (your favorite color as a string)
#    - favorite_number (your favorite number as an integer)
#    - hometown (your hometown as a string)
#
# 2. Display this information using print statements in a clear, organized format
#
# 3. Create a variable called 'creative_statement' that contains an f-string
#    sentence using at least 3 of your variables, then print it
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

first_name = "Jonathan"
last_name = "Smith"
age = 25
favorite_color = "blue"
favorite_number = 12
hometown = "Durham"

print("First Name: ", first_name)
print("Last Name: ", last_name)
print("Age: ", age)
print("Favorite Color: ", favorite_color)
print("Favorite Number: ", favorite_number)
print("Hometown: ", hometown)

creative_statement = f"There once was a man named {first_name} who lived in a city called {hometown} and had {favorite_number} children."

print(creative_statement)

# Task 2: Fix the Errors (10 points)
print("\nTask 2: Fixed Code")

# INSTRUCTIONS: The code below contains several errors that prevent it from running.
# Fix all the errors so the code runs properly and calculates correctly.
# 
# IMPORTANT: You must keep the final variable names as:
# - student_name
# - student_age  
# - favorite_subject
# - graduation_year
#
# These exact variable names are required for grading compatibility.
#
# BROKEN CODE (fix the errors below):

student_name = "John"
student_age = 20
favorite_subject = "Data Science"

print("Student name:", student_name)
print("Age:", student_age, "years old")
print("Favorite subject:", favorite_subject)

graduation_year = 2025 + student_age
print("Graduation year:", graduation_year)

# ----------------------------------------------------------------------------
# Part B: GitHub Practice (25 points)
# ----------------------------------------------------------------------------

print("\n--- Part B: GitHub Practice ---")

# Task 3: GitHub Repository Information (25 points)
print("\nTask 3: GitHub Repository Information")

# REQUIREMENTS:
# You must complete the following GitHub tasks, then create the variables below
# to document what you accomplished:
#
# GITHUB TASKS TO COMPLETE:
# 1. Create a new public repository named "test[yourfirstname]" (example: "testjohn")
# 2. Add a README file when creating the repository
# 3. Create a text file named exactly "github_exercise.txt" 
# 4. In the text file, put your full name on the first line and today's date on the second line
# 5. Upload the text file to your repository
# 6. Make a commit with the message "Add github exercise file"
#
# VARIABLES TO CREATE:
# After completing the GitHub tasks above, create these variables with your actual information:
# - github_username (string: your actual GitHub username)
# - repository_name (string: your actual repository name)
# - repository_url (string: the complete URL to your repository)
# - file_created (string: must be exactly "github_exercise.txt")
# - commit_message (string: must be exactly "Add github exercise file")
#
# IMPORTANT: Use the exact variable names listed above for grading compatibility
#
# Write your code below:

github_username = "jpsmith370-png"
repository_name = "testjonathan"
repository_url = "https://github.com/CSC-121-Fall-2025/testjonathan.git"
file_created = "github_exercise.txt"
commit_message = "Add github exercise file"

# Verification that you completed the GitHub tasks:
github_tasks_completed = {
    "created_repository": True,      # Set to True if you created the repository
    "uploaded_txt_file": True,       # Set to True if you uploaded github_exercise.txt
    "file_contains_name_date": True, # Set to True if file contains your name and date
    "made_commit": True              # Set to True if you made a commit
}

print("GitHub Tasks Completed:", github_tasks_completed)
# ============================================================================
# REFLECTION SECTION (Bonus - 5 points)
# ============================================================================

print("\n=== REFLECTION SECTION ===")

# Answer these reflection questions by replacing the placeholder text:
reflection_1 = "The most challenging thing to me was the f strings, since they were a new concept to me."
reflection_2 = "I learned that f strings can be set as variables in Python."
reflection_3 = "It's confusing, but I think I'll get the hang of it soon."

print("Most challenging part:", reflection_1)
print("What I learned about Python:", reflection_2)
print("Thoughts about GitHub:", reflection_3)

# ============================================================================
# END OF HOMEWORK ASSIGNMENT
# ============================================================================

print("\n=== HOMEWORK ASSIGNMENT COMPLETED ===")
print("Student:", first_name, last_name)
print("All sections completed successfully!")