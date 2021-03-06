'''
Problem 4
20.0/20.0 points (graded)
Write a function that meets the following specification. Hint: there exists a greedy algorithm that provides an optimal solution to this problem.

def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
You are not allowed to import anything. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed. Paste only the solve function and any helper functions you made for yourself (if any).
'''

def solve(s):
    """
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    result = [0, 0, 0, 0]
    multiplier = [25, 10, 5, 1]
    for x in range(len(result)):
        while (result[x] + 1) * multiplier[x] <= s:
            result[x] += 1
        s = s - result[x] * multiplier[x]
    return result
