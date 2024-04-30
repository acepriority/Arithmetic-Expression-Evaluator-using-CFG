# Arithmetic-Expression-Evaluator-using-CFG

This Python script evaluates arithmetic expressions using a context-free grammar (CFG) approach. It supports addition, subtraction, multiplication, and division operations, as well as parentheses for grouping.

## Usage
To use the arithmetic expression evaluator, simply call the evaluate_expression function with a valid arithmetic expression as input. The function will return the result of the evaluation.

Example:
result = evaluate_expression('2+2*3')
print(result)  # Output: 8

## Context-Free Grammar (CFG)
The arithmetic expressions are parsed according to the following CFG:

expression -> term
            | expression + term
            | expression - term

term -> factor
      | term * factor
      | term / factor

factor -> num
        | (expression)

Implementation Details
The evaluate_expression function tokenizes the input expression using regular expressions to separate numbers and operators.
Three parsing functions (parse_expression, parse_term, and parse_factor) are defined to recursively parse and evaluate arithmetic expressions according to the CFG.
The parsing functions handle arithmetic operations and parentheses by evaluating subexpressions and combining results.
The eval() function is used to perform arithmetic operations dynamically.
Basic error handling is included to handle invalid input tokens or malformed expressions.

Dependencies
The script requires the re module for regular expression tokenization.

License
This project is licensed under the MIT License - see the LICENSE file for details.
