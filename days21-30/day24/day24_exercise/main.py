# Day 24 exercises, practicing with open method.

# Opening a local txt file and reading contents
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Alternative open method:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Opening in write-mode and writing to file:
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")

# Append mode
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text 2.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)