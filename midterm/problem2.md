## Problem 2-1
0.0/2.0 points (graded)\
Which of the following problems can be solved using dynamic programming? Check all that work.

Selected - Sum of elements - Given a list of integer elements, find the sum of all the elements.\
Binary search - Given a list of elements, check if the element X is in the list.\
Selected - Dice throws - Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.\
incorrect


## Problem 2-2
2.0/2.0 points (graded)\
What is the exact probability of rolling at least two 6's when rolling a die three times?

2/27\
correct


## Problem 2-3
2.0/2.0 points (graded)\
A greedy optimization algorithm

is typically efficient in time.\
correct


## Problem 2-4
2.0/2.0 points (graded)\
Suppose you have a weighted directed graph and want to find a path between nodes A and B with the smallest total weight. Select the most accurate statement.

If all edges have weight 2, breadth-first search guarantees that the first path found to be is the shortest path.\
correct


## Problem 2-5
2.0/2.0 points (graded)\
Which of the following functions are deterministic?
```python
import random
        
def F():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
```
Both F and G\
correct


## Problem 2-6
0.0/2.0 points (graded)\
Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,

in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11\
in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16\
One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has seen. What is the time complexity of this algorithm in terms of the length of the list, N?

none of the above\
incorrect
