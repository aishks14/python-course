import os

# Specify the directory path (or use the current directory)
directory_path = "."

# List all files and folders in the directory
contents = os.listdir(directory_path)

print("Directory Contents:")
for item in contents:
    print(item)