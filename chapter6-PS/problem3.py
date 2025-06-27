# WAP in python to detect the spam message.
# A message is considered spam if it contains the words "make a lot of money", "buy now", "click this", or "subscribe this".
def is_spam_message(message):
    spam_keywords = [
        "make a lot of money",
        "buy now",
        "click this",
        "subscribe this"
    ]
    
    # Check if any spam keyword is in the message
    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            return print("The comment is a spam.")
    print("The comment is not a spam.")

message = input("Enter comment: ")
is_spam_message(message)

#------------------------------------------------------------------
# Alternate way using no fucntions
# WAP in python to detect the spam message without using functions.
# A message is considered spam if it contains the words "make a lot of money", "buy now", "click this", or "subscribe this".
comment = input("Enter comment: ")
spam_keywords = [
    "make a lot of money",
    "buy now",
    "click this",
    "subscribe this"
]
# Check if any spam keyword is in the message
is_spam = False
for keyword in spam_keywords:
    if keyword.lower() in comment.lower():
        is_spam = True
        break
if is_spam:
    print("The comment is a spam.")
else:
    print("The comment is not a spam.")
        