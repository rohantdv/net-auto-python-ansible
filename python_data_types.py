# DATA TYPES
#
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# List is a collection which is ordered and changeable. Allows
# duplicate members

X = 5
print(type(X))

# STRING

first_char = "Hello, World!" [10]
print(first_char)

first_char = "Hello, World!" [0:10]
print(first_char)

lowercase = "Hello, World!".lower()
print(lowercase)


upercase = "Hello, World!".upper()
print(upercase)


capitalize = "Hello, World!".capitalize()
print(capitalize)

title = "Hello, World!".title()
print(title)

strip = "         Hello, World!".strip()
print(strip)

lstrip = "         Hello, World!".lstrip()
print(lstrip)

rstrip = "         Hello, World!***    **   *   ".rstrip()
print(rstrip)

replace = "Hello, World!".replace("World","python")
print(replace)

split = "Hello, World!".split(" ")
print(split)

join = "".join(['Hello,', 'World!'])
print(join)

index = "Hello, World!".find("World")   #find("Gold")
print(index)

starts_with_hello = "Hello, World!".startswith("Hello")
print(starts_with_hello)

ends_with_world = "Hello, World!".endswith("World!")
print(ends_with_world)

count_of_l = "Hello, World!".count("o")
print(count_of_l)

formatted = "Hello, {}!".format("Jay")
print(formatted)







# LIST

xyz = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(xyz)

xyz = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(len(xyz))

list = ["abc",34,True,40,"male"]

xyz = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(type(xyz))

xyz = ["1.1.1.1","2.2.2.2","3.3.3.3"]
xyz[1] = "192.168.1.1"
print(xyz)


xyz123 = ["1.1.1.1", "2.2.2.2", '3.3.3.3']
print(xyz123)

xyz123 = {"1.1.1.1", "2.2.2.2", '3.3.3.3'}
print(xyz123)


# NUMBERS

x = 1 #integer
y = 2.8 #float
z = 1j #complex

numbers = [1,2,3,4]
numbers.append(5)
print(numbers)

numbers = [1,2,3,4]
numbers.extend([5,6,7])
print(numbers)

numbers = [1,2,3,4,10]
numbers.insert(9,11)
print(numbers)

numbers = [1,2,3,4,10]
numbers.remove(1)
print(numbers)

numbers = [1,2,3,4,10]
numbers.pop(4)
print(numbers)


numbers = [1,2,3,4,10]
numbers.clear()
print(numbers)

numbers = [1,2,3,4,10]
index = numbers.index(2)
print(index)


numbers = [1,2,3,4,3,10]
count = numbers.count(3)
print(count)

numbers = [3,4,1,6,8,9,7]
numbers.sort()
print(numbers)

numbers = [1, 3, 4, 6, 7, 8, 9]
numbers.reverse()
print(numbers)