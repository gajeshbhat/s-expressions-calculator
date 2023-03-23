## Encircle Site Reliablity Engineering Coding Assignment

### Author : Gajesh Bhat (gajeshbht@gmail.com)


**Question:** Write a command line program that acts as a simple calculator: it takes a
single argument as an expression and prints out the integer result of
evaluating it.

Assuming the program is implemented in Python, invocations should look like:

    $ ./calc.py 123
    123

    $ ./calc.py "(add 12 12)"
    24

    $ ./calc.py "(add 1 (multiply 2 3))"
    7

    $ ./calc.py "(multiply 2 (add (multiply 2 3) 8))"
    28

More details on the problem https://gist.github.com/rraval/2ef5e2ff228e022653db2055fc12ea9d

### How to run the program

    $ ./calc.py 123

    or 

    $ ./calc.py "(add 12 12)"

## Note:

1. Executable file is calc.py
2. If the file is not executable then run the following command (I have made it executable by default) `chmod +x calc.py`
3. If you want to run it as a python script then run the following command `python3 calc.py 123` , `python3 calc.py "(add 12 12)"`

## Approach to solve the problem

### Recursive implementation

1. I started out with a recurisve implementation which was a version of `_evaluate_recursive` to start with.
2. The method first checks if the input expression is a single number, and if it is, returns it as an integer. If the input expression is not a number, the method assumes that it contains nested sub-expressions and recursively evaluates each sub-expression until all sub-expressions have been evaluated and replaced with their corresponding values.
3. To recursively evaluate a sub-expression, the method first finds the left and right bounds of the sub-expression by locating the opening and closing parentheses. It then evaluates the sub-expression by calling the _evaluate_single() method, which splits the sub-expression into an operation and its operands, performs the operation on the operands, and returns the result.
4. The method then replaces the evaluated sub-expression with its value in the full expression string and recursively calls itself on the modified string until all sub-expressions have been evaluated and replaced.
5. The method returns the final result of evaluating the full expression string.
6. The advantage of the recursive method is that it is easy to implement and understand, and it can handle S-expressions of any depth. However, the recursive method can be slow for very deeply nested S-expressions because it has to keep making recursive function calls for each sub-expression. This can lead to stack overflow errors for very large expressions. Additionally, since the recursive method evaluates each sub-expression multiple times, it can be less efficient than the memoized method for large expressions.
7. **Time complexity** of the recursive method is `O(n^2)` because it has to evaluate each sub-expression multiple times. Assuming that the input expression has n sub-expressions each sub-expression may be recursively evaluated multiple times, and there can be up to n sub-expressions in the input expression. The **Space complexity** of the recursive solution also depends on the depth of the expression. In the worst case, the space complexity is `O(d)`, where `d` is the depth of the expression. This is because the recursive calls are added to the call stack, which grows linearly with the depth of the expression. For very deep expressions, this can lead to a stack overflow error.

### Memoized Iterative implementation

1. After implementing the recursive solution, I proceeded to implement the memoized iterative solution using `_evaluate_memoized()` method.
2. The memoized method evaluates each sub-expression exactly once and memoizes the result in a dictionary to avoid re-evaluating it in the future.
3. The method uses a while loop to iterate over the expression string until all sub-expressions have been evaluated and replaced with their corresponding values. Within the while loop, the method finds the left and right bounds of the current sub-expression, evaluates the sub-expression, and replaces it with its value in the expression string. If the entire expression has already been evaluated, the method returns the memoized result.
4. The advantage of the memoized method is that it is more efficient than the recursive method for large expressions because it evaluates each sub-expression only once and memoizes the result to avoid re-evaluating it in the future. Additionally, since the method does not make recursive function calls, it avoids the risk of stack overflow errors.

5. The **Time complexity** of the memoized method is `O(n)` because it evaluates each sub-expression exactly once, and there can be up to `n` sub-expressions in the input expression. The Space complexity of the memoized method is also `O(n)` because the memoization dictionary can store up to n sub-expressions, and the expression string itself is also stored in memory.


## Testing
1. I have added a test file `test_expression.py` to test the S-expression evaluation class.

2. To execute the test file run the following command  `python -m unittest test_expression.py`

3. I could not get the time to write custom exceptions to the Value Errors raised and wrote a test anywway so that I can impelment it later. (1 test fails because of this!)

## Profiling
1. I have added a profiling file `profile_expression.py` to profile the S-expression evaluation class.
2. I used the `line profiler` package to profile the two different implementations for S-expression evaluation. You can install it by running `pip install line_profiler` or by running `pip install -r requirements.txt`
3. To execute the profiling file run the following command `python profile_expression.py`
4. Below are the results for the input `"(add (multiply 2 3) (multiply (add 1 2) (add 3 4) (add 5 6)) (multiply 7 8))"`
```
Total time: 8.9e-05 s
File: /Users/gajesh/git/Encircle/profile_expression.py
Function: profile_recursive at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           def profile_recursive():
     6         1       1000.0   1000.0      1.1      expression = "(add (multiply 2 3) (multiply (add 1 2) (add 3 4) (add 5 6)) (multiply 7 8))"
     7         1       4000.0   4000.0      4.5      evaluator = SExpressionEvaluator(expression)
     8         1      84000.0  84000.0     94.4      evaluator._evaluate_recursive(expression)

Total time: 6.9e-05 s
File: /Users/gajesh/git/Encircle/profile_expression.py
Function: profile_memoized at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           def profile_memoized():
    11         1       1000.0   1000.0      1.4      expression = "(add (multiply 2 3) (multiply (add 1 2) (add 3 4) (add 5 6)) (multiply 7 8))"
    12         1       5000.0   5000.0      7.2      evaluator = SExpressionEvaluator(expression)
    13         1      63000.0  63000.0     91.3      evaluator._evaluate_memoized(expression)
```
5. After running the profiler many times, I found that the memoized method is consistently faster than the recursive method espicially for larger inputs. The recursive method can also be speed up by memoizing the results of the recursive calls.

## Additional feature and optimizations

1. I also did a minor optimization on the program by adding the `_evaluate` method and allowing it to choose the appropriate method to evaluate the expression based on the size of the expression. The `_evaluate` method uses the memoized method for expressions with more than 100 characters and the recursive method for expressions with less than 100 characters. This optimization is not very significant, but it does help speed up the program for large expressions.