new_list = [1,2,3]  # creates a list
result = new_list[0]  # sets result to an element at index 0

try:
    new_list[5]
except IndexError:
    print("The value is not in range")

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

len(new_list)  # returns length of the list
new_list.append(4)  # adds 4 to the list
new_list.extend([5,6])  # adds a list of 5,6 to the list
new_list.insert(6,7)  # inserts 7 at the index 6
new_list.remove(7)  # removes 7 from the list
new_list.index(6)  # finds the index for an element 6



