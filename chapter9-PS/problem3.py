# WAP in python to replace a word with hash symbol, such as if a file contains a word "bad", replace it with "###" and update the same file
word = "bad"
with open('problem3.txt', 'r') as file:
    content = file.read()
    updated_content = content.replace(word, "###")
    
with open('problem3.txt', 'w') as file:
    file.write(updated_content)

    
    
    