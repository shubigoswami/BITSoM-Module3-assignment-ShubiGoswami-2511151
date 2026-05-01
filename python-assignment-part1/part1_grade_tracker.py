##Task 1 - Data Parsing & Profile cleaning 

#Given Data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]


def clean_student(student):
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = [int(x.strip()) for x in student["marks_str"].split(",")]

    return {
        "name": name,
        "roll": roll,
        "marks": marks
    }


def is_valid_name(name):
    return all(word.isalpha() for word in name.split())


def print_profile(student):
    name = student["name"]
    roll = student["roll"]
    marks = student["marks"]

    # name validation
    status = "✓ Valid name" if is_valid_name(name) else "✗ Invalid name"
    print(f"{name} → {status}")

   
    print(f"Student: {name}")
    print(f"Roll No: {roll}")
    print(f"Marks  : {marks}")
    print("-" * 35)


cleaned_students = []

for s in raw_students:
    cleaned = clean_student(s)
    cleaned_students.append(cleaned)
    print_profile(cleaned)


# special case
for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSpecial Output for Roll 103:")
        print(s["name"].upper())
        print(s["name"].lower())


##Task 2 — Marks Analysis Using Loops & Conditionals 

#Given Data

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]


#  1. Grades to be given based on Marks
print(f"\nReport for {student_name}\n")

for sub, mark in zip(subjects, marks):

    if 90 <= mark <= 100:
        grade = "A+"
    elif 80 <= mark <= 89:
        grade = "A"
    elif 70 <= mark <= 79:
        grade = "B"
    elif 60 <= mark <= 69:
        grade = "C"
    else:
        grade = "F"

    print(f"{sub}: {mark} → Grade {grade}")


# 2. Marks Summary

#Total Marks
total = sum(marks)

#Average Marks
average = round(total / len(marks), 2)

# Highest Marks
max_mark = max(marks)
max_index = marks.index(max_mark)

# Lowest Marks
min_mark = min(marks)
min_index = marks.index(min_mark)

print("\nSummary:")
print(f"Total Marks : {total}")
print(f"Average     : {average}")
print(f"Highest     : {subjects[max_index]} ({max_mark})")
print(f"Lowest      : {subjects[min_index]} ({min_mark})")


# 3. Using While Loop - Adding Subjects
new_count = 0

while True:
    subject = input("\nEnter subject name (or type 'done' to stop): ").strip()

    if subject.lower() == "done":
        break

    mark_input = input(f"Enter marks for {subject}: ").strip()

    # validate marks
    if not mark_input.isdigit():
        print("⚠ Invalid input! Marks must be a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("⚠ Marks should be between 0 and 100.")
        continue

    # valid entry → add
    subjects.append(subject)
    marks.append(mark)
    new_count += 1

    print(f"Added: {subject} ({mark})")


# ---------- Final Output ----------
updated_avg = round(sum(marks) / len(marks), 2)

print("\n--- Update Complete ---")
print(f"New subjects added : {new_count}")
print(f"Updated Average    : {updated_avg}")


#Task3 - Class Performance Summary

#Given Data

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

results = []

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_class_avg = 0


for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)

    status = "Pass" if avg >= 60 else "Fail"

    # count pass/fail
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    # track topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    total_class_avg += avg

    results.append((name, avg, status))


# Student Report 

print("\nClass Report\n")

print(f"{'Name':<18} | {'Average':<7} | Status")
print("-" * 40)

for name, avg, status in results:
    print(f"{name:<18} | {avg:<7} | {status}")


# Final SUmmary

class_avg = round(total_class_avg / len(class_data), 2)

print("\nSummary:")
print(f"Passed Students : {pass_count}")
print(f"Failed Students : {fail_count}")
print(f"Topper          : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_avg}")

#Task 4 — String Manipulation Utility

#Given String Data

essay = "python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning."

#1. Strip whitespaces
clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)


# 2. Title Case 
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)


# 3. Counting 'python' 
count_python = clean_essay.count("python")
print("\n3. Count of 'python':")
print(count_python)


#  4. Replaceing 'python'
replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. After Replacement:")
print(replaced)


# 5. Split into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentences List:")
print(sentences)


# 6. Numbering sentences
print("\n6. Numbered Sentences:")

for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()

    # ensure sentence ends with '.'
    if not sentence.endswith("."):
        sentence += "."

    print(f"{i}. {sentence}")