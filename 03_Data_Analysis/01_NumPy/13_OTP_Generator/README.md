# OTP Generator

This notebook demonstrates how to generate a numeric one-time password (OTP)
using Python's cryptographically secure `secrets` module.

## Features

- Generates a six-digit OTP by default, with a configurable length.
- Produces numeric output as a string, so leading zeroes are preserved.
- Rejects non-positive or non-integer lengths.
- Uses a reusable `generate_otp()` function.

## Requirements

- Python 3.x
- Jupyter Notebook or VS Code with the Jupyter extension

No external packages are required.

## Usage

Open [OTP-Generator.ipynb](OTP-Generator.ipynb) and run the Python cell:

```python
import secrets
import string


def generate_otp(length=6):
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be a positive integer")
    return "".join(secrets.choice(string.digits) for _ in range(length))


otp = generate_otp()
print(f"Your OTP is: {otp}")
```

Each run produces a different six-digit string, for example:

```text
Your OTP is: 083741
```

## Custom Length

Pass the desired length to `generate_otp()`:

```python
otp = generate_otp(6)
```

The generator samples from all ten decimal digits (`0` through `9`).

## Note

This demonstrates secure random generation only. A production authentication
flow also needs OTP expiry, retry limits, secure storage, and secure delivery.
