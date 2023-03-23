# You need to install line_profiler package to run this script:
from calc import SExpressionEvaluator
from line_profiler import LineProfiler

def profile_recursive():
    expression = "(add (multiply 2 3) (multiply (add 1 2) (add 3 4) (add 5 6)) (multiply 7 8))"
    evaluator = SExpressionEvaluator(expression)
    evaluator._evaluate_recursive(expression)

def profile_memoized():
    expression = "(add (multiply 2 3) (multiply (add 1 2) (add 3 4) (add 5 6)) (multiply 7 8))"
    evaluator = SExpressionEvaluator(expression)
    evaluator._evaluate_memoized(expression)

# Initialize the profiler and add the functions to be profiled:
profiler = LineProfiler()
profiler.add_function(profile_memoized)
profiler.add_function(profile_recursive)

# Run the profiler and print the results for recursive and memoized functions:
profiler.run('profile_recursive()')
profiler.print_stats()

profiler.run('profile_memoized()')
profiler.print_stats()
