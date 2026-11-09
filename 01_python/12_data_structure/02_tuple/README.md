# Python Tuple

## Introduction

A **tuple** is an ordered and immutable collection of items in Python. It is similar to a list, but unlike a list, a tuple cannot be changed after creation.

Tuples are:

* Ordered
* Immutable
* Allow duplicate values
* Can store different data types
* Can contain nested tuples

Example:

```python
numbers = (10, 20, 30, 40)
```

---

# Important Properties of Tuples

| Property | Tuple |
| --- | --- |
| Ordered | Yes |
| Immutable | Yes |
| Duplicates | Allowed |
| Indexing | Yes |
| Negative Indexing | Yes |
| Slicing | Yes |
| Different Data Types | Yes |
| Nested Tuples | Yes |

---

## Tuple Syntax

```python
tuple_name = (value1, value2, value3)
```

Example:

```python
numbers = (10, 20, 30, 40)
```

A tuple can also store mixed data types:

```python
data = (10, 3.14, "Python", True)
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
numbers = (10, 20, 30)

print(type(numbers))
```

Output:

```text
<class 'tuple'>
```

---

## len()

The `len()` function returns the number of items in a tuple.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

---

## Indexing

Each element in a tuple has an index.

Python uses **zero-based indexing**.

```python
numbers = (10, 20, 30, 40)
```

```text
Value:    10   20   30   40
Index:     0    1    2    3
```

Example:

```python
print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## Negative Indexing

Python also supports negative indexing in tuples.

```text
Value:           10    20    30    40
Positive Index:   0     1     2     3
Negative Index:  -4    -3    -2    -1
```

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

---

## Updating Tuples

Tuples are **immutable**, so we cannot change an item directly.

```python
numbers = (10, 20, 30)

# numbers[1] = 25   # This will raise an error
```

If we want to change data, we need to create a new tuple.

```python
numbers = (10, 20, 30)
new_numbers = (10, 25, 30)
print(new_numbers)
```

Output:

```text
(10, 25, 30)
```

---

## Slicing

Slicing is used to extract a portion of a tuple.

### Syntax

```python
tuple[start:stop:step]
```

The `stop` index is not included.

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

### Step

```python
print(numbers[::2])
```

Output:

```text
(10, 30, 50)
```

### Reverse a Tuple Using Slicing

```python
print(numbers[::-1])
```

Output:

```text
(50, 40, 30, 20, 10)
```

---

## Tuple Methods

Python provides a few built-in methods for tuples.

### count()

Returns how many times a value appears in the tuple.

```python
numbers = (10, 20, 20, 30)
print(numbers.count(20))
```

Output:

```text
2
```

### index()

Returns the index of the first matching value.

```python
numbers = (10, 20, 30, 40)
print(numbers.index(30))
```

Output:

```text
2
```

---

## Common Example

```python
student = ("Nikhil", 21, "India")

print(student[0])
print(len(student))
print(student.count("Nikhil"))
```

Output:

```text
Nikhil
3
1
```

---

## Summary

A tuple is a useful Python data structure when you want to store fixed values that should not be changed. It is faster and safer than a list in situations where data should remain constant.

Tuples are ideal for:

* Fixed configuration values
* Coordinates or points
* Multiple values that should not change
* Data that must remain constant

In short, tuples are reliable, ordered, and immutable collections in Python.

---

## Function Examples

```python
# Tuple functions example
numbers = (10, 20, 30, 20)

print(numbers.count(20))
print(numbers.index(30))
print(numbers[1:3])
print(len(numbers))
```

Output:

```text
2
2
(20, 30)
4
```

This example shows common tuple functions like `count()`, `index()`, slicing, and `len()`.
