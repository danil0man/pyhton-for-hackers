"""
Variables and Data Types
"""
### Variables

# string variable
name: str = "Danny"  # str = text

# integer variable
name_length: int = 5  # int = integer numbers

# typeof
print(type(name))
print(type(name_length))

# type conversion
change_to_int: int = int("4")
change_tp_str: str = str(4)

# Case sensitive
lower: int = 4
Lower: int = 5
print(lower, Lower)

### Other Data Types
pi: float = 3.14  # float = decimals and floating point numbers

name_list: list = ["Marc", "Rune", "Hugo"]  # list = arrays

coordinate_tuple: tuple = (3, 4, 7)  # tuple = immutable list

person_dictionary: dict = {"name": "Danny", "age": 36}  # dict = key/ value pairs

is_married: bool = True  # bool = true or false

number_range: range = range(10)  # range, from one number to another
print(number_range)

name_bytes: bytes = b"Danny"
print(name_bytes)

# Multiple assignment
other_name, other_name_length = "Soc", 3

# Unpack a list
name1, name2, name3 = name_list
print(name1, name2, name3)

### Other Data Types
# set = collection immutable
# Classes -> Custom Types
# Modules
# None = The absent of value
