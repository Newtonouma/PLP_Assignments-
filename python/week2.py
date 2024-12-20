#1: Creating an empty list
my_list = []

#2: Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#3 Inserting 15 at the second position
my_list.insert(1, 15)

#4: Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

#5: Removing the last element from the list
my_list.pop()

#6: Sorting the list in ascending order
my_list.sort()

#7: Finding and print the index of the value 30
index_of_30 = my_list.index(30)

print("Sorted list:", my_list)
print("Index of 30:", index_of_30)
