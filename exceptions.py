class InvalidExpressionError(ValueError):
    """Raised when an invalid S-expression is encountered"""

    def __init__(self, expression: str):
        super().__init__("Invalid expression: {}".format(expression))