# My solution
# # TODO: Create a letter using starting_letter.txt
# with open("./Input/Letters/starting_letter.txt", mode='r') as letter_file:
#     letter = letter_file.read()
#
# with open("./Input/Names/invited_names.txt", mode='r') as name_file:
#     names = name_file.readlines()
#
# # for each name in invited_names.txt
# # Replace the [name] placeholder with the actual name.
# for name in names:
#     name = name.strip("\n")
#     with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
#         message = letter.replace("[name]", name)
#         file.write(message)

# Angela's solution
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", mode='r') as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode='r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
