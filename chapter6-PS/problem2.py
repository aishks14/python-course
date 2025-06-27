# WAP in python to calculate the percentage of marks obtained by a student in five subjects and display the result based on the percentage.
# Also check if each subject is greater than or equal to 33, then we calculate the percentage

subjects = 5
marks = []
print("Enter marks for 5 subjects:")
for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)  
total_marks = sum(marks)
max_marks = subjects * 100  # Assuming each subject is out of 100
percentage = (total_marks / max_marks) * 100
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
if percentage >= 90 and all(mark >= 33 for mark in marks):
    result = "A+ - Marvelous"
elif percentage >= 85 and all(mark >= 33 for mark in marks):
    result = "A - Excellent"
elif percentage >= 80 and all(mark >= 33 for mark in marks):
    result = "B+ - Very Good"
elif percentage >= 75 and all(mark >= 33 for mark in marks):
    result = "B - Good"
elif percentage >= 70 and all(mark >= 33 for mark in marks):
    result = "C+ - Satisfactory"
elif percentage >= 65 and all(mark >= 33 for mark in marks):
    result = "C - Average"
elif percentage >= 60 and all(mark >= 33 for mark in marks):
    result = "D+ - Below Average"
elif percentage >= 50 and all(mark >= 33 for mark in marks):
    result = "D - Poor"
elif percentage >= 40 and all(mark >= 33 for mark in marks):
    result = "E - Very Poor"
else:
    if any(mark < 33 for mark in marks):
        result = "F - Fail"
        reason = "Failed because marks are less than 33 in one or more subjects."
       
    else:
        result = "F - Fail"
        reason = "Failed because overall percentage is below 40%."

print(f"Result: {result}\nReason: {reason}" if 'reason' in locals() and reason else f"Result: {result}")