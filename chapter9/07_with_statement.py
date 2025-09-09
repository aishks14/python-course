# `with`` statement Automatically handles closing the file
with open("mypythonfile.txt", "r") as file:
    print(file.read())
    
# Read binary file
with open("python.png", "rb") as file:
    data = file.read()
    print(data)