# WAP in python to make a copy of a text file
with open("problem8.txt") as file:
    content = file.read()
    
with open("Problem8_copy.txt", "w") as file:
    file.write(content)
