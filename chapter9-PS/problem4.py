# WAP in python to replace a word with hash symbol, same as problem3 but using seek() and replace() methods, and mode to be used as "r+"
word = "bad"
with open('problem3.txt', 'r+') as file:
    content = file.read()
    file.seek(0)  # Move cursor to the beginning
    updated_content = content.replace(word, "###")
    file.write(updated_content)
    
    