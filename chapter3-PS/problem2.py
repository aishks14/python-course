# WAP in python to fill in a letter template with name and date.
letter_template = """Dear <|Name|>,
Greetings from ABC Organization!
We are pleased to inform you that you have been selected for the position of Software Engineer.
Your joining date is <|Date|>."""

# Get user input for name and date
name = input("Enter your name: ")
date = input("Enter the date: ")

# Fill in the letter template
filled_letter = letter_template.replace("<|Name|>", name).replace("<|Date|>", date)

# Print the original letter template
print("\nOriginal Letter Template:")
print("-------------------------")
print(letter_template)

# Print the filled letter
print("\nFilled Letter:")
print("-----------------")
print(filled_letter)