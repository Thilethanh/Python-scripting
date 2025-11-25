
# DATA types in Python

# 1. int - Integer
# whole number (positive, negative, zero)
# Python integers have unlimited precision,
# size grows as the number gets larger

x = 432

# small integer: 28 bytes
# Use: counters, indices, calculations

# -------------
# 2. float 
# number with decimal point, stored using 64-bit IEEE 754 double precision

pi = 3.14159

# size 24 bytes overhead + 8 bytes numeric value ~ 32 bytes
# scientific data, measurements, analog values.


# --------
# 3. bool 
# logical values True or False
# internally an integer subclass

flag = True

# Use: conditions, flags, control logic

# --------
# 4. string
# Immutable text data.
# Characters stored using Unicode (1-4 bytes per char)

name = "Alice"

# 49 bytes base + number of character x (1-4 bytes)
# Use: messages, logs, lables, file paths.

# ----
# 5. list - dynamic array
# Ordered, mutable collection of items
# stores references, not the objects themselves.

nums = [1, 2, 3]

# Empty list ~ 56 bytes
# Each element reference = 8 bytes (64-bit system)
# Use: general-purpose collections, buffers, sequences

# ------
# 6. tuple - Immutable list
# Ordered, immutable sequence
# More memory-efficient than lists.

point = (10, 20)

# 48 bytes + 8 bytes per element
# Use coordinates, fixed configuration, function returns.

# --------
# 7. dict - Dictionary (hash map)
# Key-value mapping. Very fast lookup (hash table)

person = {"name": "Alice", "age": 30}

# Empty dict ~ 72 bytes
# Grows as keys increase
# Each key/value pair adds ~70 - 150 bytes
# Use: setting, structured data, fast lookup tables.

# ----------------
# 8. set - unique unodred items
# Stored unique element, uses hashing like dict (but only keys)'

unique= {1, 2, 3}

# Empty set ~216 bytes
# Each additional element ~70 bytes
# Use: uniqueness, membership testing.

# -------------
# 9. NoneType 
# Represents "No value". Only one instances exist: None

value = None

# Singleton: 16 bytes
# All variable referencing None share sam object
# optional returns, default, placeholders.

# ------
# 10. complex 
# Real + imaginary part, both floats

z = 3 + 4j

# 32 bytes (for object) + 2x8 bytes floats = 48 bytes
# Use: signal processing, AC analysis RF, control theory

# -----
# 11. range - Efficient integer sequence
# Does not store numbers, stores only start, stop and step
r = range(0, 10)

# 48 bytes (independent of number count)
# Use: loops, large ranges without memory cost

# -----
# 12. bytes - Immutable bytes
# Raw binary data

data = b'\x00\xFF'

# 37 bytes base + 1 byte per element
# Use: files, serial data, sockets,

# ----
# 13. bytearray - Mutable bytes
# Same as bytes but modifiable

ba = bytearray(b'ABC')

# Similar to bytes byt slightly more overhead
# 1 byte per element

# ---
# 14. memoryview - Zero-copy slice
# Reference to existing binary data withoutt copying.

mv = memoryview(b"example")

# Very small, 48 bytes
# Does NOT duplicate data
# Use: fast I/O pipelines, slicing buffers.

# ---
# 15. generator
# Produces values one at a time using yield.
# Does NOT store tthe whole sequence

def gen():
    yield 1
    yield 2

# ~112 bytes
# Use almost no extra memory regardless of outputs
# Use: streaming data, measurement loops, large datasets.


