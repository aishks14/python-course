# Python code to read line one by one 
LINE_TYPE = "Type of the line:\n\t"
file = open("readlines.txt") # Reading file and its text
print("Printing the lines one by one:\n\t")

line1 = file.readline() 
print(line1,LINE_TYPE, type(line1))

line2 = file.readline() 
print(line2,LINE_TYPE , type(line2))

line3 = file.readline() 
print(line3,LINE_TYPE, type(line3))

line4 = file.readline() 
print(line4,LINE_TYPE, type(line4))

line5 = file.readline() 
print(line5,LINE_TYPE, type(line5))

file.close()