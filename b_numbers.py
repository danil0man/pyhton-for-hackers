"""
Numbers
"""
# Integers
number_1: int = 45
number_2: int = -49

# Floats
number_3: float = 3.0
number_4: float = 2.5763

# Complex
number_5: complex = 3.14j

# hex number
number_6: int = 0xA

# octal
number_7: int = 0o10

# Possible to use together
print(number_1 + number_3 + number_7)
print(number_2 * number_4 + number_6)

### Some number methods

# Absolute
print(abs(4))
print(abs(-4))

# rounding
print(round(8.4))
print(round(8.7))

# binary and hex representation
print(bin(10))
print(hex(10))

### for more methods use the Math module
