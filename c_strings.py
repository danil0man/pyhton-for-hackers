"""
String formatting
"""

# Double quotes or single quote
my_string: str = "I am a string"
my_other_string: str = "I am a string too!"

# Triple quotes, multiline strings, docstring, function docstring
multiline: str = """
This is a multiline string,
it span in multiple lines
for long strings and poems
"""

# Escaping characters
escape_double_quotes: str = 'I"m a string'
escape_single_quotes: str = "I'm a string"

# Without escaping
no_escape_quote: str = 'I"am a string'

# Other escape characters
new_line: str = "I am in first line\nI am in second line\n"
print(new_line)

backslash: str = "If I need a backlash \\ I need to escape it twice"
print(backslash)

tab: str = "\t I start with a tab"
print(tab)

in_hex: str = "\x41\x42\x43"
print(in_hex)

# Repeating
many_a: str = "a" * 10
print(many_a)

# length of a string
print(len(many_a))

# substring in string
long_message: str = "This is a very long message"

print("in" in long_message)
print("is" in long_message)

# some string methods

# start with
print(long_message.startswith("I"))
print(long_message.startswith("This"))

# index
print(long_message.index("very"))

# upper and lower
print(my_string.upper())
print(my_string.lower())

# strip
messy_string: str = "   Messy string!   "
print(messy_string.strip())

# replace
print(messy_string.replace("!", "?"))

# split to list
string_list: str = "This is a string of words"
separate_by_comma: str = "I want, to split, by commas"
print(string_list.split())
print(separate_by_comma.split(","))

# encode string


# chained methods
chained_methods: str = "   I need to do multiple things!   "
print(chained_methods.replace("I", "You").strip().upper())
