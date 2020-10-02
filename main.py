"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""

names = []

for x in range(3):
    names.append(input("Name: "))

found = False
search = input("Who would you like to search for? ")
print()
for x in range(len(names)):
    found = False
    if names[x] == search:
        found = True
        print("Found in position number " + str(x + 1))

if found == False:
    print("Not found")
