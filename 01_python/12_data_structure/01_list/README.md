# Python List

## Introduction

A **list** is a built-in Python data structure used to store multiple values in a single variable.

Lists are:

* Ordered
* Mutable
* Allow duplicate values
* Can store different data types
* Can contain other lists

Example:

```python
numbers = [10, 20, 30, 40]
```

---

# Important Properties of Lists

| Property | List |
| --- | --- |
| Ordered | Yes |
| Mutable | Yes |
| Duplicates | Allowed |
| Indexing | Yes |
| Negative Indexing | Yes |
| Slicing | Yes |
| Different Data Types | Yes |
| Nested Lists | Yes |

---

## List Syntax

```python
list_name = [value1, value2, value3]
```

Example:

```python
numbers = [10, 20, 30, 40]
```

A list can contain different data types:

```python
data = [10, 3.14, "Python", True]
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
numbers = [10, 20, 30]

print(type(numbers))
```

Output:

```text
<class 'list'>
```

---

## len()

The `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

---

## Indexing

Each element in a list has an index.

Python uses **zero-based indexing**.

```python
numbers = [10, 20, 30, 40]
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

Python also supports negative indexing.

```text
Value:           10    20    30    40
Positive Index:   0     1     2     3
Negative Index:  -4    -3    -2    -1
```

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

---

## Updating List Elements

Lists are **mutable**, which means their elements can be changed.

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:

```text
[10, 25, 30]
```

---

## Slicing

Slicing is used to extract a portion of a list.

### Syntax

```python
list[start:stop:step]
```

The `stop` index is not included.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

### Step

```python
print(numbers[::2])
```

Output:

```text
[10, 30, 50]
```

### Reverse a List Using Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

## List Methods

Python provides several built-in methods for lists.

### append()

Adds an element at the end of the list.

```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### insert()

Inserts an element at a specified index.

```python
numbers = [10, 20, 30]
numbers.insert(1, 25)
print(numbers)
```

Output:

```text
[10, 25, 20, 30]
```

### remove()

Removes the first matching value.

```python
numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)
```

Output:

```text
[10, 30, 40]
```

### pop()

Removes the last item from the list and returns it.

```python
numbers = [10, 20, 30]
print(numbers.pop())
print(numbers)
```

Output:

```text
30
[10, 20]
```

### sort()

Sorts the list in ascending order.

```python
numbers = [30, 10, 20]
numbers.sort()
print(numbers)
```

Output:

```text
[10, 20, 30]
```

### reverse()

Reverses the order of the list.

```python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)
```

Output:

```text
[30, 20, 10]
```

---

## Common Example

```python
students = ["Nikhil", "Aman", "Riya"]

print(students[0])
print(len(students))
students.append("Pooja")
print(students)
```

Output:

```text
Nikhil
3
['Nikhil', 'Aman', 'Riya', 'Pooja']
```

---

## Summary

A list is one of the most commonly used data structures in Python. It helps store multiple values together and allows easy modification, indexing, sorting, and slicing.

Lists are ideal for handling collections of data such as:

* Student names
* Marks and scores
* Product prices
* To-do tasks
* Data analysis values

In short, lists are powerful, flexible, and extremely useful in Python programming.

---

## Function Examples

```python
# List functions example
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)

print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[1:3])
```

Output:

```text
[10, 15, 30, 40]
4
10
[15, 30]
```

This example shows common list functions such as `append()`, `insert()`, `remove()`, `len()`, and slicing.
