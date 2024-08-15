# Define the data types
list_example = [1, 2, 3, 4]
tuple_example = (1, 2, 3, 4)
set_example = {1, 2, 3, 4}
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Print their types
print("Types:")
print("List:", type(list_example))
print("Tuple:", type(tuple_example))
print("Set:", type(set_example))
print("Dict:", type(dict_example))

# Accessing elements
print("\nAccessing elements:")
print("List element:", list_example[0])
print("Tuple element:", tuple_example[0])
# Sets do not support indexing
# print("Set element:", set_example[0])  # This would raise an error
print("Dict element by key:", dict_example['a'])

# Mutability
print("\nMutability:")
list_example[0] = 10
print("Modified list:", list_example)
# Tuples are immutable
# tuple_example[0] = 10  # This would raise an error
set_example.add(5)
print("Modified set:", set_example)
dict_example['a'] = 10
print("Modified dict:", dict_example)

# Order
print("\nOrder:")
print("List maintains order:", list_example)
print("Tuple maintains order:", tuple_example)
print("Set does not maintain order:", set_example)
print("Dict maintains insertion order (since Python 3.7):", dict_example)

# Duplicate elements
print("\nDuplicates:")
list_example.append(10)
print("List with duplicates:", list_example)
tuple_example = tuple_example + (10,)
print("Tuple with duplicates:", tuple_example)
set_example.add(10)
print("Set without duplicates:", set_example)
dict_example['e'] = 10
print("Dict with unique keys:", dict_example)
