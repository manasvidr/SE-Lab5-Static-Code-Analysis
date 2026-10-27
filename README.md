# CS262 Lab 5 — Static Code Analysis: Society Dues Ledger

**Student repository:** https://github.com/manasvidr/SE-Lab5-Static-Code-Analysis  
**Assigned source:** https://github.com/SETAPESU26/L5_17_society_dues  
**Assigned file:** `society_dues.py`

## Project files

- `society_dues_before.py` preserves the assigned source for baseline analysis.
- `society_dues.py` is the refactored program.
- `issues.md` records reviewed defects and intended fixes.
- `tests/test_society_dues.py` contains regression tests for the refactored program.
- `reports/` is the destination for before/after Pylint, Bandit, and Flake8 reports.
- `reflection.md` notes the reflection-question wording gap in the supplied handout.

## Run the program and tests

```bash
python society_dues_before.py
python society_dues.py
python -m unittest discover -s tests -v
```

## Install static-analysis tools

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pylint bandit flake8
```

## Capture baseline reports

```bash
pylint society_dues_before.py > reports/pylint_before.txt 2>&1
bandit -r society_dues_before.py > reports/bandit_before.txt 2>&1
flake8 society_dues_before.py > reports/flake8_before.txt 2>&1
```

## Capture final reports

```bash
pylint society_dues.py > reports/pylint_after.txt 2>&1
bandit -r society_dues.py > reports/bandit_after.txt 2>&1
flake8 society_dues.py > reports/flake8_after.txt 2>&1
```

The uploaded handout asks for all Bandit findings and Flake8 formatting issues to be addressed, and a final Pylint score above 9.5. Record actual output; do not claim the target is met until the tools run successfully.

## Reflection questions

The supplied three-page PDF references four reflection questions but does not include their wording. `reflection.md` identifies this gap instead of inventing questions. Add the exact questions from your instructor's full handout if they were provided separately.
