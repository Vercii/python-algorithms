numList = []

for _ in range(5):
    num = int(input("Enter a number: "))
    numList.append(num) # appends the inputs to the list

num_search = int(input("Search for a number: "))

checked = 0
for checker in range(len(numList)): # gets range of the list's length
    if num_search == numList[checker]: #  searches every index
        checked += 1 # adds value if true
        break # breaks if found

if checked == 1:
    print("Found at index: ", checker)
else:
    print("Nothing here!")