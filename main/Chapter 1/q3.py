import os

directory_path = '/Program Files' # USE / ALWAYS FOR DIRECTORY INITIALIZATION

contents = os.listdir(directory_path)

for item in contents:
    print(item)