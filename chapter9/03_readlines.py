# Python code to read a file and lines inside it and put them in a list using readlines() function
file = open("readlines.txt") # Reading file and its text
lines = file.readlines() # It will read the lines and put them in a list. This function reads line whenever it is called
print("Printing the lines in a list: \n\t", lines, "\n Type of the lines: \n\t", type(lines))
file.close()

