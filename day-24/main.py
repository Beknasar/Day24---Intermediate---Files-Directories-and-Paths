# read file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write file with delete everything in it
# with open("new_file.txt", mode='w') as file:
#     contents = file.write("Just Monika")
#     print(contents)

# write file with just appending new text
# with open("my_file.txt", mode='a') as file:
#     contents = file.write("\nJust Monika")
#     print(contents)

# ../../new_file.txt
# ../../../new_file.txt
with open("../new_file.txt") as file:
    contents = file.read()
    print(contents)
