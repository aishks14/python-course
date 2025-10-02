# Check word "python" in a text/html (log) file, if it is present or not. Count the number of repetitions
word = "Python"
file = "problem6_log.txt"
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