# unordered collections of unique values stored in (Key-Value) pairs., mutable, unordered so we can't perform indexing and slicing

my_dict = {1: "Harry", 2: "Hermione", 3: "Ron"}

print(my_dict)
print(type(my_dict))

print(my_dict[3])

my_dict[1] = "Voldemort"
print(my_dict)