# Python makes file I/O (Input/Output) operations incredibly straightforward and powerful

# Opens a file for any opration in different mode. By default the file remains in read mode and hence no second parameter is passed
file = open("about_python.txt") 
# Reading the file
file_data = file.read() 

# Printing the content of the file
print(file_data)

# Closing the file
file.close()
