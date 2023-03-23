#!/usr/bin/env python3
import sys
from expression import SExpressionEvaluator

def main():
    """
    Main function that reads an S-expression from the command line and evaluates it
    """
    try:
        expression = SExpressionEvaluator(sys.argv[1])
        print(expression.evaluate())
    except ValueError as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)
    except IndexError:
        print("Error: expression not provided")
        sys.exit(1)

if __name__ == '__main__':
    main()
