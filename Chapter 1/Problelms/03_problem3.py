# problem 3
import os

# Path of the directory
path = r"C:\Users\Home\OneDrive\Documents\Python\Chapter1"

# Get list of files and folders
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)