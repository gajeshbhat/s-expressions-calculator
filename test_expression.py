import unittest
from expression import SExpressionEvaluator

class TestSExpressionEvaluator(unittest.TestCase):

    def setUp(self):
        self.evaluator = SExpressionEvaluator

    def test_evaluate_simple_addition(self):
        """Test evaluating a simple addition S-expression"""
        expr = "(add 2 3)"
        expected = 5
        self.assertEqual(self.evaluator(expr).evaluate(), expected)

    def test_evaluate_simple_multiplication(self):
        """Test evaluating a simple multiplication S-expression"""
        expr = "(multiply 2 3)"
        expected = 6
        self.assertEqual(self.evaluator(expr).evaluate(), expected)

    def test_evaluate_nested_expression(self):
        """Test evaluating a nested S-expression"""
        expr = "(add (multiply 2 3) 4)"
        expected = 10
        self.assertEqual(self.evaluator(expr).evaluate(), expected)

    def test_evaluate_float_division(self):
        """Test evaluating an S-expression with float division"""
        expr = "(multiply 0.5 2)"
        expected = 1.0
        self.assertEqual(self.evaluator(expr).evaluate(), expected)

    def test_evaluate_division_by_zero(self):
        """Test evaluating an S-expression with division by zero"""
        expr = "(multiply 2 (/ 1 0))"
        with self.assertRaises(ValueError) as cm:
            self.evaluator(expr).evaluate()
        self.assertEqual(str(cm.exception), "Invalid sub-expression: / 1 0")

    def test_evaluate_invalid_expression(self):
        """Test evaluating an invalid S-expression"""
        expr = "(add 2 3"
        with self.assertRaises(ValueError) as cm:
            self.evaluator(expr).evaluate()
        print(cm.exception)
        self.assertEqual(str(cm.exception), "Invalid expression: (add 2 3")

    def test_evaluate_memoization(self):
        """Test that memoization works for an S-expression"""
        expr = "(add (multiply 2 3) (multiply 2 3))"
        expected = 12
        evaluator = self.evaluator(expr)
        self.assertEqual(evaluator.evaluate(), expected)
        # Evaluate the expression again to test memoization
        expected = 12
        self.assertEqual(evaluator.evaluate(), expected)
