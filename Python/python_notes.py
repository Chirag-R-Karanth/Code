# Python Quick Reference Notes

## Basic Syntax

### Variables & Types
```python
# Dynamic typing
name = "Alice"
age = 25
height = 5.8
is_student = True

# Type hints (Python 3.5+)
name: str = "Alice"
age: int = 25

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0
```

### Strings
```python
# String methods
text = "hello world"
text.upper()          # "HELLO WORLD"
text.capitalize()     # "Hello world"
text.split()          # ["hello", "world"]
text.replace("h", "H") # "Hello world"

# String formatting
name = "Alice"
age = 25
f"My name is {name} and I'm {age}"           # f-strings (Python 3.6+)
"My name is {} and I'm {}".format(name, age) # .format()
"My name is %s and I'm %d" % (name, age)     # old style

# Multi-line strings
text = """
This is a
multi-line string
"""
```

## Data Structures

### Lists
```python
# Creation and access
fruits = ["apple", "banana", "cherry"]
fruits[0]        # "apple"
fruits[-1]       # "cherry" (last item)
fruits[1:3]      # ["banana", "cherry"] (slicing)

# Methods
fruits.append("date")        # Add to end
fruits.insert(1, "avocado")  # Insert at index
fruits.remove("banana")      # Remove by value
fruits.pop()                 # Remove and return last
fruits.sort()                # Sort in place
len(fruits)                  # Length

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dictionaries
```python
# Creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Access
person["name"]           # "Alice"
person.get("name")       # "Alice"
person.get("job", "N/A") # "N/A" (default if not found)

# Methods
person.keys()            # dict_keys(['name', 'age', 'city'])
person.values()          # dict_values(['Alice', 25, 'NYC'])
person.items()           # dict_items([('name', 'Alice'), ...])

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

### Sets
```python
# Creation
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates an empty dict

# Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1 | set2        # Union: {1, 2, 3, 4, 5}
set1 & set2        # Intersection: {3}
set1 - set2        # Difference: {1, 2}
```

### Tuples
```python
# Immutable sequences
coordinates = (10, 20)
x, y = coordinates  # Unpacking

# Single element tuple (note the comma)
single = (1,)
```

## Control Flow

### Conditionals
```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Ternary operator
result = "Even" if x % 2 == 0 else "Odd"
```

### Loops
```python
# For loop
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for item in [1, 2, 3]:
    print(item)

# Enumerate (index and value)
for idx, value in enumerate(['a', 'b', 'c']):
    print(idx, value)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip to next iteration
    if i == 7:
        break     # Exit loop
    print(i)
```

## Functions

### Basic Functions
```python
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# Variable arguments
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda (anonymous function)
square = lambda x: x ** 2
add = lambda a, b: a + b
```

## Object-Oriented Programming

### Classes
```python
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 2

# Usage
dog = Dog("Buddy", 3)
print(dog.bark())
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
```

## File Handling

```python
# Reading
with open("file.txt", "r") as f:
    content = f.read()        # Read entire file
    lines = f.readlines()     # Read as list of lines
    for line in f:            # Iterate line by line
        print(line.strip())

# Writing
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Appending
with open("file.txt", "a") as f:
    f.write("New line\n")

# JSON
import json

# Write JSON
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors")
finally:
    print("Always executes")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

## Common Modules

### datetime
```python
from datetime import datetime, timedelta

now = datetime.now()
today = datetime.today()
specific = datetime(2024, 12, 25, 10, 30)

# Formatting
now.strftime("%Y-%m-%d %H:%M:%S")  # "2024-11-27 14:35:14"

# Arithmetic
tomorrow = now + timedelta(days=1)
```

### os and pathlib
```python
import os
from pathlib import Path

# os module
os.getcwd()                    # Current directory
os.listdir(".")                # List files
os.path.exists("file.txt")     # Check if exists
os.path.join("dir", "file")    # Join paths

# pathlib (modern approach)
path = Path("dir/file.txt")
path.exists()                  # Check if exists
path.is_file()                 # Is it a file?
path.parent                    # Parent directory
path.name                      # File name
path.suffix                    # Extension
```

### collections
```python
from collections import Counter, defaultdict, deque

# Counter
words = ["apple", "banana", "apple", "cherry"]
count = Counter(words)  # Counter({'apple': 2, 'banana': 1, ...})

# defaultdict
dd = defaultdict(list)
dd["key"].append(1)  # No KeyError

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
```

## List Comprehensions & Generators

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[i+j for j in range(3)] for i in range(3)]

# Generator expression (memory efficient)
squares_gen = (x**2 for x in range(10))

# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
```

## Decorators

```python
# Simple decorator
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

## Important Tips

### PEP 8 Style Guide
- Use 4 spaces for indentation
- Max line length: 79 characters
- Use snake_case for functions/variables
- Use PascalCase for class names
- Use UPPER_CASE for constants

### Common Pitfalls
```python
# Mutable default arguments (BAD)
def add_item(item, items=[]):  # Don't do this!
    items.append(item)
    return items

# Correct way
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()       # Changes to nested lists affect both
deep = copy.deepcopy(original)  # Fully independent copy
```

### Useful Built-in Functions
```python
# Commonly used
len([1, 2, 3])              # Length
sum([1, 2, 3])              # Sum
max([1, 2, 3])              # Maximum
min([1, 2, 3])              # Minimum
sorted([3, 1, 2])           # Return sorted list
reversed([1, 2, 3])         # Return reversed iterator
enumerate([10, 20, 30])     # Index and value pairs
zip([1, 2], ['a', 'b'])     # Combine iterables
all([True, True, False])    # All truthy?
any([False, False, True])   # Any truthy?
```

### Virtual Environments
```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Install packages
pip install package_name
pip install -r requirements.txt

# Save dependencies
pip freeze > requirements.txt

# Deactivate
deactivate
```
