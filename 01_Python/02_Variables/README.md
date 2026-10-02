# Python Variables

## 1. Overview

Variables are one of the most important foundations of Python programming. They help us store data, reuse it, and perform operations on it.

A variable is essentially a named location in memory that holds a value.

Example:

```python
name = "Nikhil"
age = 21
city = "Maihar"
```

Here:

- `name` stores `"Nikhil"`
- `age` stores `21`
- `city` stores `"Maihar"`

---

## 2. What is a Variable?

A variable is a name that refers to a value stored in memory.

In simple language, a variable gives a value a meaningful name so that the program can use it later.

### Syntax

```python
variable_name = value
```

### Example

```python
student_name = "Nikhil Patel"
student_age = 21
student_height = 5.8
```

This makes code cleaner and easier to understand.

---

## 3. Why Variables Are Important

Variables are important because they allow us to:

1. Store data temporarily during execution
2. Reuse values multiple times
3. Perform calculations on stored values
4. Write cleaner and more readable programs
5. Build dynamic and logical solutions

Without variables, a program would be static and difficult to manage.

---

## 4. How Variables Work in Python

When we assign a value to a variable, Python creates a memory reference to that value.

Example:

```python
age = 21
print(age)
```

Output:

```text
21
```

Conceptually:

```text
age --> 21
```

This means the variable name `age` points to the value `21`.

---

## 5. Creating Variables

A variable is created as soon as a value is assigned to it.

```python
name = "Nikhil"
city = "Maihar"
marks = 90
```

Python does not require a special declaration before assigning values.

Example:

```python
x = 10
```

This is valid Python.

---

## 6. Variable Assignment

The `=` operator is called the assignment operator.

It assigns the value on the right side to the variable on the left side.

```python
name = "Nikhil Patel"
```

This means:

- `name` is the variable name
- `"Nikhil Patel"` is the assigned value

Another example:

```python
result = 10 + 5
```

Now `result` stores `15`.

---

## 7. Reassigning a Variable

A variable can be assigned a new value later.

```python
age = 21
print(age)

age = 22
print(age)
```

Output:

```text
21
22
```

This is a core feature of variables: their values can change.

---

## 8. Variables Can Change Their Value

Python allows us to reuse the same variable name with different values.

```python
value = 10
print(value)

value = 25
print(value)

value = 50
print(value)
```

Output:

```text
10
25
50
```

This is why variables are called variables.

---

## 9. Python is Dynamically Typed

Python is dynamically typed, which means we do not need to explicitly specify the type of a variable while creating it.

```python
x = 10
x = "Nikhil"
x = 5.7
```

Python automatically determines the current data type of the value.

Example:

```python
value = 10
print(value)

value = "Hello"
print(value)
```

Output:

```text
10
Hello
```

---

## 10. Variable Name vs Value

A variable is made of two parts:

- variable name
- value

Example:

```python
name = "Nikhil"
```

Here:

- `name` is the variable name
- `"Nikhil"` is the value

This is important because the variable is just a label or reference pointing to the stored value.

---

## 11. Variable Naming Rules

Python has a few rules for naming variables.

### 11.1 Variable names can contain letters

```python
name = "Nikhil"
```

### 11.2 Variable names can contain numbers

```python
student1 = "Ankit"
```

### 11.3 Variable names cannot start with a number

```python
1student = "Nikhil"   # Invalid
```

### 11.4 Underscore is allowed

```python
student_name = "Nikhil Patel"
```

### 11.5 Spaces are not allowed

```python
student name = "Nikhil"   # Invalid
```

Use:

```python
student_name = "Nikhil"
```

### 11.6 Hyphen is not allowed

```python
student-name = "Nikhil"   # Invalid
```

### 11.7 Variable names are case-sensitive

```python
name = "Nikhil"
Name = "Patel"
```

These are different variables.

### 11.8 Python keywords cannot be used as variable names

```python
class = "Python"   # Invalid
```

`class` is a reserved keyword in Python.

---

## 12. Valid and Invalid Variable Names

### Valid examples

```python
name = "Nikhil"
student_name = "Ankit"
student1 = "Patel"
_marks = 98
total_marks = 500
```

### Invalid examples

```python
1name = "Nikhil"        # starts with a number
student-name = "Ankit"  # hyphen not allowed
student name = "Patel"   # space not allowed
class = "Python"        # keyword not allowed
```

---

## 13. Meaningful Variable Names

Variable names should be clear and descriptive.

### Good examples

```python
student_name = "Nikhil Patel"
total_marks = 450
mobile_number = 9876543210
```

### Bad examples

```python
x = "Nikhil Patel"
a = 450
m = 9876543210
```

Readable names make the code easier to understand.

---

## 14. Python Naming Convention

Python commonly follows `snake_case` naming style.

### Examples

```python
employee_name
total_marks
mobile_number
date_of_birth
```

This is the preferred style in Python programming.

---

## 15. Assigning Different Types of Values

A variable can store different kinds of values.

```python
name = "Nikhil"
age = 21
height = 5.8
is_student = True
```

This shows that Python variables can hold different data types.

---

## 16. Printing Variables

The `print()` function is used to display variable values.

```python
name = "Nikhil Patel"
age = 21

print(name)
print(age)
```

Output:

```text
Nikhil Patel
21
```

---

## 17. Printing Text and Variables Together

```python
name = "Nikhil Patel"
age = 21

print("My name is", name)
print("My age is", age)
```

Output:

```text
My name is Nikhil Patel
My age is 21
```

---

## 18. Using Variables in Calculations

Variables can be used with arithmetic operations.

```python
a = 10
b = 20

sum_result = a + b
print(sum_result)
```

Output:

```text
30
```

Another example:

```python
price = 60
quantity = 3

total = price * quantity
print(total)
```

Output:

```text
180
```

---

## 19. Multiple Assignment

Python allows us to assign multiple values to multiple variables in a single line.

```python
name, age, city = "Nikhil Patel", 21, "Maihar"
print(name)
print(age)
print(city)
```

Output:

```text
Nikhil Patel
21
Maihar
```

---

## 20. Assigning the Same Value to Multiple Variables

```python
a = b = c = 200
print(a)
print(b)
print(c)
```

Output:

```text
200
200
200
```

This assigns the same value to all three variables.

---

## 21. Unpacking Values into Variables

Python can unpack values from a collection into separate variables.

```python
numbers = (20, 30, 40)
x, y, z = numbers

print(x)
print(y)
print(z)
```

Output:

```text
20
30
40
```

This is useful when working with tuples and sequences.

---

## 22. Swapping Variables

Swapping means exchanging values between two variables.

```python
a = 50
b = 100

print("Before swapping:")
print(a, b)

a, b = b, a

print("After swapping:")
print(a, b)
```

Output:

```text
Before swapping:
50 100
After swapping:
100 50
```

Python makes this easy with tuple unpacking.

---

## 23. Checking the Type of a Variable

The `type()` function is used to check the data type of a variable.

```python
name = "Nikhil"
age = 21

print(type(name))
print(type(age))
```

Output:

```text
<class 'str'>
<class 'int'>
```

This helps us understand what kind of value a variable stores.

---

## 24. Variables and Objects in Python

In Python, a variable is not just a box; it is a name that points to an object in memory.

```python
age = 21
```

This can be understood as:

```text
age --> 21
```

If we assign a new value later:

```python
age = 25
```

Now `age` points to `25` instead of `21`.

---

## 25. Multiple Variables Referring to the Same Object

Two variables can point to the same value.

```python
a = 100
b = a

print(a)
print(b)
```

Both variables refer to the same object value `100`.

---

## 26. The id() Function

The `id()` function returns the identity of an object.

```python
a = 100
b = a

print(id(a))
print(id(b))
```

This can help us check whether two variables refer to the same memory object.

---

## 27. Reassignment and Object References

When one variable is reassigned, it does not automatically change another variable unless both refer to the same object.

```python
a = 10
b = a

a = 20

print(a)
print(b)
```

Output:

```text
20
10
```

This demonstrates that reassigning `a` does not change `b`.

---

## 28. Variables and Memory

Variables are stored in memory while the program is executing. Python manages this automatically.

```python
name = "Python"
```

The name `name` refers to a string object containing `Python`.

When assigned another value:

```python
name = "Java"
```

The name now refers to the new object `Java`.

---

## 29. Deleting a Variable

The `del` statement removes a variable name from memory.

```python
age = 21
del age
```

If we try to use the variable afterward, Python raises an error.

```python
print(age)
```

This causes a `NameError`.

---

## 30. Files in This Section

This folder contains the following files:

### 30.1 Variables.py

This file contains practical examples of variables, including:

- variable creation
- reassignment
- arithmetic using variables
- multiple assignment
- same value assignment
- unpacking
- swapping
- type checking

### 30.2 Variables.ipynb

This is the notebook version of the variables lesson. It is useful for interactive learning and visual execution of code.

### 30.3 README.md

This file explains the theory and examples for the variables topic.

### 30.4 Trainer_Notes.pdf

This file contains reference notes from the trainer.

---

## 31. Practice Examples from Variables.py

The practice file includes code such as:

```python
name = "Nikhil Patel"
age = 21
city = "Maihar"
print(name)
print(age)
print(city)
```

```python
num1 = 10
num2 = 20
sum_result = num1 + num2
print("Sum:", sum_result)
```

```python
name, age, city = "Nikhil Patel", 21, "Maihar"
print(name)
print(age)
print(city)
```

```python
a = 50
b = 100
a, b = b, a
print(a, b)
```

```python
name = "Ankit"
age = 21
print(type(name))
print(type(age))
```

These examples are useful for understanding variables in real practice.

---

## 32. Learning Outcome

After completing this topic, the learner should be able to:

1. understand what a variable is
2. assign values correctly
3. use meaningful variable names
4. reassign values when needed
5. perform calculations using variables
6. use multiple assignment and unpacking
7. swap variables efficiently
8. check the type of values
9. understand how Python manages variable references in memory

---

## 33. Conclusion

Variables are the foundation of Python programming. They help us store, reuse, and manipulate data in a clean and structured way.

Without variables, programming would be much more difficult and less flexible. Every future topic in Python depends on understanding variables correctly.

---

## 34. Common Mistakes with Variables

### 34.1 Starting a variable name with a number

```python
1name = "Nikhil"
```

This is invalid.

Correct version:

```python
name1 = "Nikhil"
```

### 34.2 Using spaces in variable names

```python
student name = "Nikhil"
```

This is invalid.

Correct version:

```python
student_name = "Nikhil"
```

### 34.3 Using Python keywords as variable names

```python
class = "Python"
```

This is invalid because `class` is a reserved keyword in Python.

### 34.4 Using an undefined variable

```python
print(name)
```

If `name` is not defined first, Python raises a `NameError`.

### 34.5 Confusing `=` and `==`

- `=` is used for assignment
- `==` is used for comparison

```python
age = 21
print(age == 21)
```

---

## 35. Best Practices for Variables

- Use meaningful and descriptive names
- Follow `snake_case` naming style
- Avoid single-letter names unless necessary
- Do not use Python keywords
- Keep variable names easy to understand
- Use uppercase names for constants by convention

### Good examples

```python
employee_name = "Nikhil Patel"
total_marks = 332
mobile_number = 9876543210
company_name = "ABC"
```

### Avoid

```python
a = "Nikhil Patel"
x = 332
m = 9876543210
```

---

## 36. Quick Reference Examples

### Basic variable

```python
name = "Nikhil Patel"
```

### Multiple variables

```python
name = "Nikhil Patel"
age = 21
city = "Maihar"
```

### Multiple assignment

```python
a, b, c = 10, 20, 30
```

### Same value assigned to multiple variables

```python
a = b = c = 100
```

### Reassignment

```python
age = 21
age = 22
```

### Calculation

```python
price = 100
quantity = 5

total = price * quantity
```

### Swapping

```python
a = 10
b = 20
a, b = b, a
```

### Checking type

```python
value = 100
print(type(value))
```

### Deleting a variable

```python
name = "Nikhil Patel"
del name
```

---

## 37. Final Summary

In this topic, we learned that variables are the basic building blocks of Python programs. They allow us to store values, change them, reuse them, and work with real data in a structured way.

The most important things to remember are:

- variables hold values
- names should be meaningful
- they can be reassigned
- they can store different types
- they are essential for calculations and logic

This topic forms the foundation for all future Python learning.
