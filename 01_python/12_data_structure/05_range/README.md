# Python Range

## Introduction

A **range** is a built-in Python sequence used to generate a sequence of numbers. It is often used in loops and iteration.

Range is:

* Immutable
* Sequence-based
* Commonly used in `for` loops
* Memory efficient

Example:

```python
numbers = range(1, 6)
print(list(numbers))
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

# Important Properties of Range

| Property | Range |
| --- | --- |
| Ordered | Yes |
| Immutable | Yes |
| Duplicate Values | No |
| Indexing | Yes |
| Slicing | Yes |
| Memory Efficient | Yes |

---

## Range Syntax

```python
range(start, stop, step)
```

### Parameters

* `start` - beginning value (included)
* `stop` - ending value (excluded)
* `step` - difference between numbers (default is 1)

Example:

```python
numbers = range(2, 10, 2)
print(list(numbers))
```

Output:

```text
[2, 4, 6, 8]
```

---

## type()

The `type()` function is used to check the data type of an object.

```python
numbers = range(1, 6)

print(type(numbers))
```

Output:

```text
<class 'range'>
```

---

## len()

The `len()` function returns the number of elements in the range.

```python
numbers = range(1, 10, 2)
print(len(numbers))
```

Output:

```text
5
```

---

## Indexing

Range supports indexing like a list.

```python
numbers = range(10, 20)

print(numbers[0])
print(numbers[3])
```

Output:

```text
10
13
```

---

## Slicing

Range objects can also be sliced.

```python
numbers = range(1, 11)
print(numbers[2:8])
```

Output:

```text
range(3, 9)
```

To display values clearly, convert it to a list:

```python
print(list(numbers[2:8]))
```

Output:

```text
[3, 4, 5, 6, 7, 8]
```

---

## Using Range in Loops

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## Common Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Summary

The `range` object is a simple and memory-efficient way to generate a sequence of numbers. It is especially useful in loops, counting operations, and repetitive tasks.

Range is ideal for:

* Loops
* Number generation
* Iteration control
* Efficient sequence creation

In short, `range` helps you generate numeric sequences in a compact and efficient way.

---

## Function Examples

```python
# Range functions example
numbers = range(1, 11, 2)

print(list(numbers))
print(len(numbers))
print(numbers[0])
print(numbers[2])

for i in range(1, 6):
    print(i)
```

Output:

```text
[1, 3, 5, 7, 9]
5
1
5
1
2
3
4
5
```

This example shows how `range` is used for sequence generation, indexing, length checking, and loops.
