# TASK 3: Task Automation with Python Scripts 
# ● Goal: Automate a small, real-life repetitive task. 
# ● Scope:
# ○ Extract all email addresses from a .txt file and save them to another file. 
# ● Key Concepts Used: re, file handling.

import re

# Ask user for input and output file names
input_file = input("Enter the path to the .txt file to scan for emails: ")
output_file = input("Enter the filename to save found email addresses: ")

# Read the input file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Find all email addresses using regex
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)

# Remove duplicates and sort
unique_emails = sorted(set(emails))

# Write the emails to the output file
with open(output_file, "w", encoding="utf-8") as f:
    for email in unique_emails:
        f.write(email + "\n")

print(f"Found {len(unique_emails)} unique email addresses. Saved to {output_file}.")
