# Static Analysis Issue Log — Society Dues Ledger

The line numbers below refer to `society_dues_before.py`, which preserves the course-assigned starter. Findings are based on direct source review; exact tool messages and line numbers must be aligned with actual Pylint, Bandit, and Flake8 outputs after those tools run.

| Issue | Type / likely tool | Starter line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Arbitrary expression execution with `eval` | Security / Bandit | 22 | `penalty` evaluates an arbitrary Python expression supplied as a string. | Replace it with numeric inputs and ordinary arithmetic. |
| SQL query string interpolation | Security review | 11 | `addDue` interpolates values directly into SQL text. | Use placeholders and pass values separately. |
| Mutable default argument | Code quality / Pylint | 10 | `history=[]` is shared by calls that omit the argument. | Use `None` and initialize a fresh list per call. |
| Hard-coded password-like constant | Security review / unused constant | 5 | `TREASURER_PASSWORD` is embedded in source and not used. | Remove the unused credential-like constant. |
| Unnecessary `None` comparison | Code quality / Pylint | 29 | `fetchall()` returns a list; comparing it to `None` is unnecessary. | Return the transformed list directly. |
| Non-PEP 8 names and formatting | Style / Pylint / Flake8 | multiple | CamelCase names, insufficient blank lines, and long lines reduce consistency. | Use snake_case and standard formatting. |
| Code runs when imported | Maintainability | 40 | Unconditional `main()` executes the demonstration on import. | Add an `if __name__ == "__main__":` guard. |

## Verification status

- Both original and refactored demonstration scripts were executed successfully.
- Seven regression tests passed for the refactored program.
- Pylint, Bandit, and Flake8 could not be installed in the current runtime because the package index could not be resolved. No tool output or scores are fabricated. Use the commands in `README.md` in an environment with package-index access to generate the reports and update this log with exact findings.
