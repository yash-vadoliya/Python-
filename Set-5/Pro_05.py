# 5. Allow users to enter multiple strings in the list; arrange the entered string into alphabetical order and display.


strings = []

print("Enter multiple strings ")
while True:
    string = input("\nEnter a string: ")
    if string.lower() == ' ':
        break
    strings.append(string)


strings.sort()


print("\nSorted strings")
for string in strings:
    print(string)
