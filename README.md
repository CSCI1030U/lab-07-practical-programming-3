# Lab 07 - Practical Python: Recursion and Objects

In this lab, we'll practise two ideas from this week's lectures: **recursion** (a
function that calls itself on a smaller version of its problem) and **object-oriented
programming** (bundling data and behaviour together in a **class**). You'll write two
recursive functions and two small classes, checked against a set of automated tests.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect.

## Getting Started

Accept the GitHub Classroom assignment invitation in Canvas (the link is in the lab
assignment on Canvas), which will clone your own copy of the repository. In the folder
where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab07-your-username
```

## Instructions

You will edit **`lab07.py`**. The function and class names are already written for you -
**do not rename them** - fill in the bodies where you see `# TODO`.

**Parts 1 and 2 must use recursion** (the function calling itself) - **no loops**.

### Part 1 - `count_occurrences(target, values)`

Write `count_occurrences` **recursively** so it returns how many times `target` appears
in the list `values`.

- **Base case:** an empty list contains `target` zero times.
- **Recursive case:** `1` if the first item equals `target` (otherwise `0`), plus the
  count in the rest of the list (`values[1:]`).

```python
count_occurrences(2, [1, 2, 2, 3, 2])   # returns 3
count_occurrences(5, [1, 2, 3])         # returns 0
count_occurrences("a", ["a", "b", "a"]) # returns 2
```

### Part 2 - `is_sorted(values)`

Write `is_sorted` **recursively** so it returns `True` when `values` is in
non-decreasing order (each item is `<=` the next one) and `False` otherwise.

- **Base case:** a list with 0 or 1 items is already sorted.
- **Recursive case:** the first two items are in order **and** the rest of the list is
  sorted.

```python
is_sorted([1, 2, 3])   # returns True
is_sorted([2, 2, 3])   # returns True   (equal values are fine)
is_sorted([1, 3, 2])   # returns False
```

### Part 3 - the `Rectangle` class

Fill in the `Rectangle` class so that each rectangle stores a `width` and a `height`
and offers:

- `area()` - returns `width * height`;
- `perimeter()` - returns `2 * (width + height)`;
- `__str__()` - returns `"<width>x<height>"` (this is what `print()` and `str()` show).

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
str(r)          # "3x4"
```

Hint: store the values in `__init__` as `self.width` and `self.height`, then use them
in the other methods.

### Part 4 - the `Square` class  *(stretch - optional)*

A square is just a rectangle whose width and height are equal. Fill in `Square` so it
**inherits** from `Rectangle`: its `__init__(self, side)` should call the `Rectangle`
constructor with `side` for both width and height, using `super().__init__(...)`. You
don't need to rewrite `area`, `perimeter`, or `__str__` - they're inherited.

```python
s = Square(5)
s.area()   # 25
str(s)     # "5x5"
```

This part is optional - the three parts above are the core of the lab.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

Read the output closely - a failing test tells you which piece is wrong and shows what
it expected versus what your code produced. Fix, save, and run `pytest` again.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Once your tests pass (or the session is ending), commit and push:

```
git add --all
git commit -m "Lab 07 completed"
git push origin main
```

You can confirm the autograder ran correctly by opening the **Actions** tab on your
repository page in GitHub. It can take a minute or two.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
