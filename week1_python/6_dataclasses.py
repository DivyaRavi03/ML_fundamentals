# PART 1: Basic dataclass
# Create a Student dataclass with:
# - name: str
# - age: int  
# - gpa: float
# - Create 2 students and compare them with ==


from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age :int
    gpa:float


student_1 = Student('John', 18, 3.7)
student_2 = Student('John', 18, 3.5)

# a = Student.__eq__(student_1, student_2)
# print(a)
print(student_1 == student_2)

# PART 2: Dataclass with defaults and field()
from dataclasses import dataclass, field

# Create a Course dataclass with:
# - name: str
# - code: str
# - students: list[str] = empty list (use field(default_factory=list))
# - max_capacity: int = 30
# - Add a method is_full() -> bool

@dataclass
class Course:
    name: str
    code: str
    students: list[str] = field(default_factory=list)
    max_capacity: int = 30

    def is_full(self)->bool:
        return len(self.students) >= self.max_capacity 
    
c1 = Course("AI", "CS501")
c1.students = ["Alice", "Bob"]
c1.max_capacity = 2
print(c1.is_full())  # True

c2 = Course("ML", "CS502")
print(c2.is_full())  # False (empty list, capacity 30)


# PART 3: Frozen dataclass (immutable)
# Create a Point dataclass that cannot be modified after creation
# Hint: @dataclass(frozen=True)

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

# Test
p1 = Point(3, 5)
print(p1)          
p1.x = 10      

# PART 4: __slots__ example
# Create a SlottedPoint class with __slots__
# Create 1 million points and compare memory usage vs normal class
# Use: import sys; sys.getsizeof(obj)


import sys

# Normal class (uses __dict__)
class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Slotted class (no __dict__, less memory)
class SlottedPoint:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Compare memory usage
normal = NormalPoint(1, 2)
slotted = SlottedPoint(1, 2)

print(f"Normal: {sys.getsizeof(normal)} bytes")
print(f"Normal __dict__: {sys.getsizeof(normal.__dict__)} bytes")
print(f"Slotted: {sys.getsizeof(slotted)} bytes")

import sys

# Create 1 million normal points
normal_points = [NormalPoint(i, i) for i in range(1_000_000)]

# Create 1 million slotted points
slotted_points = [SlottedPoint(i, i) for i in range(1_000_000)]

print(f"Normal list size: {sys.getsizeof(normal_points)} bytes")
print(f"Slotted list size: {sys.getsizeof(slotted_points)} bytes")

# PART 5: Combine both — dataclass with __slots__
# Hint: @dataclass and __slots__ = ['x', 'y'] together

from dataclasses import dataclass
import sys

@dataclass
class SlottedDataPoint:
    __slots__ = ['x', 'y']
    x: float
    y: float

# Usage
point = SlottedDataPoint(3.0, 4.0)
print(point)  # SlottedDataPoint(x=3.0, y=4.0)
print(f"Size: {sys.getsizeof(point)} bytes")

