# WAP in python to check whether a given username contains less than 10 characters (error message to be printed), starts with an alphabet, and contains only alphanumeric characters.

username = input("Enter a username: ")
if len(username) > 10 and username[0].isalpha() and username.isalnum():
    print("The username is valid.")
else:
    print("Error: The username is invalid.\nIt must be less than 10 characters, start with an alphabet, and contain only alphanumeric characters.")