Inventory Management System - Static Analysis Lab
Project Overview
A simple inventory management system developed for a static analysis lab exercise. The goal was to identify and fix code quality, security, and style issues using Python static analysis tools.
Tools Used

Pylint - Code quality and style checker
Flake8 - PEP 8 style enforcer
Bandit - Security vulnerability scanner

Project Structure
.
├── inventory_system.py      # Main application code
├── pylint_report.txt        # Pylint analysis report
├── flake8_report.txt        # Flake8 analysis report
├── bandit_report.txt        # Bandit security report
├── reflection.md            # Personal reflection
└── README.md               # This file
Installation
bash# Install static analysis tools
pip install pylint flake8 bandit

# Verify installations
pylint --version
flake8 --version
bandit --version
Running Static Analysis
bash# Generate reports
pylint inventory_system.py > pylint_report.txt 2>&1 || true
flake8 inventory_system.py > flake8_report.txt 2>&1 || true
bandit -r inventory_system.py > bandit_report.txt 2>&1 || true

# Or run individually
pylint inventory_system.py
flake8 inventory_system.py
bandit -r inventory_system.py
Issues Fixed
Total: 18 Distinct Issues
Critical (1)

Removed eval() usage - code injection vulnerability

High Priority (2)

Fixed mutable default argument bug
Replaced bare except with specific exception handling

Medium Priority (5)

Added UTF-8 encoding to file operations
Implemented context managers for file handling
Refactored to eliminate global statement usage

Low Priority (10)

Removed unused imports
Renamed functions to snake_case (7 functions)
Added comprehensive docstrings
Converted to f-strings
Fixed PEP 8 spacing issues
Removed trailing whitespace
Split long lines
Added final newline

Tool           Before                      After
Pylint        4.80/10 (27 issues)         10.00/10 (0 issues)
Flake8         11violations                0 violations
Bandit         2security issues            0 issues
Usage Example
pythonfrom inventory_system import *

# Load inventory
stock_data = load_data("inventory.json")

# Add items
add_item("apple", 50)
add_item("banana", 30)

# Check quantity
qty = get_qty("apple")

# Check low stock
check_low_items(threshold=25)

# Display inventory
print_data()

# Save changes
save_data("inventory.json")
Key Functions

add_item(item, qty, logs) - Add or update item
remove_item(item) - Remove item from inventory
get_qty(item) - Get quantity of item
load_data(filename) - Load inventory from JSON
save_data(filename) - Save inventory to JSON
print_data() - Display all items
check_low_items(threshold) - Alert for low stock

Learning Outcomes

Understanding static analysis benefits
Identifying security vulnerabilities
Following PEP 8 and Python best practices
Integrating linters into development workflow
Writing production-ready code

References

Pylint Documentation
Flake8 Documentation
Bandit Documentation
PEP 8 Style Guide

Summary

Fixed 18 distinct issues across all severity levels
Achieved perfect scores on all three static analysis tools
Eliminated critical security vulnerability
Code is now production-ready following Python best practices
