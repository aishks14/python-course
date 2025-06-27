# WAP in python to check whetger a post is talking about python or not.

post = input("Enter a post: ")
if "python" in post.lower():
    print("The post is talking about Python.")
else:
    print("The post is not talking about Python.")