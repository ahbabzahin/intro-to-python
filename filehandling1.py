file_name = "sample.txt"

with open(file_name, "r") as f:
    data = f.read()
    print("Read entire file:\n", data)

with open(file_name, "r") as f:
    line = f.readline()
    print("\nRead one line:\n", line)

with open(file_name, "r") as f:
    lines = f.readlines()
    print("\nRead all lines into a list:\n", lines)

with open(file_name, "r") as f:
    print("\nReading line by line using loop:")
    for l in f:
        print(l.strip())
