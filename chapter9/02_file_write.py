
my_string = "This is a python demo string, that can be used to be written inside a file directly by file write operation"
file = open("mypythonfile.txt", "w")
file.write(my_string)
file.close()