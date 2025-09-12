# WAP in python check if content of one file identical to another file or not
with open("problem9a.txt") as file:
    content_9a = file.read()
    
with open("problem9b.txt") as file:
    content_9b = file.read()
    
if(content_9a == content_9b):
    print("File contents are identical. Below is the content:")
    print("--------------------------------------------------")
    print(content_9a)
    
else:
    print("File contents are not identical.")
