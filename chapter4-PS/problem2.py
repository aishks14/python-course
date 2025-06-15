# WAP in python to accept the marks of 6 students and display them in alphabetical order of their names.
# students = []
# for i in range(6):
#     name = input(f"Enter the name of student {i + 1}: ")
#     marks = input(f"Enter the marks of {name}: ")
#     students.append((name, marks))

#WAP in python to store seven marks in a list entered by the user. Then display the list in alphabetical order.
marks = []
print("Enter and sort marks of 6 students:")
print("-----------------------------------")
m1 = float(input("Enter first marks here: "))
marks.append(m1)
m2 = float(input("Enter second marks here: "))
marks.append(m2)
m3 = float(input("Enter third marks here: "))
marks.append(m3)
m4 = float(input("Enter fourth marks here: "))
marks.append(m4)
m5 = float(input("Enter fifth marks here: "))
marks.append(m5)
m6 = float(input("Enter sixth marks here: "))
marks.append(m6)

# Display the list in alphabetical order
marks.sort()
print("Marks in sorted order:", marks)

# Alternatively, you can use a loop to collect the marks
print("\n")
print("Alternate way to enter and sort marks of 6 students:")
print("----------------------------------------------------")
marks = []
for i in range(6):
    mark = float(input(f"Enter marks {i + 1}: "))
    marks.append(mark)
marks.sort()
print("Marks in sorted order:", marks)



