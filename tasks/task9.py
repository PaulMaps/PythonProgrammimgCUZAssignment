import re

# Task 9 - Full Code

text = """
Hello Anesu, my email is anesu@example.com. 
You can also reach out to mel123@school.co.zw or admin@techhub.org. 
We’ll meet on 2025-04-05. 
Let’s replace 'hard' with 'easy'. Also, try splitting this: 'Hi@Anesu#Good_Morning!' """

# 1️⃣ Extract all email addresses from text
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Extracted Emails:", emails)

# 2️⃣ Validate date format (YYYY-MM-DD)
date_pattern = r'^\d{4}-\d{2}-\d{2}$'

sample_dates = ["2025-04-05", "05-04-2025", "2025/04/05"]
for date in sample_dates:
    if re.match(date_pattern, date):
        print(f"{date} is valid.")
    else:
        print(f"{date} is INVALID.")

# 3️⃣ Replace all occurrences of a word
replaced_text = re.sub(r'\bhard\b', 'easy', text)
print("Replaced Text:", replaced_text)

# 4️⃣ Split by all non-alphanumeric characters
splits = re.split(r'\W+', "Hi@Anesu#Good_Morning!")
print("Split Parts:", splits)
