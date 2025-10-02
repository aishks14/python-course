# WAP in pytho to read a file and find a word/string in it
stringToSearch = input('Enter the word to be searched:')

with open("poems.txt", "r") as fileToRead:  
    fileContent = fileToRead.read()
    
if stringToSearch.lower() in fileContent.lower():
    print("\n---------------------------------------------------\n")
    print(f"The word '{stringToSearch}' was found in the file. \n")
    print("---------------------------------------------------")
else:
    print("\n---------------------------------------------------\n")
    print(f" The word '{stringToSearch}' was NOT found in the file. \n")
    print("---------------------------------------------------")
    