# WAP in python to replace number of words as like in problem3 and problem4 but there would be multiple words to be replaced
words = ["bad", "worse", "mood"]
with open('problem3.txt', 'r') as file:
    content = file.read()
    
for word in words:
    content = content.replace(word, "#" * len(word))
    
with open('problem3.txt', 'w') as file:
    file.write(content)