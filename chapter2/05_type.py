#type() function and type casting

# type() function
print("\nType of various data types:")
print("----------------------------------")
print("type(5) - class name: ", type(5))  # <class 'int'>
print("type(5).__name__  - name of the type: ", type(5).__name__)
print("type(5.0) - class name: ", type(5.0))  # <class 'float'>
print("type(5.o).__name__ - name of the type: ", type(5.0).__name__)
print("type('Hello') - class name:", type("Hello"))  # <class 'str'>
print("type('Hello').__name__ - name of the type:", type("Hello").__name__)
print("type(True) - class name:", type(True))  # <class 'bool'>
print("type(True).__name__ - name of the type:", type(True).__name__)
print("type(None) - class name:", type(None))  # <class 'NoneType'>
print("type(None).__name__ - name of the type:", type(None).__name__)
print("type([1, 2, 3]) - class name:", type([1, 2, 3]))  # <class 'list'>
print("type([1, 2, 3]).__name__ - name of the type:", type([1, 2, 3]).__name__)
print("type((1, 2, 3)) - class name:", type((1, 2, 3)))  # <class 'tuple'>
print("type((1, 2, 3)).__name__ - name of the type:", type((1, 2, 3)).__name__)
print("type({'name': 'Aish', 'age': 25}) - class name:", type({"name": "Aish", "age": 25}))  # <class 'dict'>
print("type({'name': 'Aish', 'age': 25}).__name__ - name of the type:", type({"name": "Aish", "age": 25}).__name__)


# type casting
print("\nType casting examples:")
print("----------------------------------")
# int to float
x = 5
y = float(x)
print(y)  # 5.0

# float to int
x = 5.7
y = int(x)
print(y)  # 5

# str to int
x = "10"
y = int(x)
print(y)  # 10

# str to float
x = "10.5"
y = float(x)
print(y)  # 10.5

# int to str
x = 10
y = str(x)
print(y)  # '10'

# float to str
x = 10.5
y = str(x)
print(y)  # '10.5'

# bool to int
x = True
y = int(x)
print(y)  # 1

# bool to str
x = False
y = str(x)
print(y)  # 'False'

# None to str
x = None
y = str(x)
print(y)  # 'None'

# None to int (will raise an error)
# x = None
# y = int(x)  # TypeError: int() argument must be a string or a number, not 'NoneType'

# None to float (will raise an error)
# x = None
# y = float(x)  # TypeError: float() argument must be a string or a number, not 'NoneType'

# None to bool
x = None
y = bool(x)
print(y)  # False

# None to list (will raise an error)
# x = None
# y = list(x)  # TypeError: 'NoneType' object is not iterable

# None to tuple (will raise an error)
# x = None
# y = tuple(x)  # TypeError: 'NoneType' object is not iterable

# None to dict (will raise an error)
# x = None
# y = dict(x)  # TypeError: 'NoneType' object is not iterable

# None to set (will raise an error)
# x = None
# y = set(x)  # TypeError: 'NoneType' object is not iterable

# None to frozenset (will raise an error)
# x = None
# y = frozenset(x)  # TypeError: 'NoneType' object is not iterable

# None to bytes (will raise an error)
# x = None
# y = bytes(x)  # TypeError: 'NoneType' object cannot be interpreted as an integer

# None to bytearray (will raise an error)
# x = None
# y = bytearray(x)  # TypeError: 'NoneType' object cannot be interpreted as an integer

# None to memoryview (will raise an error)
# x = None
# y = memoryview(x)  # TypeError: 'NoneType' object is not iterable

# None to complex (will raise an error)
# x = None
# y = complex(x)  # TypeError: complex() first argument must be a string or a number, not 'NoneType'

# None to range (will raise an error)
# x = None
# y = range(x)  # TypeError: 'NoneType' object cannot be interpreted as an integer

# None to slice (will raise an error)
# x = None
# y = slice(x)  # TypeError: 'NoneType' object cannot be interpreted as an integer