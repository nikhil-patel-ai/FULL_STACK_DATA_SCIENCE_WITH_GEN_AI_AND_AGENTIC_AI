# Python Dictionary

## Introduction

A **dictionary** is a collection of key-value pairs in Python. Each key is unique and is used to access its corresponding value.

Dictionaries are:

* Ordered (in Python 3.7+)
* Mutable
* Key-value based
* Keys must be unique
* Can store different data types

Example:

```python
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}
```

---

# Important Properties of Dictionaries

| Property | Dictionary |
| --- | --- |
| Ordered | Yes |
| Mutable | Yes |
| Key-value pairs | Yes |
| Duplicate Keys | Not Allowed |
| Indexing | By Key |
| Different Data Types | Yes |
| Nested Dictionaries | Yes |

---

## Dictionary Syntax

```python
dict_name = {"key1": value1, "key2": value2}
```

Example:

```python
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
student = {"name": "Nikhil", "age": 21}

print(type(student))
```

Output:

```text
<class 'dict'>
```

---

## len()

The `len()` function returns the number of key-value pairs in the dictionary.

```python
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}

print(len(student))
```

Output:

```text
3
```

---

## Accessing Values

Values are accessed using their keys.

```python
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}

print(student["name"])
print(student["age"])
```

Output:

```text
Nikhil
21
```

---

## Adding and Updating Values

We can add new key-value pairs or update existing ones.

```python
student = {"name": "Nikhil", "age": 21}

student["city"] = "Maihar"
student["age"] = 22

print(student)
```

Output:

```text
{'name': 'Nikhil', 'age': 22, 'city': 'Maihar'}
```

---

## Removing Values

We can remove values using `pop()` or `del`.

```python
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}

student.pop("city")
print(student)
```

Output:

```text
{'name': 'Nikhil', 'age': 21}
```

---

## Dictionary Methods

### keys()

Returns all keys.

```python
student = {"name": "Nikhil", "age": 21}
print(student.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

### values()

Returns all values.

```python
student = {"name": "Nikhil", "age": 21}
print(student.values())
```

Output:

```text
dict_values(['Nikhil', 21])
```

### items()

Returns key-value pairs.

```python
student = {"name": "Nikhil", "age": 21}
print(student.items())
```

Output:

```text
dict_items([('name', 'Nikhil'), ('age', 21)])
```

---

## Common Example

```python
student = {
    "name": "Nikhil",
    "age": 21,
    "subjects": ["Python", "SQL", "AI"]
}

print(student["name"])
print(student["subjects"][0])
```

Output:

```text
Nikhil
Python
```

---

## Summary

A dictionary is a highly useful Python data structure for storing data in key-value form. It makes it easy to organize and access information by meaningful names instead of numeric indexes.

Dictionaries are ideal for:

* Storing user information
* Managing records
* Building JSON-like data structures
* Mapping names to values

In short, dictionaries are one of the most important and widely used data structures in Python.

---

## Function Examples

```python
# Dictionary functions example
student = {"name": "Nikhil", "age": 21, "city": "Maihar"}

student["course"] = "Python"
student["age"] = 22
student.pop("city")

print(student)
print(student["name"])
print(student.keys())
print(student.values())
print(len(student))
```

Output:

```text
{'name': 'Nikhil', 'age': 22, 'course': 'Python'}
Nikhil
dict_keys(['name', 'age', 'course'])
dict_values(['Nikhil', 22, 'Python'])
3
```

This example shows common dictionary operations such as adding keys, updating values, `pop()`, `keys()`, `values()`, and `len()`.
