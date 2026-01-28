# PART 1: Context Manager using class
# Build a FileManager class that:
# - Opens a file in __enter__
# - Closes it in __exit__
# - Handles exceptions gracefully

class FileManager:
    def __init__(self,filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello \n")


# PART 2: Context Manager using contextlib
# Build the same thing using @contextmanager decorator
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try: 
        yield f
    finally:
        f.close()

with open_file("test.txt", "a") as f:
    f.write("Hello worlddd!! \n")
    

# PART 3: Generators
# 1. Write a generator that yields fibonacci numbers up to n
def fibo(x):
    a,b = 0,1
    while a<= x:
        yield a
        a, b= b, a+b

print(list(fibo(10)))
for i in fibo(10):
    print(i)


# 2. Write a generator that reads a large file line by line
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        for line in f:
            yield line.strip()
    finally:
        f.close()


for line in open_file("test.txt", 'r'):
    print(line)
    
# 3. Write a generator expression that squares numbers 1-100

generators = (x*x for x in range(1, 101))

for sq in generators:
    print(sq)


