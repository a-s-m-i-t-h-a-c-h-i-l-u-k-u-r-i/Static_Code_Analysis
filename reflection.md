1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest to fix:
- Formatting issues like adding blank lines, removing trailing whitespace, and adding the final newline were trivial mechanical edits
- Removing the unused logging import was a simple deletion
- Renaming functions from camelCase to snake_case was straightforward find-and-replace
- Converting to f-strings required minimal changes

Hardest to fix:
-The mutable default argument (logs=[]) required understanding Python's function default evaluation behavior and how the same list object persists across calls
-The bare except clause required deciding what specific exceptions could occur and how to handle them appropriately
-Deciding how to handle the eval() security vulnerability and whether to replace or remove it entirely

2. Did the static analysis tools report any false positives? If so, describe one example.
The global statement warning in the load_data() function could be considered debatable. While Pylint correctly flagged it as a code smell, the function legitimately needed to modify the module-level stock_data dictionary. This is more of a design suggestion than a true error. I eventually refactored it to return data instead, which improved the design, but the original implementation wasn't technically wrong for a simple script.


3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.

Local Development:
Configure IDE integration for real-time warnings
Set up pre-commit hooks to run flake8 before each commit
Create a simple script or Makefile command to run all three tools together
Add configuration files (.pylintrc, .flake8) to standardize rules

CI/CD Pipeline:
Add static analysis as a required stage in GitHub Actions or GitLab CI
Configure builds to fail on high-severity Bandit issues
Set minimum Pylint score thresholds (e.g., 8.0/10)
Use differential analysis to only flag new issues in pull requests
Generate and archive reports as CI artifacts

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- Security: Removing eval() eliminated a critical code injection vulnerability. Adding specific exception handling prevents catching system exits and keyboard interrupts.
- Robustness: Using context managers ensures files close properly even with exceptions. Fixing the mutable default prevents subtle bugs where data accumulates across function calls. Adding file encoding prevents cross-platform compatibility issues.
- Readability: Adding docstrings made every function self-documenting. Snake_case naming follows Python conventions. F-strings are cleaner than concatenation. Proper spacing creates clear visual structure.
- Maintainability: The code went from 4.80/10 to 10.00/10 on Pylint, eliminating all style violations and warnings. It now follows PEP 8 standards, making it consistent with professional Python code.