# Homework Assignment 2: Python Basics & GitHub Introduction

**Course:** - CSC 121 Introduction to Python and Data Science  
**Week:** 1  
**Lecture:** 02 - Python Basics & GitHub Repositories  
**Due Date:** Before Lecture 4 (Week 2)  
**Points:** 100 points  

---

## Assignment Overview

This assignment will help you practice the fundamental Python concepts we learned in class and get you started with GitHub. You'll work with variables, data types, and print statements, then create your first GitHub repository.

**IMPORTANT SUBMISSION FORMAT:** You must submit your entire homework as ONE Python file named `homework02_lastname_firstname.py` with clearly marked sections and question numbers as shown in the template below.

---

## Learning Objectives

By completing this assignment, you will:
- Create and use Python variables with different data types
- Write effective print statements to display information
- Understand basic GitHub terminology and concepts
- Create your first GitHub repository
- Upload and commit a simple file to GitHub

---

## Submission Template

**You MUST use this exact template structure in your Python file:**

```python
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
```

---

## Detailed Instructions

### Step 1: Download the Template
1. Copy the entire template code above
2. Create a new Python file named `homework02_lastname_firstname.py` (replace with your actual last name and first name)
3. Paste the template code into your file

### Step 2: Complete Section 1 (Basic Understanding)
- Replace each answer with the correct letter (a, b, c, or d) or True/False
- Do NOT change the question numbers or section headers
- Keep the `print` statements exactly as shown

### Step 3: Complete Section 2 (Application)
- **Part A:** Replace the placeholder values with your actual information
- **Part B:** Complete the GitHub tasks and fill in your repository information
- Make sure all variables have real values, not placeholder text

### Step 4: GitHub Repository Tasks
You must complete these GitHub tasks and update the corresponding variables in your Python file:

1. **Create Repository:**
   - Name: `test[yourfirstname]` (example: `testsarah`)
   - Description: "My first GitHub repository for CSC 121"
   - Make it Public
   - Add a README file

2. **Create and Upload File:**
   - Create a file named `github_exercise.txt`
   - Content should be exactly:
     ```
     [Your First Name] [Your Last Name]
     [Today's Date]
     ```
   - Commit message: "Add github exercise file"

3. **Update Python File:**
   - Fill in your actual GitHub username
   - Fill in your actual repository name
   - Fill in the complete repository URL
   - Set all the `github_tasks_completed` values to `True`

### Step 5: Test Your Code
- Run your Python file to make sure it executes without errors
- Check that all your information displays correctly
- Verify that no placeholder text remains

---

## Submission Requirements

### What to Submit:
1. **Python File:** `homework02_lastname_firstname.py` with all sections completed
2. **GitHub Repository URL:** Include this in your Python file and also submit separately

### Submission Checklist:
- [ ] Python file follows the exact template structure
- [ ] All section headers and question numbers are preserved
- [ ] All questions in Section 1 are answered
- [ ] All personal information in Section 2 is filled in with real data
- [ ] GitHub repository is created with the correct name
- [ ] `github_exercise.txt` file is uploaded to repository
- [ ] All placeholder text is replaced with actual information
- [ ] Code runs without errors

### File Naming Convention:
- **Correct:** `homework02_smith_john.py`
- **Incorrect:** `homework2.py`, `assignment.py`, `HW02.py`

---

## Automated Grading Information

**For Students:** It's crucial to:
- Follow the exact template structure
- Keep all section markers and question numbers
- Use the exact variable names shown
- Not delete or modify any section headers

**In grading I will look for:**
- Correct answers to multiple choice questions
- Proper variable assignments
- Complete personal information
- Evidence of GitHub repository creation
- Proper file naming and structure

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Section 1: Questions 1-10** | 50 pts | 5 points each for correct answers |
| **Personal Information Program** | 15 pts | All variables filled with real data, creative f-string |
| **Fixed Errors Code** | 10 pts | All errors corrected, code runs properly |
| **GitHub Repository** | 20 pts | Repository created, file uploaded, proper naming |
| **Repository Information** | 5 pts | Correct URLs and information in Python file |
| **Code Structure & Execution** | 5 pts | Follows template, runs without errors |
| **Reflection (Bonus)** | 5 pts | Thoughtful responses to reflection questions |
| **Total** | 105 pts | (100 pts + 5 bonus) |

---

## Common Mistakes to Avoid

1. **Changing section headers or question numbers**
2. **Leaving placeholder text like "YourFirstName"**
3. **Incorrect file naming**
4. **Not creating the GitHub repository**
5. **Syntax errors that prevent code from running**
6. **Wrong variable names**
7. **Not following the exact template structure**

---

## Getting Help

- **Office Hours:** [Tuesdays 12pm - 12:40pm ]
- **Course Forum:** Post questions about concepts
- **Email:** maperezrodriguez602@alamancecc.edu
- **GitHub Help:** [GitHub Hello World Guide](https://guides.github.com/activities/hello-world/)

Remember: Please follow the template precisely!
