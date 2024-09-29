# Week4 :  Calculator App  
This project is an Advanced calculator implemented in Python that performs basic arithmetic operations: 
Addition, Subtraction, Multiplication, and Division. 
The calculator is designed using object-oriented principles and showcases various design patterns, including class methods, static methods, and a calculation history feature.
Using the Faker Library to test the functionalities with randomly generated fake test Data.
Test the functionality on the command line: "python main.py 1 2 add"

## Set up: 
Python Virtual Environments: Essential for managing project-specific dependencies. 

Pytest: A powerful framework for writing and running Python tests.

Pylint: A tool for analyzing your Python code for errors and enforcing a coding standard.

Coverage: A tool for measuring the coverage of your unit tests.

Installed Faker Library

Deactivated and Activated Virtual env

Added ConfTest file to test data using Faker Library

## Main Principes followed:
Follow DRY Principle (Don't Repeat Yourself)

Separation of Concerns -- Separate each part that the program needs to do, so it is organized and the functionals only have to do ONE thing. Steps Followed:

## Testing Commands:
pytest --num_records=10

pytest --pylint --cov

## Testing From Terminal based on user input: 
"5", "3", 'add', "The result of 5 add 3 is equal to 8"

"10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"

"4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"

"20", "4", 'divide', "The result of 20 divide 4 is equal to 5"

"1", "0", 'divide', "An error occurred: Cannot divide by zero"

"9", "3", 'unknown', "Unknown operation: unknown" # Test for unknown operation

"a", "3", 'add', "Invalid number input: a or 3 is not a valid number." # Testing invalid number input

"5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number." # Testing another invalid number input

# Command Line Test Results:

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$ python main.py a b add

Invalid number input: a or b is not a valid number.

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$ python main.py 1 0 divide

An error occurred: Cannot divide by zero

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$  python main.py 1 2 divide

The result of 1 divide 2 is equal to 0.5

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$ python main.py 1 2 multiply

The result of 1 multiply 2 is equal to 2

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$  python main.py 5 2 subtract

The result of 5 subtract 2 is equal to 3

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$  python main.py 1 2 add

The result of 1 add 2 is equal to 3

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$ 

# pytest --pylint --cov Test Results:

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$   pytest --pylint --cov

Linting files
.....
--------------------------------------------------------------------------------


tests/test_operations.py::test_divide_by_zero PASSED                                                                                                [100%]


 ---------- coverage: platform linux, python 3.10.12-final-0 ----------

Name                         Stmts   Miss  Cover

------------------------------------------------

calculator/__init__.py          22      0   100%

calculator/calculation.py       15      0   100%

calculator/calculations.py      22      0   100%

calculator/operations.py        11      0   100%

main.py                         25      7    72%

tests/__init__.py                0      0   100%

tests/conftest.py               28      3    89%

tests/test_calculation.py       15      0   100%

tests/test_calculations.py      31      0   100%

tests/test_calculator.py         9      0   100%

tests/test_main.py               7      0   100%

tests/test_operations.py        11      0   100%

------------------------------------------------

TOTAL                          196     10    95%

# pytest --num_records=10 Test Results:

(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$  pytest --num_records=10
=================================================================== test session starts ===================================================================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0 -- /home/mallikakasi/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project/VMKenv/bin/python
cachedir: .pytest_cache
rootdir: /home/mallikakasi/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project
configfile: pytest.ini
testpaths: tests
plugins: pylint-0.21.0, cov-4.1.0, Faker-23.1.0
collected 41 items                                                                                                                                        

tests/test_calculation.py::test_calculation_operations[a0-b0-divide-expected0] PASSED                                                               [  2%]
tests/test_calculation.py::test_calculation_operations[a1-b1-subtract-expected1] PASSED                                                             [  4%]
tests/test_calculation.py::test_calculation_operations[a2-b2-add-expected2] PASSED                                                                  [  7%]
tests/test_calculation.py::test_calculation_operations[a3-b3-subtract-expected3] PASSED                                                             [  9%]
tests/test_calculation.py::test_calculation_operations[a4-b4-divide-expected4] PASSED                                                               [ 12%]
tests/test_calculation.py::test_calculation_operations[a5-b5-subtract-expected5] PASSED                                                             [ 14%]
tests/test_calculation.py::test_calculation_operations[a6-b6-subtract-expected6] PASSED                                                             [ 17%]
tests/test_calculation.py::test_calculation_operations[a7-b7-subtract-expected7] PASSED                                                             [ 19%]
tests/test_calculation.py::test_calculation_operations[a8-b8-divide-expected8] PASSED                                                               [ 21%]
tests/test_calculation.py::test_calculation_operations[a9-b9-multiply-expected9] PASSED                                                             [ 24%]
tests/test_calculation.py::test_calculation_repr PASSED                                                                                             [ 26%]
tests/test_calculation.py::test_divide_by_zero PASSED                                                                                               [ 29%]
tests/test_calculations.py::test_add_calculation PASSED                                                                                             [ 31%]
tests/test_calculations.py::test_get_history PASSED                                                                                                 [ 34%]
tests/test_calculations.py::test_clear_history PASSED                                                                                               [ 36%]
tests/test_calculations.py::test_get_latest PASSED                                                                                                  [ 39%]
tests/test_calculations.py::test_find_by_operation PASSED                                                                                           [ 41%]
tests/test_calculations.py::test_get_latest_with_empty_history PASSED                                                                               [ 43%]
tests/test_calculator.py::test_addition PASSED                                                                                                      [ 46%]
tests/test_calculator.py::test_subtraction PASSED                                                                                                   [ 48%]
tests/test_calculator.py::test_multiply PASSED                                                                                                      [ 51%]
tests/test_calculator.py::test_divide PASSED                                                                                                        [ 53%]
tests/test_main.py::test_calculate_and_print[5-3-add-The result of 5 add 3 is equal to 8] PASSED                                                    [ 56%]
tests/test_main.py::test_calculate_and_print[10-2-subtract-The result of 10 subtract 2 is equal to 8] PASSED                                        [ 58%]
tests/test_main.py::test_calculate_and_print[4-5-multiply-The result of 4 multiply 5 is equal to 20] PASSED                                         [ 60%]
tests/test_main.py::test_calculate_and_print[20-4-divide-The result of 20 divide 4 is equal to 5] PASSED                                            [ 63%]
tests/test_main.py::test_calculate_and_print[1-0-divide-An error occurred: Cannot divide by zero] PASSED                                            [ 65%]
tests/test_main.py::test_calculate_and_print[9-3-unknown-Unknown operation: unknown] PASSED                                                         [ 68%]
tests/test_main.py::test_calculate_and_print[a-3-add-Invalid number input: a or 3 is not a valid number.] PASSED                                    [ 70%]
tests/test_main.py::test_calculate_and_print[5-b-subtract-Invalid number input: 5 or b is not a valid number.] PASSED                               [ 73%]
tests/test_operations.py::test_operation[a0-b0-subtract-expected0] PASSED                                                                           [ 75%]
tests/test_operations.py::test_operation[a1-b1-multiply-expected1] PASSED                                                                           [ 78%]
tests/test_operations.py::test_operation[a2-b2-subtract-expected2] PASSED                                                                           [ 80%]
tests/test_operations.py::test_operation[a3-b3-add-expected3] PASSED                                                                                [ 82%]
tests/test_operations.py::test_operation[a4-b4-subtract-expected4] PASSED                                                                           [ 85%]
tests/test_operations.py::test_operation[a5-b5-add-expected5] PASSED                                                                                [ 87%]
tests/test_operations.py::test_operation[a6-b6-add-expected6] PASSED                                                                                [ 90%]
tests/test_operations.py::test_operation[a7-b7-multiply-expected7] PASSED                                                                           [ 92%]
tests/test_operations.py::test_operation[a8-b8-divide-expected8] PASSED                                                                             [ 95%]
tests/test_operations.py::test_operation[a9-b9-add-expected9] PASSED                                                                                [ 97%]
tests/test_operations.py::test_divide_by_zero PASSED                                                                                                [100%]

=================================================================== 41 passed in 0.55s ====================================================================
(VMKenv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week4/Week4_Project$

