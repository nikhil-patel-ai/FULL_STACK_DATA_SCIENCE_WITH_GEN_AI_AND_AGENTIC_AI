# Python Set

## Introduction

A **set** is an unordered collection of unique items in Python. It is used to store values without duplicates.

Sets are:

* Unordered
* Mutable
* Do not allow duplicate values
* Do not support indexing
* Can store different data types

Example:

```python
numbers = {10, 20, 30, 40}
```

---

# Important Properties of Sets

| Property | Set |
| --- | --- |
| Ordered | No |
| Mutable | Yes |
| Duplicates | Not Allowed |
| Indexing | No |
| Slicing | No |
| Different Data Types | Yes |
| Unique Values | Yes |

---

## Set Syntax

```python
set_name = {value1, value2, value3}
```

Example:

```python
numbers = {10, 20, 30, 40}
```

A set can contain different data types:

```python
data = {10, 3.14, "Python", True}
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
numbers = {10, 20, 30}

print(type(numbers))
```

Output:

```text
<class 'set'>
```

---

## len()

The `len()` function returns the number of items in a set.

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

---

## Adding Elements

We can add items to a set using `add()`.

```python
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

## Removing Elements

We can remove items using `remove()` or `discard()`.

```python
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)
```

Output:

```text
{10, 30}
```

---

## Duplicate Values

Sets automatically remove duplicates.

```python
numbers = {10, 20, 10, 30, 20}
print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

## Set Operations

Sets support mathematical operations such as union and intersection.

### Union

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5}
```

### Intersection

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)
```

Output:

```text
{3}
```

### Difference

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)
```

Output:

```text
{1, 2}
```

---

## Common Example

```python
students = {"Nikhil", "Aman", "Riya", "Nikhil"}
print(students)
```

Output:

```text
{'Riya', 'Nikhil', 'Aman'}
```

The duplicate name `Nikhil` is removed automatically.

---

## Summary

A set is a powerful Python data structure used to store unique values. It is especially useful when we want to remove duplicates or perform mathematical operations on collections.

Sets are ideal for:

* Removing duplicate values
* Checking membership quickly
* Performing set operations
* Managing unique collections of data

In short, sets are useful for uniqueness and fast membership checks in Python.

---

## Function Examples

```python
# Set functions example
numbers = {10, 20, 30, 20}
numbers.add(40)
numbers.remove(20)

A = {1, 2, 3}
B = {3, 4, 5}

print(numbers)
print(len(numbers))
print(30 in numbers)
print(A | B)
print(A & B)
```

Output:

```text
{10, 30, 40}
3
True
{1, 2, 3, 4, 5}
{3}
```

This example shows common set operations such as `add()`, `remove()`, membership testing, union, and intersection.
