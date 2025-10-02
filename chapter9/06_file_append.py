
# Python program that appends any string or value at the end of the file. This will add everytime when this function is called.
# Notice here the file is opened here with append "a" mode
my_string = "\nThis is a python demo string, that can be used to be appended inside a file directly by file append operation"
file = open("file_for_append.txt", "a")
file.write(my_string)
file.close()