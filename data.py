# w writing a appending r reading r+ reading/writing
# file = open("./data.csv", "r+")
# file.write("id,name,email\n")
# file.write("1,John,john@gmail.com\n")
# file.write("2,Alex,alex@gmail.com\n")

import os.path

filename = "data.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")

# for line in file:
#     print(file)
# print(file.readlines())
# file.close()