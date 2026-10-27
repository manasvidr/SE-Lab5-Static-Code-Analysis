# Reflection

The provided three-page `Lab 5: Static Code Analysis` PDF asks students to answer four reflection questions but does not show the actual question text. I am not inventing question wording. Please insert the exact four questions from the instructor's full handout here and answer each one before submitting.

Notes grounded in this project that may help with those answers:

- Static analysis inspects source code for potential quality, style, and security issues before execution.
- Parameterized SQL passes values separately from SQL syntax, reducing SQL injection risk.
- Evaluating arbitrary strings with `eval` can execute code; the revised `penalty` function accepts numbers and uses arithmetic.
- Mutable default arguments can share state across calls; using `None` and creating a new list avoids that behavior.
- Regression tests help check that the refactored program still supports adding dues, collecting payments, computing a fee, and listing unpaid dues.
