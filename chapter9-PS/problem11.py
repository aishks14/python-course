# WAP in python to rename a file
with open("problem11.txt") as file:
    content = file.read()
    
with open("problem11_renamed.txt", "w") as file:
    file.write(content)
    
    
# Note: After the operation is performed by this file, remove the original file("problem11.txt") manually. 
# OR else use os module to delete it using functions.