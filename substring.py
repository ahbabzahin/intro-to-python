def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# Input from user
string = input("Enter a string: ")

# Get all substrings
result = all_substrings(string)

# Print the substrings
print("All substrings:")
for sub in result:
    print(sub)
