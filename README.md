# Lab 07 - Practical Python: Recursion and Objects

In this lab, we'll practise two ideas from this week's lectures: **recursion** (a
function that calls itself on a smaller version of its problem) and **object-oriented
programming** (bundling data and behaviour together in a **class**). You'll write two
recursive functions and two small classes, checked against a set of automated tests.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 07 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

You should be a member of the **CSCI1030U** organization on GitHub, from the invitation
sent out after Lab 01. If you never accepted that invitation, do it now (check your email,
or go to <https://github.com/CSCI1030U>) - you can't create your lab repository until
you're a member. Tell your lab instructor if no invitation ever arrived.

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 07 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** `CSCI1030U` (the organization, *not* your own account)
   - **Repository name:** `lab07-your-username` - for example `lab07-jsmith2026`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab07-your-username
cd lab07-your-username
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

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 07 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 07 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab07-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
