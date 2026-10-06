# PLP Python Week 6 Assignment

## File Descriptions
- **safe_tools.py**: Contains functions using `try/except` blocks to handle runtime errors like division by zero, invalid number conversions, and missing dictionary keys safely.
- **unbreakable.py**: Demonstrates robust execution by running safe functions on valid and edge-case inputs without crashing.

## Question Answer
**Why can the `if` check not catch `abc` on its own?**
An `if` conditional check cannot anticipate the runtime exceptions thrown by functions like `int()` when given invalid data types. A `try/except` block is required to catch the actual `ValueError` raised at runtime when Python tries to convert a non-numeric string like `"abc"` into an integer.