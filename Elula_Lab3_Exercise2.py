
# Input the lists
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

# Using list comprehension to create a list of tuples
list_of_tuples = [(x, y) for x, y in zip(list1, list2)]

print(list_of_tuples)