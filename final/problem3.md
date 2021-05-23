## Problem 3
20/20 points (graded)

In a lecture, there are 3 things you might do: listen, sleep, or Facebook (in a single lecture, you might do all, some, or none of them). Lectures are independent of each other, the probabilities associated with the activities are independent of each other, and they are all > 0. You are given the following class, Lecture, and the function, get_mean_and_std.

Write a Monte Carlo simulation called lecture_activities(N, aLecture) that meets the specifications below.

```python
import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION
          
# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)
```

You are not allowed to import anything. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed. Paste only the lecture_activities function and any helper functions you made for yourself (if any).

```python
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object

    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence
             interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION
    result = []
    for i in range(N):
        counter = 0
        while True:
            counter += 1
            if random.random() <= aLecture.get_listen_prob():
                if random.random() <= aLecture.get_sleep_prob():
                    if random.random() <= aLecture.get_fb_prob():
                        result.append(counter)
                        break
    mu, sigma = get_mean_and_std(result)
    width = (mu+1.96*sigma)-(mu-1.96*sigma)
    return (mu, width)
  ```
