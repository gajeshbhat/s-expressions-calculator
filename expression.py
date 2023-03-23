from typing import List
from functools import reduce

# Threshold (Expression length) for deciding whether to use the recursive or memoized evaluation function
INPUT_THRESHOLD = 15

class SExpressionEvaluator:
    """
    Class for evaluating S-expressions
    """

    # Dictionary containing operations that can be performed on operands
    OPERATIONS = {
        'add': lambda *args: sum(args),
        'multiply': lambda *args: reduce(lambda x, y: x * y, args),
    }

    def __init__(self, expression: str):
        """
        Initialize an instance of the SExpressionEvaluator class
        """

        # Ensure the provided expression is a string
        if not isinstance(expression, str):
            raise TypeError("Expression must be a string")
        
        # Strip whitespace from the expression and save it as an instance variable
        self.expression = expression.strip()

        # Dictionary to memoize previously calculated sub-expressions for optimization
        self.memoized_subexpressions = {}

    def evaluate(self) -> int:
        """
        Evaluate the S-expression and return its result
        """

        # Decide whether to use the recursive or memoized evaluation function based on length
        if len(self.expression) < INPUT_THRESHOLD:
            return self._evaluate_recursive(self.expression)
        else:
            return self._evaluate_memoized(self.expression)

    def _evaluate_recursive(self, expression: str) -> int:
        """
        Recursively evaluate the given S-expression
        """

        # If the sub-expression is a single number, return it as an integer
        if expression.isdigit():
            return int(expression)

        # If the sub-expression is nested, recursively evaluate its sub-expressions
        if '(' not in expression:
            raise ValueError("Invalid expression: {}".format(expression))

        # Find the left and right bounds of the current sub-expression
        right_bound = expression.index(')')
        left_bound = expression[:right_bound].rindex('(')

        # Evaluate the current sub-expression and replace it in the full expression string
        current_expression = expression[left_bound + 1:right_bound].strip()
        current_value = self._evaluate_single(current_expression)

        # Recursively evaluate the modified expression string and memoize the result
        result = self._evaluate_recursive(
            expression[:left_bound] + str(current_value) + expression[right_bound + 1:]
        )
        return result
    
    def _evaluate_memoized(self, expression: str) -> int:
        """
        Evaluate the given S-expression using iteration and memoization
        """

        # Keep replacing nested sub-expressions with their evaluated values until there are no more
        while ')' in expression:
            # If the entire expression has already been evaluated, return the memoized result
            if expression in self.memoized_subexpressions:
                return self.memoized_subexpressions[expression]

            # Find the left and right bounds of the current sub-expression
            right_bound = expression.index(')')
            left_bound = expression[:right_bound].rindex('(')

            # Evaluate the current sub-expression and replace it in the full expression string
            current_expression = expression[left_bound + 1:right_bound].strip()
            current_value = self._evaluate_single(current_expression)

            # If the sub-expression is the only one in the expression string, return its value
            if left_bound == 0:
                return current_value

            # Replace the current sub-expression with its value in the full expression string
            expression = expression[:left_bound] + str(current_value) + expression[right_bound + 1:]

        # If the expression string is just a single number, return it as an integer
        if not expression.isdigit():
            raise ValueError("Invalid expression: {}".format(expression))

        return int(expression)

    def _evaluate_single(self, expression: str) -> int:
        """
        Evaluate a single sub-expression
        """

        # Ensure the provided sub-expression is a string
        if not isinstance(expression, str):
            raise TypeError("Sub-expression must be a string")

        # Check if this sub-expression has already been evaluated and return the result
        if expression in self.memoized_subexpressions:
            return self.memoized_subexpressions[expression]

        try:
            # Split the sub-expression into an operation and its operands
            operation, *operands = expression.split()

            # Convert the operands to integers or floats
            operands = [int(arg) if '.' not in arg else float(arg) for arg in operands]

            # Perform the operation on the operands and save the result in the memoization dictionary
            result = self.OPERATIONS[operation](*operands)
            self.memoized_subexpressions[expression] = result

            return result

        except (ValueError, TypeError, KeyError):
            raise ValueError("Invalid sub-expression: {}".format(expression))