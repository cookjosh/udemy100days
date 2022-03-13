# Day 24 Mail Merge Project
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("Output/ReadyToSend/example.txt") as template_letter:
    letter_contents = template_letter.read()

with open("Input/Names/invited_names.txt") as first_file:
    contents = first_file.readlines()
    new_list = []
    for name in contents:
        name = name.strip()
        new_list.append(name)

for name in new_list:
    new_contents = letter_contents.replace("Aang", name)
    with open(f"./Output/ReadyToSend/Letter_for_{name}", "w") as new_file:
        new_file.write(new_contents)

