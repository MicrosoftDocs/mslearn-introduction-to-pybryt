```python
!pip install -Uqq pybryt
!wget -q https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-pybryt/main/exercise_utils.py
import pybryt
from exercise_utils import fiberator
from typing import Any, Dict, List, Optional

def run_test_cases(fib_fn):
    global annotations
    annotations = []
    for n, expected in zip(range(1, 31), fiberator()):
        actual = fib_fn(n)
        assert actual == expected
    print("All test cases passed!")
```

In this exercise, you will create a reference implementation using PyBryt, and we'll check that reference using PyBryt.

Recall that throughout this module, our goal has been to write a problem that will ask students to implement a dynamic programming solution to calculating numbers in the Fibonacci sequence. The function `fib` below does this for us: it takes in an integer $n$ and returns the $n^\text{th}$ Fibonacci number (starting from 1).

Annotate the fib function to create a simple reference implementation for the algorithm it implements, which we will test with PyBryt. Here's what you need to do:

* Replace the `...` prompts with calls to `pybryt.Value(<some value>)` call from PyBryt library. 
* Append your annotations to the list `annotations`.

_Tip:_ Try implementing yourself first, referring to the previous chapter if you need to. There's a solution at the bottom, should you get stuck.


```python
annotations = []  # collect your annotations in this list

def fib(n: int) -> int:
    fib_nums = [None for _ in range(n)]
    ...

    fib_nums[0] = 0
    ...

    if n > 1:
        fib_nums[1] = 1
        ...

        for i in range(2, n):
            fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]
            ...

    return fib_nums[n - 1]
```

In order to test the various solutions presented in this exercise, the `run_test_cases` function runs a simple unit test of the Fibonacci number generator passed to it on the first 30 numbers in the Fibonacci sequence. It also resets and populates the `annotations` list when we pass it the `fib` function, so run the cell below to create all of your annotations in preparation for the next step.


```python
run_test_cases(fib)
```

If the implementation is incorrect, `run_test_cases` raises an error, although all of the solutions in this exercise are correct; rather, the goal here is to determine whether the solutions follow the specified algorithm for generating the numbers in a way that a simple test case can't.

Now that we have some annotations, let's contruct a reference implementation. Assign the variable `ref` to a reference implementation created from the `annotations` list you populated in the `fib` function. Fill in the `...` prompt with a call like `pybryt.ReferenceImplementation(<some args>)` to create the reference implementation. Recall that the constructor takes two arguments: the name of the reference (a string) and the list of annotations.


```python
ref = ...
ref 
```

Now that you've got the correct reference implementation, let's try running it against some student implementations. As a sanity check, we'll run your reference against the solution above. You should see only your success messages, and that the reference was satisfied.


```python
with pybryt.check(ref):
    run_test_cases(fib)
```

Now let's check a few implementations which return the correct answer (that is, they pass our `run_test_cases` function), but which don't implement the algorithm in the same way. The next cell defines a version that uses an infinite generator to generate the Fibonacci sequence without storing the intermediate results in a list. You should see that your reference was not satisfied, and all of your failure messages.


```python
def fib_gen(n: int) -> int:
    def fiberator():
        i, j = 0, 1
        yield i
        yield j
        while True:
            i, j = j, i + j
            yield j
    fib = fiberator()
    for _ in range(n):
        ret = next(fib)
    return ret

with pybryt.check(ref):
    run_test_cases(fib_gen)
```

The next implementation uses a similar dynamic programming implementation of the Fibonacci sequence, but it doesn't create a full-sized list at the beginning, instead appending elements with each iteration. You should see some of your success messages here, because one the `for` loop finishes we end up with the same fully-populated list we expect in the reference implementation, but otherwise you should see your failure messages.


```python
def fib_append(n: int) -> int:
    fib_nums = []
    fib_nums.append(0)
    if n > 1:
        fib_nums.append(1)
        for i in range(2, n):
            fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    return fib_nums[n - 1]

with pybryt.check(ref):
    run_test_cases(fib_append)
```

Finally, let's look at an implementation of Fibonacci that doesn't use dynamic programming at all; instead, the version below uses a `dict` to remember old values of the function, and uses the normal recursive algorithm to generate the values when it can't find them. Here, again, you should only see your failure messages.


```python
def fib_dict(n: int, cache: Dict[int, int] = {}):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in cache:
        return cache[n]
    val = fib_dict(n - 1, cache) + fib_dict(n - 2, cache)
    cache[n] = val
    return val

with pybryt.check(ref):
    run_test_cases(fib_dict)
```

## Solution

Here's an annotated version of the `fib` function from above:

```python
def fib(n: int) -> int:
    fib_nums = [None for _ in range(n)]
    annotations.append(pybryt.Value(fib_nums, success_message="sm1", failure_message="fm1"))

    fib_nums[0] = 0
    annotations.append(pybryt.Value(fib_nums, success_message="sm2", failure_message="fm2"))

    if n > 1:
        fib_nums[1] = 1
        annotations.append(pybryt.Value(fib_nums, success_message="sm3", failure_message="fm3"))

        for i in range(2, n):
            fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]
            annotations.append(pybryt.Value(fib_nums, success_message="sm4", failure_message="fm4"))

    return fib_nums[n - 1]
```
