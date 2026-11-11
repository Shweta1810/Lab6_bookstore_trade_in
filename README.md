# Lab 6 – Bookstore Trade-In

## Objective
The objective of this lab is to perform code coverage and branch coverage testing on a Python-based Bookstore Trade-In system.

## Project Description
The Bookstore Trade-In system evaluates used books based on their format, condition, missing pages, and counterfeit status. It calculates the trade-in payout and determines whether the transaction should be completed or rejected.

The project also includes a scanner calibration module that checks scanner error rates and determines whether recalibration is required.

## Modules Tested

### 1. Bookstore Trade-In
- Book format validation.
- Book condition evaluation.
- Missing pages validation.
- Counterfeit book detection.
- Store credit bonus calculation.
- Transaction and audit status validation.

### 2. Scanner Calibration
- Empty scanner data validation.
- Scanner error rate checking.
- Consecutive error detection.
- Scanner recalibration status.

## Technologies Used
- Python
- Pytest
- Pytest-Cov
- Coverage.py

## How to Run the Project

Install the required packages:

```bash
python -m pip install pytest pytest-cov coverage
```

Run the test cases:

```bash
python -m pytest -v
```

Generate the line and branch coverage report:

```bash
python -m pytest --cov=bookstore_trade_in --cov-branch --cov-report=term-missing
```

Generate the HTML coverage report:

```bash
python -m pytest --cov=bookstore_trade_in --cov-branch --cov-report=html
```

Open `htmlcov/index.html` in a browser to view the detailed coverage report.

## Test Results

- Total test cases: 18
- Line coverage: 100%
- Branch coverage: 100%
- All test cases passed.

## Screenshots

Screenshots demonstrating test execution and coverage results are available in the `Lab6_Screenshots` folder.

## Conclusion

The Bookstore Trade-In system was tested using Pytest. Both line coverage and branch coverage were evaluated to ensure that the program statements and decision branches were tested. The tests achieved complete coverage of the tested program.
