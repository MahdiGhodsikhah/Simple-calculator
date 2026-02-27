# 🐍 Python Simple Calculator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

A sleek and efficient command-line calculator built with Python. This project demonstrates basic arithmetic operations and interactive loop handling.

## 🚀 Features

- **Basic Arithmetic**: Support for addition, subtraction, multiplication, and division.
- **Interactive CLI**: Easy-to-use command-line interface.
- **Continuous Execution**: Perform multiple calculations without restarting the script.
- **Clean Code**: Modular function-based architecture.

## 🛠️ Core Functions

The core logic is implemented in [Simple calculator.py](file:///d:/GitHub/Simple-calculator/Simple%20calculator.py) using specific functions for each operation:

| Function | Symbol | Description |
| :--- | :---: | :--- |
| `add(a, b)` | `+` | Returns the sum of two numbers |
| `minus(a, b)` | `-` | Returns the difference of two numbers |
| `multiply(a, b)` | `*` | Returns the product of two numbers |
| `divide(a, b)` | `/` | Returns the quotient of two numbers |

## 📖 How It Works

The program runs within a `while True` loop to provide a seamless user experience:

1. **Input Stage**: Prompts for the first number, the operator, and the second number.
2. **Calculation**: Maps the operator to the corresponding function using a dictionary (`dic`).
3. **Output**: Displays the result immediately.
4. **Loop Control**: Asks `Do you want to continue? (y/n)`.
   - Pressing **`y`** restarts the process for a new calculation.
   - Any other key gracefully exits the program.

## 💻 Usage

To run the calculator, ensure you have Python installed and execute the following command:

```bash
python "Simple calculator.py"
```

---
*Created with ❤️ for Python enthusiasts.*
