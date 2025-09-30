file_name = "data.txt"

with open(file_name, "w") as f:
    f.write("Hello World\n")
    f.write("This is a file handling example.\n")

with open(file_name, "a") as f:
    f.write("Adding a new line in append mode.\n")

with open(file_name, "r") as f:
    print("File Content:\n", f.read())

with open(file_name, "r") as f:
    lines = f.readlines()
    lines[0] = "Updated first line.\n"

with open(file_name, "w") as f:
    f.writelines(lines)

with open(file_name, "r") as f:
    print("\nAfter Update:\n", f.read())
