# Take a word from the user as an input and search in the file. If found then show relevant message and the number of count.
print("--------------")
print("SEARCH A WORD")
print("--------------")
word = input("Enter a word which needs to be searched: ")
file = "problem6_log.html"
def text_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            count = content.count(word)
            if count > 0:
                print(f"The word '{word}' was found {count} times.")
            else:
                print(f"The word '{word}' was not found in the file.")
    except FileNotFoundError:
        print("File not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

text_occurrences(file)