# WAP in python to remove a given word from a list and strip at the same time
# print("\nRemove operation using a function:")
# print("-------------------------------------------")
list_of_words = ["Alice", "Amar", "Shivani", "Mathavan", "Aishwarya", "Daphne", "Mark", "Timothy", "Furqan", "Rupali", "Datta", "Anamaya"]
def remove_word(word_list, word):
    for item in word_list:
            word_list.remove(word)
            return word_list

print(f"List of words: {list_of_words}")
word_to_remove = input("Enter the word to be removed from the list:") 
print(f"Output list: {remove_word(list_of_words, word_to_remove)}")

print("\nStrip operation using a function:")
print("--------------------------------")
list_of_words = [" Alice ", "Amar", " Shivani", "Mathavan ", " Aishwarya ", "Daphne", "Mark", "Timothy", "Furqan", "Rupali", "Datta", "Anamaya"]

def strip_word(word_list, substring):
    # strip() only removes characters from the start and end, not in the middle
    return [word.strip(substring) for word in word_list]

print(f"List of words before strip: {list_of_words}")
substring_to_strip = input("Enter the substring (characters) to strip from start/end of each word: ")
stripped_list = strip_word(list_of_words, substring_to_strip)
print("Output stripped list:", stripped_list)
